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

### 1. Prerequisites
- Python 3.10 or higher
- Git

### 2. Set Up Virtual Environment

It is recommended to use an isolated Python virtual environment:

```bash
# Navigate to project root directory
cd Krishi-Bondhu-AI(models)

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment:
# On Linux / macOS:
source .venv/bin/activate
# On Windows (PowerShell):
# .venv\Scripts\Activate.ps1
# On Windows (cmd.exe):
# .venv\Scripts\activate.bat
```

> **Note for Debian/Ubuntu/Mint users:** If `python3 -m venv` reports missing `ensurepip`, install it via `sudo apt install python3-venv` or create with `python3 -m venv --without-pip .venv` followed by `curl -sS https://bootstrap.pypa.io/get-pip.py | python3`.

### 3. Install Dependencies

Install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

*(Packages include: `fastapi`, `uvicorn`, `pydantic`, `pandas`, `joblib`, `scikit-learn`)*

### 4. (Optional) Re-fetch Live NASA Datasets
To pull fresh live agro-climatic telemetry directly from NASA servers:
```bash
python scripts/download_real_nasa_data.py
```

### 5. Launch Web Application

Start the FastAPI and Uvicorn server:
```bash
python -m uvicorn backend.main:app --reload --port 8000
```

Once running, access the application in your browser:
- 🌐 **Interactive Dashboard:** [http://localhost:8000](http://localhost:8000)
- 📑 **API Documentation (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)

### 6. How to Stop the Application

- **In the active terminal:** Press `Ctrl + C` to stop the Uvicorn server.
- **Background / Detached process:** Run `pkill -f "uvicorn backend.main:app"`.
- **Exit virtual environment:** Run `deactivate`.

---

## 📊 Core Quantified Impacts
- **Water Saved:** Up to 44.4% irrigation water conserved compared to continuous Boro monoculture.
- **Cost Reduction:** Up to ৳4,000+ per bigha saved in irrigation electricity/diesel costs.
- **Soil Restoration:** Up to 85 kg/ha of atmospheric nitrogen fixed biologically via legume rotation (Mungbean & Lentils).

