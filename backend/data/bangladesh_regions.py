"""
Bangladesh 64 Districts & Agro-Ecological Zones (AEZ) Database.
Covers all 8 administrative divisions and 30 Agro-Ecological Zones:
1. Rajshahi Division (8 districts - High Barind Tract, Drought & Groundwater crisis)
2. Rangpur Division (8 districts - Tista Floodplain, Drought & Sandy Loam)
3. Sylhet Division (4 districts - Haor Basin, Extreme Flash Floods)
4. Khulna Division (10 districts - Coastal Saline Belt, Cyclone Surges)
5. Barishal Division (6 districts - Lower Meghna Estuary & Tidal Saline)
6. Dhaka Division (13 districts - Central Floodplains, Intensive cropping)
7. Mymensingh Division (4 districts - Old Brahmaputra & Northern Haor edge)
8. Chattogram Division (11 districts - Coastal, River Basins & Chittagong Hill Tracts)
"""

from typing import Dict, Any, List

DISTRICTS: Dict[str, Dict[str, Any]] = {
    # ================= RAJSHAHI DIVISION (Barind Tract & Drought) =================
    "rajshahi": {
        "id": "rajshahi", "name_en": "Rajshahi", "name_bn": "রাজশাহী", "division": "Rajshahi", "division_bn": "রাজশাহী",
        "lat": 24.3745, "lon": 88.6042, "aez": "AEZ-25: High Barind Tract", "zone_type": "BARIND_DROUGHT",
        "soil_type": "Tight silty clay with low organic matter (<1.0%), compacted hardpan at 15cm",
        "groundwater_stress": "Critical (Depletion: 0.75m/yr)", "historical_irrigation_cost_share": "37.5%",
        "primary_risk": "Severe Groundwater Depletion & Heatwave", "default_past_crop": "boro_rice"
    },
    "chapainawabganj": {
        "id": "chapainawabganj", "name_en": "Chapainawabganj", "name_bn": "চাঁপাইনবাবগঞ্জ", "division": "Rajshahi", "division_bn": "রাজশাহী",
        "lat": 24.5965, "lon": 88.2775, "aez": "AEZ-25: High Barind Tract", "zone_type": "BARIND_DROUGHT",
        "soil_type": "Clayey Barind soil, severe moisture deficiency in winter",
        "groundwater_stress": "Critical", "historical_irrigation_cost_share": "38.2%",
        "primary_risk": "Drought & Extreme Summer Heat (>42°C)", "default_past_crop": "boro_rice"
    },
    "naogaon": {
        "id": "naogaon", "name_en": "Naogaon", "name_bn": "নওগাঁ", "division": "Rajshahi", "division_bn": "রাজশাহী",
        "lat": 24.7936, "lon": 88.9318, "aez": "AEZ-26: High Barind / Level Barind", "zone_type": "BARIND_DROUGHT",
        "soil_type": "Silty clay to clay, low infiltration",
        "groundwater_stress": "Critical", "historical_irrigation_cost_share": "36.0%",
        "primary_risk": "Excessive groundwater extraction for Boro monoculture", "default_past_crop": "boro_rice"
    },
    "bogra": {
        "id": "bogra", "name_en": "Bogura", "name_bn": "বগুড়া", "division": "Rajshahi", "division_bn": "রাজশাহী",
        "lat": 24.8465, "lon": 89.3777, "aez": "AEZ-4: Karatoya-Bangali Floodplain", "zone_type": "INTENSIVE_AGRICULTURE",
        "soil_type": "Fertile silt loam, intensive triple-cropping",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "28.5%",
        "primary_risk": "Soil nutrient depletion due to intensive monoculture", "default_past_crop": "potato"
    },
    "pabna": {
        "id": "pabna", "name_en": "Pabna", "name_bn": "পাবনা", "division": "Rajshahi", "division_bn": "রাজশাহী",
        "lat": 24.0064, "lon": 89.2372, "aez": "AEZ-11: High Ganges River Floodplain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Calcareous silt loam, good moisture capacity",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "22.0%",
        "primary_risk": "Dry spell during Rabi season", "default_past_crop": "boro_rice"
    },
    "sirajganj": {
        "id": "sirajganj", "name_en": "Sirajganj", "name_bn": "সিরাজগঞ্জ", "division": "Rajshahi", "division_bn": "রাজশাহী",
        "lat": 24.4534, "lon": 89.7008, "aez": "AEZ-7: Active Jamuna Floodplain", "zone_type": "CHAR_FLOODPLAIN",
        "soil_type": "Sandy silt, char land prone to sand deposition",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "16.5%",
        "primary_risk": "Jamuna riverbank erosion & seasonal flooding", "default_past_crop": "mustard"
    },
    "natore": {
        "id": "natore", "name_en": "Natore", "name_bn": "নাটোর", "division": "Rajshahi", "division_bn": "রাজশাহী",
        "lat": 24.4206, "lon": 88.9324, "aez": "AEZ-5: Lower Atrai Basin (Chalan Beel)", "zone_type": "BEEL_WETLAND",
        "soil_type": "Heavy basin clay, prolonged seasonal waterlogging",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "20.0%",
        "primary_risk": "Chalan beel drainage congestion & post-monsoon waterlogging", "default_past_crop": "boro_rice"
    },
    "joypurhat": {
        "id": "joypurhat", "name_en": "Joypurhat", "name_bn": "জয়পুরহাট", "division": "Rajshahi", "division_bn": "রাজশাহী",
        "lat": 25.1015, "lon": 89.0277, "aez": "AEZ-25: Level Barind Tract", "zone_type": "BARIND_DROUGHT",
        "soil_type": "Grey terrace soil, low permeability",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "31.0%",
        "primary_risk": "Soil compaction & early summer dry spell", "default_past_crop": "potato"
    },

    # ================= RANGPUR DIVISION (Northern Drought & Chars) =================
    "rangpur": {
        "id": "rangpur", "name_en": "Rangpur", "name_bn": "রংপুর", "division": "Rangpur", "division_bn": "রংপুর",
        "lat": 25.7439, "lon": 89.2752, "aez": "AEZ-3: Tista Meander Floodplain", "zone_type": "SANDY_DROUGHT",
        "soil_type": "Sandy loam, low moisture retention, organic matter ~1.2%",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "24.5%",
        "primary_risk": "Monga/Drought vulnerability, rapid surface dry-out", "default_past_crop": "potato"
    },
    "dinajpur": {
        "id": "dinajpur", "name_en": "Dinajpur", "name_bn": "দিনাজপুর", "division": "Rangpur", "division_bn": "রংপুর",
        "lat": 25.6217, "lon": 88.6355, "aez": "AEZ-1: Old Himalayan Piedmont Plain", "zone_type": "SANDY_DROUGHT",
        "soil_type": "Coarse sandy loam, very acidic (pH 4.8 - 5.5)",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "27.0%",
        "primary_risk": "Soil acidity & seasonal agricultural drought", "default_past_crop": "boro_rice"
    },
    "kurigram": {
        "id": "kurigram", "name_en": "Kurigram", "name_bn": "কুড়িগ্রাম", "division": "Rangpur", "division_bn": "রংপুর",
        "lat": 25.8054, "lon": 89.6362, "aez": "AEZ-2: Active Tista Floodplain & Chars", "zone_type": "CHAR_FLOODPLAIN",
        "soil_type": "Loose sand and silt, poor nutrient retention",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "15.0%",
        "primary_risk": "Severe river erosion, seasonal floods & char land poverty", "default_past_crop": "groundnut"
    },
    "gaibandha": {
        "id": "gaibandha", "name_en": "Gaibandha", "name_bn": "গাইবান্ধা", "division": "Rangpur", "division_bn": "রংপুর",
        "lat": 25.3288, "lon": 89.5408, "aez": "AEZ-2: Active Tista & Brahmaputra Chars", "zone_type": "CHAR_FLOODPLAIN",
        "soil_type": "Alluvial silt and sand",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "17.0%",
        "primary_risk": "Floods during monsoon, dry sandstorms in pre-monsoon", "default_past_crop": "mustard"
    },
    "nilphamari": {
        "id": "nilphamari", "name_en": "Nilphamari", "name_bn": "নীলফামারী", "division": "Rangpur", "division_bn": "রংপুর",
        "lat": 25.9318, "lon": 88.8560, "aez": "AEZ-3: Tista Meander Floodplain", "zone_type": "SANDY_DROUGHT",
        "soil_type": "Sandy loam, low fertility",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "21.0%",
        "primary_risk": "Low rainfall in winter, high irrigation dependency", "default_past_crop": "boro_rice"
    },
    "thakurgaon": {
        "id": "thakurgaon", "name_en": "Thakurgaon", "name_bn": "ঠাকুরগাঁও", "division": "Rangpur", "division_bn": "রংপুর",
        "lat": 26.0337, "lon": 88.4617, "aez": "AEZ-1: Old Himalayan Piedmont Plain", "zone_type": "SANDY_DROUGHT",
        "soil_type": "Acidic sandy loam, rich in stone/pebble substrata",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "26.5%",
        "primary_risk": "Subsurface stony layer prevents deep root penetration", "default_past_crop": "wheat"
    },
    "panchagarh": {
        "id": "panchagarh", "name_en": "Panchagarh", "name_bn": "পঞ্চগড়", "division": "Rangpur", "division_bn": "রংপুর",
        "lat": 26.3411, "lon": 88.5542, "aez": "AEZ-1: Old Himalayan Piedmont Plain", "zone_type": "SANDY_DROUGHT",
        "soil_type": "Light sandy loam, ideal for tea and pulses",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "23.0%",
        "primary_risk": "Extreme winter cold spells (fog-burn on crops)", "default_past_crop": "mustard"
    },
    "lalmonirhat": {
        "id": "lalmonirhat", "name_en": "Lalmonirhat", "name_bn": "লালমনিরহাট", "division": "Rangpur", "division_bn": "রংপুর",
        "lat": 25.9923, "lon": 89.2847, "aez": "AEZ-2: Tista Alluvial Belt", "zone_type": "CHAR_FLOODPLAIN",
        "soil_type": "Sandy char soil, low nitrogen",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "16.0%",
        "primary_risk": "Tista barrage upstream water withdrawal & flash deluge", "default_past_crop": "maize"
    },

    # ================= SYLHET DIVISION (Haor Basin & Flash Floods) =================
    "sylhet": {
        "id": "sylhet", "name_en": "Sylhet", "name_bn": "সিলেট", "division": "Sylhet", "division_bn": "সিলেট",
        "lat": 24.8949, "lon": 91.8687, "aez": "AEZ-20: Eastern Surma-Kushiyara Floodplain", "zone_type": "HAOR_FLASH_FLOOD",
        "soil_type": "Silty clay to heavy basin clay, rich in silt deposit",
        "groundwater_stress": "Safe", "historical_irrigation_cost_share": "9.5%",
        "primary_risk": "Extreme rainfall (>4,000 mm/yr) & early flash floods in April", "default_past_crop": "boro_rice"
    },
    "sunamganj": {
        "id": "sunamganj", "name_en": "Sunamganj", "name_bn": "সুনামগঞ্জ", "division": "Sylhet", "division_bn": "সিলেট",
        "lat": 25.0658, "lon": 91.4073, "aez": "AEZ-21: Sylhet Basin / Core Haor", "zone_type": "HAOR_FLASH_FLOOD",
        "soil_type": "Heavy basin clay, submerged under 3-6 meters water for 6 months",
        "groundwater_stress": "Safe", "historical_irrigation_cost_share": "8.0%",
        "primary_risk": "Devastating Meghalaya upstream flash floods drowning mature Boro rice", "default_past_crop": "boro_rice"
    },
    "moulvibazar": {
        "id": "moulvibazar", "name_en": "Moulvibazar", "name_bn": "মৌলভীবাজার", "division": "Sylhet", "division_bn": "সিলেট",
        "lat": 24.4829, "lon": 91.7774, "aez": "AEZ-22: Northern & Eastern Piedmont Plains", "zone_type": "HAOR_HILL_MIX",
        "soil_type": "Acidic loam to heavy clay in haor fringes",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "11.0%",
        "primary_risk": "Hakaluki haor flash floods & soil acidity", "default_past_crop": "boro_rice"
    },
    "habiganj": {
        "id": "habiganj", "name_en": "Habiganj", "name_bn": "হবিগঞ্জ", "division": "Sylhet", "division_bn": "সিলেট",
        "lat": 24.3749, "lon": 91.4155, "aez": "AEZ-21: Sylhet Basin (Southern Haor)", "zone_type": "HAOR_FLASH_FLOOD",
        "soil_type": "Heavy grey basin clay",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "10.0%",
        "primary_risk": "Early inundation from Khowai river flash floods", "default_past_crop": "boro_rice"
    },

    # ================= KHULNA DIVISION (Coastal Salinity & Cyclones) =================
    "khulna": {
        "id": "khulna", "name_en": "Khulna", "name_bn": "খুলনা", "division": "Khulna", "division_bn": "খুলনা",
        "lat": 22.8456, "lon": 89.5403, "aez": "AEZ-13: Ganges Tidal Floodplain", "zone_type": "COASTAL_SALINE",
        "soil_type": "Saline silty clay, electrical conductivity (EC) rises to 8-16 dS/m in winter",
        "groundwater_stress": "Critical (Saline Aquifer)", "historical_irrigation_cost_share": "26.0%",
        "primary_risk": "Soil & surface water salinity during Rabi season", "default_past_crop": "saline_rice_brri67"
    },
    "satkhira": {
        "id": "satkhira", "name_en": "Satkhira", "name_bn": "সাতক্ষীরা", "division": "Khulna", "division_bn": "খুলনা",
        "lat": 22.7185, "lon": 89.0705, "aez": "AEZ-13: Ganges Tidal Saline Plain", "zone_type": "COASTAL_SALINE",
        "soil_type": "Heavy coastal clay, high chloride & sodium salinity",
        "groundwater_stress": "Critical (Shallow saline barrier)", "historical_irrigation_cost_share": "28.5%",
        "primary_risk": "Severe salinity barrier in Rabi & Cyclone tidal surges", "default_past_crop": "sunflower"
    },
    "bagerhat": {
        "id": "bagerhat", "name_en": "Bagerhat", "name_bn": "বাগেরহাট", "division": "Khulna", "division_bn": "খুলনা",
        "lat": 22.6516, "lon": 89.7859, "aez": "AEZ-13: Ganges Tidal Floodplain", "zone_type": "COASTAL_SALINE",
        "soil_type": "Saline clay loam, brackish shrimp polder boundaries",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "24.0%",
        "primary_risk": "Saline water intrusion & cyclone damage", "default_past_crop": "saline_rice_brri67"
    },
    "jessore": {
        "id": "jessore", "name_en": "Jashore", "name_bn": "যশোর", "division": "Khulna", "division_bn": "খুলনা",
        "lat": 23.1664, "lon": 89.2182, "aez": "AEZ-11: High Ganges River Floodplain", "zone_type": "INTENSIVE_AGRICULTURE",
        "soil_type": "Calcareous dark grey floodplain soil, very fertile",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "22.5%",
        "primary_risk": "Dry season water scarcity & waterlogging in Bhabodah", "default_past_crop": "mustard"
    },
    "kushtia": {
        "id": "kushtia", "name_en": "Kushtia", "name_bn": "কুষ্টিয়া", "division": "Khulna", "division_bn": "খুলনা",
        "lat": 23.9013, "lon": 89.1204, "aez": "AEZ-11: High Ganges Floodplain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Calcareous loam to silt loam, high cation exchange capacity",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "25.0%",
        "primary_risk": "Gorai river flow depletion & drought", "default_past_crop": "wheat"
    },
    "chuadanga": {
        "id": "chuadanga", "name_en": "Chuadanga", "name_bn": "চুয়াডাঙ্গা", "division": "Khulna", "division_bn": "খুলনা",
        "lat": 23.6402, "lon": 88.8418, "aez": "AEZ-11: High Ganges Plain", "zone_type": "BARIND_DROUGHT",
        "soil_type": "Calcareous dark loam",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "30.0%",
        "primary_risk": "Highest recorded summer temperatures in BD (>43°C)", "default_past_crop": "maize"
    },
    "jhenaidah": {
        "id": "jhenaidah", "name_en": "Jhenaidah", "name_bn": "ঝিনাইদহ", "division": "Khulna", "division_bn": "খুলনা",
        "lat": 23.5450, "lon": 89.1726, "aez": "AEZ-11: High Ganges Plain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Silty clay loam",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "22.0%",
        "primary_risk": "Dry spell during flowering stages of crops", "default_past_crop": "mustard"
    },
    "magura": {
        "id": "magura", "name_en": "Magura", "name_bn": "মাগুরা", "division": "Khulna", "division_bn": "খুলনা",
        "lat": 23.4873, "lon": 89.4199, "aez": "AEZ-12: Low Ganges Floodplain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Fertile silt loam, good pulse producing area",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "19.0%",
        "primary_risk": "Early monsoon water stagnation", "default_past_crop": "lentil"
    },
    "meherpur": {
        "id": "meherpur", "name_en": "Meherpur", "name_bn": "মেহেরপুর", "division": "Khulna", "division_bn": "খুলনা",
        "lat": 23.7746, "lon": 88.6318, "aez": "AEZ-11: High Ganges Plain", "zone_type": "BARIND_DROUGHT",
        "soil_type": "Calcareous loam",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "29.0%",
        "primary_risk": "Intense heatwave & low winter rainfall", "default_past_crop": "maize"
    },
    "narail": {
        "id": "narail", "name_en": "Narail", "name_bn": "নড়াইল", "division": "Khulna", "division_bn": "খুলনা",
        "lat": 23.1725, "lon": 89.5127, "aez": "AEZ-12: Low Ganges Plain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Heavy clay to silty clay loam",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "18.0%",
        "primary_risk": "Drainage congestion in Chitra river basin", "default_past_crop": "boro_rice"
    },

    # ================= BARISHAL DIVISION (Coastal Tidal & Saline Delta) =================
    "barisal": {
        "id": "barisal", "name_en": "Barishal", "name_bn": "বরিশাল", "division": "Barishal", "division_bn": "বরিশাল",
        "lat": 22.7010, "lon": 90.3535, "aez": "AEZ-13: Ganges Tidal Floodplain (Non-Saline to Mild)", "zone_type": "TIDAL_DELTA",
        "soil_type": "Clayey silt, tidal flushing, rich in alluvium",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "12.0%",
        "primary_risk": "Tidal surges and seasonal cyclone floods", "default_past_crop": "aman_rice_short"
    },
    "patuakhali": {
        "id": "patuakhali", "name_en": "Patuakhali", "name_bn": "পটুয়াখালী", "division": "Barishal", "division_bn": "বরিশাল",
        "lat": 22.3596, "lon": 90.3299, "aez": "AEZ-13: Ganges Tidal Saline Delta", "zone_type": "COASTAL_SALINE",
        "soil_type": "Heavy saline clay, high winter salinity",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "21.0%",
        "primary_risk": "Lack of freshwater irrigation during Rabi & sea surge", "default_past_crop": "sunflower"
    },
    "bhola": {
        "id": "bhola", "name_en": "Bhola", "name_bn": "ভোলা", "division": "Barishal", "division_bn": "বরিশাল",
        "lat": 22.6859, "lon": 90.6481, "aez": "AEZ-18: Young Meghna Estuarine Floodplain", "zone_type": "COASTAL_SALINE",
        "soil_type": "Silty alluvium, mild to moderate coastal salinity",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "17.0%",
        "primary_risk": "Meghna river island erosion & tidal inundation", "default_past_crop": "soybean"
    },
    "barguna": {
        "id": "barguna", "name_en": "Barguna", "name_bn": "বরগুনা", "division": "Barishal", "division_bn": "বরিশাল",
        "lat": 22.1570, "lon": 90.1265, "aez": "AEZ-13: Ganges Tidal Saline Belt", "zone_type": "COASTAL_SALINE",
        "soil_type": "Saline clay",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "24.0%",
        "primary_risk": "High salinity (EC 10-14 dS/m) and storm surges", "default_past_crop": "sunflower"
    },
    "pirojpur": {
        "id": "pirojpur", "name_en": "Pirojpur", "name_bn": "পিরোজপুর", "division": "Barishal", "division_bn": "বরিশাল",
        "lat": 22.5841, "lon": 89.9720, "aez": "AEZ-13: Ganges Tidal Plain", "zone_type": "TIDAL_DELTA",
        "soil_type": "Silty clay loam, peat basin pockets",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "14.0%",
        "primary_risk": "Tidal overflow & peat soil subsidence", "default_past_crop": "mungbean"
    },
    "jhalokati": {
        "id": "jhalokati", "name_en": "Jhalokati", "name_bn": "ঝালকাঠি", "division": "Barishal", "division_bn": "বরিশাল",
        "lat": 22.6406, "lon": 90.1987, "aez": "AEZ-13: Ganges Tidal Plain", "zone_type": "TIDAL_DELTA",
        "soil_type": "Silt loam to clay loam, guava & betel nut belt",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "13.0%",
        "primary_risk": "Monsoon high tides & waterlogging", "default_past_crop": "aman_rice_short"
    },

    # ================= DHAKA DIVISION (Central Floodplains) =================
    "dhaka": {
        "id": "dhaka", "name_en": "Dhaka", "name_bn": "ঢাকা", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 23.8103, "lon": 90.4125, "aez": "AEZ-28: Madhupur Tract / Old Brahmaputra", "zone_type": "INTENSIVE_AGRICULTURE",
        "soil_type": "Red terrace clay on upland, silt loam in valleys",
        "groundwater_stress": "Critical (Industrial & Urban Over-pumping)", "historical_irrigation_cost_share": "30.0%",
        "primary_risk": "Urban encroachment & industrial wastewater runoff", "default_past_crop": "vegetables"
    },
    "gazipur": {
        "id": "gazipur", "name_en": "Gazipur", "name_bn": "গাজীপুর", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 24.0023, "lon": 90.4264, "aez": "AEZ-28: Madhupur Tract", "zone_type": "TERRACE_UPLAND",
        "soil_type": "Red acidic clay (pH 5.0 - 5.5), high iron/aluminum",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "27.0%",
        "primary_risk": "Severe subsoil acidity and industrial water drawdown", "default_past_crop": "mustard"
    },
    "tangail": {
        "id": "tangail", "name_en": "Tangail", "name_bn": "টাঙ্গাইল", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 24.2513, "lon": 89.9167, "aez": "AEZ-8: Young Brahmaputra Floodplain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Sandy loam to silt loam, very suitable for mustard & jute",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "20.0%",
        "primary_risk": "Jamuna river overflow in monsoon", "default_past_crop": "mustard"
    },
    "faridpur": {
        "id": "faridpur", "name_en": "Faridpur", "name_bn": "ফরিদপুর", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 23.6071, "lon": 89.8429, "aez": "AEZ-12: Low Ganges River Floodplain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Deep silt loam, top jute producing district",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "19.5%",
        "primary_risk": "Padma river bank erosion & siltation", "default_past_crop": "jute"
    },
    "gopalganj": {
        "id": "gopalganj", "name_en": "Gopalganj", "name_bn": "গোপালগঞ্জ", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 23.0051, "lon": 89.8266, "aez": "AEZ-14: Gopalganj-Khulna Beels", "zone_type": "BEEL_WETLAND",
        "soil_type": "Heavy organic peat soil and deep mucky clay",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "15.0%",
        "primary_risk": "Waterlogging for 7-8 months; floating agriculture zone", "default_past_crop": "boro_rice"
    },
    "manikganj": {
        "id": "manikganj", "name_en": "Manikganj", "name_bn": "মানিকগঞ্জ", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 23.8644, "lon": 90.0047, "aez": "AEZ-8: Young Brahmaputra Floodplain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Silt loam",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "20.5%",
        "primary_risk": "Dhaleshwari river seasonal flooding", "default_past_crop": "mustard"
    },
    "munshiganj": {
        "id": "munshiganj", "name_en": "Munshiganj", "name_bn": "মুন্সিগঞ্জ", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 23.5422, "lon": 90.5305, "aez": "AEZ-19: Old Meghna Estuarine Floodplain", "zone_type": "INTENSIVE_AGRICULTURE",
        "soil_type": "Deep silt loam, highest potato productivity in BD",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "22.0%",
        "primary_risk": "Excessive chemical fertilizer residues & potato blight", "default_past_crop": "potato"
    },
    "narayanganj": {
        "id": "narayanganj", "name_en": "Narayanganj", "name_bn": "নারায়ণগঞ্জ", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 23.6238, "lon": 90.5000, "aez": "AEZ-19: Old Meghna Floodplain", "zone_type": "INTENSIVE_AGRICULTURE",
        "soil_type": "Silt loam",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "26.0%",
        "primary_risk": "Industrial pollution & water table drop", "default_past_crop": "vegetables"
    },
    "narsingdi": {
        "id": "narsingdi", "name_en": "Narsingdi", "name_bn": "নরসিংদী", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 23.9322, "lon": 90.7154, "aez": "AEZ-9: Old Brahmaputra Floodplain", "zone_type": "INTENSIVE_AGRICULTURE",
        "soil_type": "Silt loam to loam, major vegetable & banana hub",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "21.0%",
        "primary_risk": "Pest recurrence from intensive monoculture", "default_past_crop": "mustard"
    },
    "kishoreganj": {
        "id": "kishoreganj", "name_en": "Kishoreganj", "name_bn": "কিশোরগঞ্জ", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 24.4449, "lon": 90.7766, "aez": "AEZ-21: Sylhet Basin / Western Haor", "zone_type": "HAOR_FLASH_FLOOD",
        "soil_type": "Heavy basin clay in eastern upazilas (Nikli, Itna, Mithamain)",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "11.0%",
        "primary_risk": "Nikli/Itna haor early submergence of Boro rice", "default_past_crop": "boro_rice"
    },
    "madaripur": {
        "id": "madaripur", "name_en": "Madaripur", "name_bn": "মাদারীপুর", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 23.1641, "lon": 90.1897, "aez": "AEZ-12: Low Ganges Floodplain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Silty clay loam",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "18.0%",
        "primary_risk": "River erosion along Arial Khan river", "default_past_crop": "jute"
    },
    "shariatpur": {
        "id": "shariatpur", "name_en": "Shariatpur", "name_bn": "শরীয়তপুর", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 23.2423, "lon": 90.4348, "aez": "AEZ-12: Low Ganges Plain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Silt alluvium",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "16.0%",
        "primary_risk": "Severe Padma river erosion", "default_past_crop": "mustard"
    },
    "rajbari": {
        "id": "rajbari", "name_en": "Rajbari", "name_bn": "রাজবাড়ী", "division": "Dhaka", "division_bn": "ঢাকা",
        "lat": 23.7574, "lon": 89.6445, "aez": "AEZ-11: High Ganges Floodplain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Calcareous loam",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "21.5%",
        "primary_risk": "Dry season moisture deficit", "default_past_crop": "onion"
    },

    # ================= MYMENSINGH DIVISION (Northern Piedmont & Haors) =================
    "mymensingh": {
        "id": "mymensingh", "name_en": "Mymensingh", "name_bn": "ময়মনসিংহ", "division": "Mymensingh", "division_bn": "ময়মনসিংহ",
        "lat": 24.7471, "lon": 90.4203, "aez": "AEZ-9: Old Brahmaputra Floodplain", "zone_type": "INTENSIVE_AGRICULTURE",
        "soil_type": "Fertile silt loam to silty clay loam",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "22.0%",
        "primary_risk": "Intensive double-rice cycle exhausting soil organic matter", "default_past_crop": "boro_rice"
    },
    "netrokona": {
        "id": "netrokona", "name_en": "Netrokona", "name_bn": "নেত্রকোণা", "division": "Mymensingh", "division_bn": "ময়মনসিংহ",
        "lat": 24.8709, "lon": 90.7279, "aez": "AEZ-21: Sylhet Basin / Northern Haor", "zone_type": "HAOR_FLASH_FLOOD",
        "soil_type": "Heavy basin clay in haor areas (Khaliajuri, Mohanganj)",
        "groundwater_stress": "Low", "historical_irrigation_cost_share": "10.0%",
        "primary_risk": "Khaliajuri haor flash flood devastating standing Boro crops", "default_past_crop": "boro_rice"
    },
    "jamalpur": {
        "id": "jamalpur", "name_en": "Jamalpur", "name_bn": "জামালপুর", "division": "Mymensingh", "division_bn": "ময়মনসিংহ",
        "lat": 24.9375, "lon": 89.9378, "aez": "AEZ-8: Young Brahmaputra Floodplain & Chars", "zone_type": "CHAR_FLOODPLAIN",
        "soil_type": "Sandy loam, alluvial char deposits",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "19.0%",
        "primary_risk": "Brahmaputra overflow & sand deposition", "default_past_crop": "mustard"
    },
    "sherpur": {
        "id": "sherpur", "name_en": "Sherpur", "name_bn": "শেরপুর", "division": "Mymensingh", "division_bn": "ময়মনসিংহ",
        "lat": 25.0205, "lon": 90.0153, "aez": "AEZ-22: Northern & Eastern Piedmont Plains", "zone_type": "PIEDMONT_VALLEY",
        "soil_type": "Garo hills piedmont alluvium, sandy clay loam",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "20.0%",
        "primary_risk": "Garo hill flash runoff, wild elephant crop raids & drought", "default_past_crop": "aman_rice_short"
    },

    # ================= CHATTOGRAM DIVISION (Coast, Estuary & Hill Tracts) =================
    "chittagong": {
        "id": "chittagong", "name_en": "Chattogram", "name_bn": "চট্টগ্রাম", "division": "Chattogram", "division_bn": "চট্টগ্রাম",
        "lat": 22.3569, "lon": 91.7832, "aez": "AEZ-23: Chittagong Coastal Plain", "zone_type": "COASTAL_SALINE",
        "soil_type": "Silty clay to heavy clay, moderate salinity in coastal pockets",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "21.0%",
        "primary_risk": "Cyclone landfall, tidal saline surges & flash rain", "default_past_crop": "aman_rice_short"
    },
    "coxsbazar": {
        "id": "coxsbazar", "name_en": "Cox's Bazar", "name_bn": "কক্সবাজার", "division": "Chattogram", "division_bn": "চট্টগ্রাম",
        "lat": 21.4272, "lon": 92.0058, "aez": "AEZ-23: Chittagong Coastal Plain & Salt Pans", "zone_type": "COASTAL_SALINE",
        "soil_type": "Sandy coast to saline tidal clay",
        "groundwater_stress": "High (Saline infiltration)", "historical_irrigation_cost_share": "25.0%",
        "primary_risk": "High soil salinity from salt cultivation beds & cyclones", "default_past_crop": "saline_rice_brri67"
    },
    "comilla": {
        "id": "comilla", "name_en": "Cumilla", "name_bn": "কুমিল্লা", "division": "Chattogram", "division_bn": "চট্টগ্রাম",
        "lat": 23.4682, "lon": 91.1788, "aez": "AEZ-19: Old Meghna Estuarine Floodplain", "zone_type": "INTENSIVE_AGRICULTURE",
        "soil_type": "Fertile silt loam, intensive triple-cropping belt",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "28.0%",
        "primary_risk": "Gumti river embankment collapse & flash flooding", "default_past_crop": "boro_rice"
    },
    "brahmanbaria": {
        "id": "brahmanbaria", "name_en": "Brahmanbaria", "name_bn": "ব্রাহ্মণবাড়িয়া", "division": "Chattogram", "division_bn": "চট্টগ্রাম",
        "lat": 23.9571, "lon": 91.1119, "aez": "AEZ-19: Old Meghna Floodplain & Haor Fringes", "zone_type": "HAOR_FLASH_FLOOD",
        "soil_type": "Silty clay to basin clay",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "18.0%",
        "primary_risk": "Titas river flooding & early haor inundation", "default_past_crop": "boro_rice"
    },
    "chandpur": {
        "id": "chandpur", "name_en": "Chandpur", "name_bn": "চাঁদপুর", "division": "Chattogram", "division_bn": "চট্টগ্রাম",
        "lat": 23.2333, "lon": 90.6667, "aez": "AEZ-19: Old Meghna Estuarine Plain", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Fertile silt loam",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "19.0%",
        "primary_risk": "Meghna river confluence erosion & seasonal surges", "default_past_crop": "potato"
    },
    "noakhali": {
        "id": "noakhali", "name_en": "Noakhali", "name_bn": "নোয়াখালী", "division": "Chattogram", "division_bn": "চট্টগ্রাম",
        "lat": 22.8696, "lon": 91.0994, "aez": "AEZ-18: Young Meghna Estuarine Saline Plain", "zone_type": "COASTAL_SALINE",
        "soil_type": "Calcareous silty clay, salinity rises to 6-12 dS/m in winter",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "23.0%",
        "primary_risk": "Coastal land accretion/salinity; ideal for soybean/sunflower", "default_past_crop": "soybean"
    },
    "feni": {
        "id": "feni", "name_en": "Feni", "name_bn": "ফেনী", "division": "Chattogram", "division_bn": "চট্টগ্রাম",
        "lat": 23.0159, "lon": 91.3976, "aez": "AEZ-19: Old Meghna Plain & Coastal Fringes", "zone_type": "BALANCED_FLOODPLAIN",
        "soil_type": "Silty clay loam",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "20.0%",
        "primary_risk": "Muhuri river embankment breaches & flash flood", "default_past_crop": "aman_rice_short"
    },
    "lakshmipur": {
        "id": "lakshmipur", "name_en": "Lakshmipur", "name_bn": "লক্ষ্মীপুর", "division": "Chattogram", "division_bn": "চট্টগ্রাম",
        "lat": 22.9425, "lon": 90.8412, "aez": "AEZ-18: Young Meghna Estuary", "zone_type": "COASTAL_SALINE",
        "soil_type": "Silt alluvium, premier soybean district in Bangladesh",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "18.0%",
        "primary_risk": "Winter surface salinity & Meghna erosion", "default_past_crop": "soybean"
    },
    "rangamati": {
        "id": "rangamati", "name_en": "Rangamati", "name_bn": "রাঙ্গামাটি", "division": "Chattogram", "division_bn": "চট্টগ্রাম",
        "lat": 22.7324, "lon": 92.2985, "aez": "AEZ-29: Northern & Eastern Hills (CHT)", "zone_type": "HILL_TRACTS",
        "soil_type": "Brown hill soil, sandy clay loam, steep slope prone to erosion",
        "groundwater_stress": "High (Steep runoff)", "historical_irrigation_cost_share": "25.0%",
        "primary_risk": "Monsoon landslides, severe topsoil erosion & winter water scarcity", "default_past_crop": "ginger_turmeric"
    },
    "bandarban": {
        "id": "bandarban", "name_en": "Bandarban", "name_bn": "বান্দরবান", "division": "Chattogram", "division_bn": "চট্টগ্রাম",
        "lat": 22.1953, "lon": 92.2184, "aez": "AEZ-29: Chittagong Hill Tracts", "zone_type": "HILL_TRACTS",
        "soil_type": "Steep slope sandy clay loam, acidic",
        "groundwater_stress": "High", "historical_irrigation_cost_share": "27.0%",
        "primary_risk": "Water runoff in steep terrain; needs contour agroforestry", "default_past_crop": "ginger_turmeric"
    },
    "khagrachhari": {
        "id": "khagrachhari", "name_en": "Khagrachhari", "name_bn": "খাগড়াছড়ি", "division": "Chattogram", "division_bn": "চট্টগ্রাম",
        "lat": 23.1193, "lon": 91.9847, "aez": "AEZ-29: Northern & Eastern Hills", "zone_type": "HILL_TRACTS",
        "soil_type": "Valley alluvium and steep hill soil",
        "groundwater_stress": "Moderate", "historical_irrigation_cost_share": "22.0%",
        "primary_risk": "Flash floods in valley floors & slope erosion on hills", "default_past_crop": "maize"
    }
}

def get_all_districts() -> List[Dict[str, Any]]:
    return list(DISTRICTS.values())

def get_district_profile(district_id: str) -> Dict[str, Any]:
    return DISTRICTS.get(district_id.lower(), DISTRICTS["rajshahi"])

def get_districts_by_division(division_name: str) -> List[Dict[str, Any]]:
    return [d for d in DISTRICTS.values() if d["division"].lower() == division_name.lower()]
