"""
NASA Dataset Extractor & Preprocessing Pipeline (ETL).
NASA Hackathon Core Engine:
This module demonstrates extracting, clipping, calibrating, and preprocessing
official NASA Earth Observation datasets for Bangladesh Agro-Ecological Zones (AEZ).

Target NASA Missions & Products:
1. GPM IMERG (Global Precipitation Measurement) - Product: GPM_3IMERGDF
2. MODIS Land Surface Temperature & Emissivity - Product: MOD11A2 / MYD11A2
3. SMAP L4 Global Root Zone Soil Moisture - Product: SPL4SMGP
4. Landsat 8/9 OLI & MODIS NDVI/EVI - Product: MOD13Q1
"""

import json
import math
from pathlib import Path
from typing import Dict, Any, List

# Target Bounding Box for Bangladesh: 20.57°N to 26.63°N, 88.03°E to 92.67°E
BANGLADESH_BBOX = {
    "min_lat": 20.57,
    "max_lat": 26.63,
    "min_lon": 88.03,
    "max_lon": 92.67
}

class NASADataPreprocessor:
    """Extracts raw satellite observations, applies scientific calibrations, and formats them for agents."""

    def __init__(self, output_dir: str = "backend/data/processed"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def calibrate_modis_lst(self, raw_digital_number: float) -> float:
        """
        NASA MODIS MOD11A2 Calibration formula:
        LST_Kelvin = raw_DN * 0.02
        LST_Celsius = LST_Kelvin - 273.15
        """
        kelvin = raw_digital_number * 0.02
        celsius = kelvin - 273.15
        return round(celsius, 2)

    def calculate_ndvi(self, nir_reflectance: float, red_reflectance: float) -> float:
        """
        Normalized Difference Vegetation Index (NDVI):
        NDVI = (NIR - RED) / (NIR + RED)
        Range: -1.0 to +1.0
        """
        denominator = nir_reflectance + red_reflectance
        if denominator == 0:
            return 0.0
        return round((nir_reflectance - red_reflectance) / denominator, 3)

    def calculate_smap_moisture_stress(self, root_zone_m3_m3: float, wilting_point: float = 0.17) -> Dict[str, Any]:
        """
        Calculates soil moisture deficit relative to plant permanent wilting point.
        """
        deficit = max(0.0, wilting_point - root_zone_m3_m3)
        stress_percentage = min(100.0, (deficit / wilting_point) * 100.0) if deficit > 0 else 0.0
        status = "CRITICAL_DEFICIT" if stress_percentage > 40 else ("MODERATE_STRESS" if stress_percentage > 0 else "OPTIMAL")
        return {
            "root_zone_moisture_m3_m3": root_zone_m3_m3,
            "wilting_point_threshold": wilting_point,
            "stress_percentage": round(stress_percentage, 1),
            "status": status
        }

    def process_raw_dataset_records(self) -> Dict[str, Any]:
        """
        Simulates parsing raw telemetry frames from NASA data portals
        and transforming them into standardized multi-agent features.
        """
        # Preprocessing matrices for core agricultural regions
        raw_telemetry_batch = [
            {
                "region_id": "rajshahi",
                "region_name": "High Barind Tract (Rajshahi/Naogaon)",
                "lat": 24.3745,
                "lon": 88.6042,
                "raw_gpm_precip_rate_mm_hr": 0.048,   # ~1.15 mm/day
                "raw_modis_lst_dn": 15717,            # 15717 * 0.02 = 314.34 K = 41.19 °C
                "raw_smap_rootzone_val": 0.158,       # Below 0.17 wilting point
                "landsat_nir": 0.42,
                "landsat_red": 0.18,
                "historical_evi_slope": -0.024        # 5-year degradation slope from continuous rice mono-cropping
            },
            {
                "region_id": "sylhet",
                "region_name": "Haor Basin (Sylhet/Sunamganj)",
                "lat": 25.0658,
                "lon": 91.4073,
                "raw_gpm_precip_rate_mm_hr": 0.385,   # ~9.24 mm/day (High flash flood trigger)
                "raw_modis_lst_dn": 15250,            # ~31.85 °C
                "raw_smap_rootzone_val": 0.442,       # Saturated / high standing water
                "landsat_nir": 0.58,
                "landsat_red": 0.12,
                "historical_evi_slope": -0.005
            },
            {
                "region_id": "rangpur",
                "region_name": "Tista Floodplain (Rangpur/Dinajpur)",
                "lat": 25.7439,
                "lon": 89.2752,
                "raw_gpm_precip_rate_mm_hr": 0.115,   # ~2.76 mm/day
                "raw_modis_lst_dn": 15510,            # ~37.05 °C
                "raw_smap_rootzone_val": 0.215,       # Moderate moisture
                "landsat_nir": 0.51,
                "landsat_red": 0.19,
                "historical_evi_slope": -0.016
            },
            {
                "region_id": "khulna",
                "region_name": "Coastal Saline Zone (Khulna/Satkhira)",
                "lat": 22.8456,
                "lon": 89.5403,
                "raw_gpm_precip_rate_mm_hr": 0.150,   # ~3.60 mm/day
                "raw_modis_lst_dn": 15435,            # ~35.55 °C
                "raw_smap_rootzone_val": 0.318,
                "landsat_nir": 0.45,
                "landsat_red": 0.17,
                "historical_evi_slope": -0.028        # Salinity & mono-cropping degradation
            }
        ]

        processed_registry = {}

        for item in raw_telemetry_batch:
            # 1. Calibrate GPM Precipitation
            daily_precip_mm = round(item["raw_gpm_precip_rate_mm_hr"] * 24, 2)
            flood_index = min(100, int((daily_precip_mm / 10.0) * 100))

            # 2. Calibrate MODIS LST
            surface_temp_c = self.calibrate_modis_lst(item["raw_modis_lst_dn"])
            drought_heat_index = min(100, max(0, int((surface_temp_c - 28.0) * 7.5)))

            # 3. Calibrate SMAP Root-zone Moisture
            moisture_analysis = self.calculate_smap_moisture_stress(item["raw_smap_rootzone_val"])

            # 4. Landsat/MODIS NDVI Calculation
            ndvi = self.calculate_ndvi(item["landsat_nir"], item["landsat_red"])

            # 5. Land Degradation Factor (EVI Trend + Monoculture fatigue)
            degradation_risk = "HIGH" if item["historical_evi_slope"] < -0.020 else ("MODERATE" if item["historical_evi_slope"] < -0.010 else "LOW")

            processed_registry[item["region_id"]] = {
                "region_id": item["region_id"],
                "region_name": item["region_name"],
                "coordinates": {"lat": item["lat"], "lon": item["lon"]},
                "nasa_gpm_imerg": {
                    "product_id": "GPM_3IMERGDF_07",
                    "daily_precipitation_mm": daily_precip_mm,
                    "flood_vulnerability_index": flood_index,
                    "extreme_rain_warning": daily_precip_mm > 7.0
                },
                "nasa_modis_lst": {
                    "product_id": "MOD11A2_061",
                    "calibrated_lst_celsius": surface_temp_c,
                    "drought_heat_stress_index": drought_heat_index,
                    "thermal_evapotranspiration_risk": "CRITICAL" if surface_temp_c > 40.0 else ("ELEVATED" if surface_temp_c > 35.0 else "NORMAL")
                },
                "nasa_smap_hydrology": {
                    "product_id": "SPL4SMGP_007",
                    **moisture_analysis
                },
                "nasa_landsat_modis_agronomy": {
                    "product_id": "MOD13Q1_061 / Landsat-8_SR",
                    "calculated_ndvi": ndvi,
                    "vegetation_health_status": "VIGOROUS" if ndvi > 0.55 else ("MODERATE" if ndvi > 0.40 else "STRESSED"),
                    "five_year_evi_trend_slope": item["historical_evi_slope"],
                    "land_degradation_risk": degradation_risk
                }
            }

        # Save to processed JSON
        output_path = self.output_dir / "preprocessed_nasa_aez_dataset.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(processed_registry, f, indent=2, ensure_ascii=False)

        print(f"[SUCCESS] NASA Dataset Extracted & Preprocessed -> Saved to {output_path}")
        return processed_registry

if __name__ == "__main__":
    preprocessor = NASADataPreprocessor()
    preprocessor.process_raw_dataset_records()

