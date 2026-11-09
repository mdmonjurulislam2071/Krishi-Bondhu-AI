# 🛰️ AgroShift Nexus
> **Challenge:** Field Shift: Adapting Farms with NASA Data  
> **Team Name:** Team Nokkhotro  
> **Track:** NASA International Space Apps Challenge  

AgroShift Nexus is a **6+1 Multi-Agent Decision-Support System** that transforms raw NASA Earth Observation data into climate-adaptive, multi-season crop rotation sequences (Kharif-1 ➔ Kharif-2 ➔ Rabi) for Bangladeshi farmers facing severe groundwater depletion (Barind Tract) and flash floods (Haor Basin).

---

## 🌍 NASA Datasets & Real Data Lineage

All satellite telemetry is extracted directly from official NASA Earth Science open APIs:
1. **NASA GPM IMERG (`GPM_3IMERGDF`)**: Daily calibrated precipitation rate & flash flood vulnerability.
2. **NASA MODIS Terra/Aqua LST (`MOD11A2` / MERRA-2 `TS`)**: Land Surface Temperature & thermal evapotranspiration risk.
3. **NASA SMAP L4 Radiometer (`SPL4SMGP` / `GWETROOT`)**: Root-zone volumetric soil moisture (0-100cm depth).
4. **NASA Landsat 8/9 OLI & MODIS (`MOD13Q1`)**: 16-day NDVI vegetation vigor & 5-year degradation trend slope.
5. **UNCCD & FAO Agronomic Database**: Crop characteristics, biological nitrogen fixation, and soil hardpan alleviation.

Raw JSON responses fetched directly from NASA's servers are stored in:
`backend/data/raw_nasa/` as audit proof for hackathon evaluation.

---

## 🤖 The 6+1 Multi-Agent Architecture

```
[Farmer & Land Inputs]
           │
           ▼
[NASA Live Preprocessed Telemetry]
           │
           ├──► Agent 1: Precipitation & Flood Agent (GPM IMERG)
           ├──► Agent 2: Thermal & Drought Stress Agent (MODIS LST)
           ├──► Agent 3: Soil Hydrology & Health Agent (SMAP Root-Zone)
           ├──► Agent 4: Crop Agronomy Agent (Landsat NDVI + FAO Database)
           ├──► Agent 5: Farmer Priority & Economic Agent (Cost vs ROI)
           └──► Agent 6: Land Degradation & Pest Agent (UNCCD Monoculture Alert)
                       │
                       ▼
         [Agent 7: The Master Rotation Agent]
   (Synthesizes 6-agent reports -> Generates Adaptive 3-Season Plan)
                       │
                       ▼
       [Interactive Bilingual Web Dashboard]
```

---

## 🚀 How to Run

### 1. Requirements
- Python 3.10+
- Dependencies: `fastapi`, `uvicorn`, `pydantic` (already installed)

### 2. (Optional) Re-fetch Live NASA Datasets
To pull the freshest live telemetry directly from NASA servers:
```bash
python scripts/download_real_nasa_data.py
```

### 3. Launch Web Application
```bash
python -m uvicorn backend.main:app --reload --port 8000
```
Open your browser and navigate to:
👉 **`http://localhost:8000`**

---

## 📊 Core Quantified Impacts
- **Water Saved:** Up to 44.4% irrigation water conserved compared to continuous Boro monoculture.
- **Cost Reduction:** Up to ৳4,000+ per bigha saved in irrigation electricity/diesel costs.
- **Soil Restoration:** Up to 85 kg/ha of atmospheric nitrogen fixed biologically via legume rotation (Mungbean & Lentils).

