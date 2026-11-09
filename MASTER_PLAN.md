# 🚀 AGROSHIFT NEXUS (KRISHI BONDHU AI)
> **NASA International Space Apps Challenge 2026**  
> **Challenge Track:** Field Shift: Adapting Farms with NASA Data  
> **Team:** Team Nokkhotro  

---

## 📌 Executive Summary
AgroShift Nexus (Krishi Bondhu AI) is an end-to-end **Autonomous Multi-Agent Decision-Support System** utilizing NASA Earth Observation data and a trained Machine Learning model to generate climate-adaptive, multi-season crop rotation strategies (Kharif-1 ➔ Kharif-2 ➔ Rabi) across all 64 districts and 8 administrative divisions of Bangladesh.

---

## 🛰️ NASA Earth Science Data Integration
1. **NASA GPM IMERG (`GPM_3IMERGDF_07`)**: Daily calibrated precipitation rate & extreme flood warnings.
2. **NASA MODIS Terra/Aqua LST (`MOD11A2` / MERRA-2 `TS`)**: Land Surface Temperature & thermal evapotranspiration.
3. **NASA SMAP L4 (`SPL4SMGP` / `GWETROOT`)**: Root-zone volumetric soil moisture (0-100cm depth).
4. **NASA Landsat-8/9 OLI & MODIS (`MOD13Q1`)**: 16-day NDVI vegetation vigor & 5-year degradation trend slope.

Raw JSON audit responses downloaded directly from `power.larc.nasa.gov` are saved in `backend/data/raw_nasa/` as verifiable proof for judges.

---

## 🤖 The 6+1 Multi-Agent Architecture
1. **Agent 1: Precipitation & Flood Agent** (NASA GPM IMERG)
2. **Agent 2: Thermal & Drought Stress Agent** (NASA MODIS LST)
3. **Agent 3: Soil Hydrology & Health Agent** (NASA SMAP L4)
4. **Agent 4: Crop Agronomy Agent (ML Enhanced)** (Landsat NDVI + Random Forest Model)
5. **Agent 5: Farmer Priority & Economic Agent** (Local market prices & irrigation tariffs)
6. **Agent 6: Land Degradation & Pest Agent** (UNCCD framework & monoculture penalty)
7. **Agent 7: Master Rotation Agent (The Brain)** (Consensus synthesis & 3-season crop sequence)

---

## 🧠 Machine Learning Engine
- **Model:** Random Forest Classifier (Scikit-Learn, 150 Decision Trees)
- **Dataset Scale:** 20,000 national-scale records across all 64 districts over 25 years (`backend/data/nasa_crop_training_dataset.csv`)
- **Test Accuracy:** **97.3%**
- **Artifact:** `backend/models/crop_risk_model.joblib`

---

## 📊 Quantified Impact
- **Water Saved:** Up to 44.4% irrigation water conserved compared to continuous Boro monoculture.
- **Irrigation Cost Reduced:** Up to ৳4,000+ per bigha saved in electricity/diesel pumping costs.
- **Biological Nitrogen Fixed:** Up to 85 kg/ha of natural nitrogen added via legumes.
