"""
Agent 3: Soil Hydrology & Health Agent (মাটির স্বাস্থ্য ও আর্দ্রতা বিশ্লেষক)
Data Sources:
- NASA SMAP L4 Global Root Zone Soil Moisture (SPL4SMGP)
- Local Barind Multipurpose Development Authority (BMDA) groundwater records
"""

from typing import Dict, Any
from .base_agent import BaseAgent

class SoilAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="soil_agent",
            name_en="Soil Hydrology & Health Agent",
            name_bn="মাটির স্বাস্থ্য ও আর্দ্রতা বিশ্লেষক",
            data_sources=["NASA SMAP L4 Radiometer (SPL4SMGP)", "BMDA Barind Groundwater Index"]
        )

    def evaluate(self, env_data: Dict[str, Any], farmer_input: Dict[str, Any]) -> Dict[str, Any]:
        smap = env_data.get("nasa_smap_hydrology", {})
        root_moisture = smap.get("root_zone_moisture_m3_m3", 0.22)
        stress_pct = smap.get("stress_percentage", 20.0)
        moisture_status = smap.get("status", "MODERATE_STRESS")

        reg_meta = env_data.get("region_metadata", {})
        gw_status = reg_meta.get("groundwater_status", {})
        gw_stress = gw_status.get("stress_level", "Moderate")
        cost_share = gw_status.get("historical_irrigation_cost_share", "15-20%")

        if moisture_status == "CRITICAL_DEFICIT" or gw_stress == "Critical":
            health_status = "CRITICAL_WATER_DEPLETION"
            warning_bn = f"শিকড়ের গভীরতায় (Root-zone) পানির মারাত্মক ঘাটতি! বরেন্দ্র এলাকায় সেচ ব্যয় মোট উৎপাদন খরচের {cost_share}-এ পৌঁছেছে। ভূগর্ভস্থ পানি তোলা অব্যাহত রাখলে আগামী মৌসুমে পাম্প ফেইল করতে পারে।"
            rec_bn = "বোরো ধানের মতো অতিরিক্ত পানিটানা ফসল বাদ দিয়ে ১০০% কম পানির লেগিউম (মসুর/মুগ) বা সরিষা লাগাতে হবে, যাতে ভূগর্ভস্থ পানি রিচার্জের সুযোগ পায়।"
        elif root_moisture > 0.40:
            health_status = "WATERLOGGED"
            warning_bn = "মাটিতে অতিরিক্ত পানি জমে আছে এবং বায়ু চলাচলে ব্যাঘাত ঘটছে।"
            rec_bn = "পানি নিষ্কাশন ব্যবস্থার উন্নয়ন করুন এবং আর্দ্রতা-সহনশীল ফসল নির্বাচন করুন।"
        else:
            health_status = "STABLE"
            warning_bn = "মাটির আর্দ্রতা সন্তোষজনক মাত্রায় রয়েছে।"
            rec_bn = "মাটির জৈব পদার্থ বজায় রাখতে ফসলের অবশিষ্টাংশ মাটিতে মিশিয়ে দিন।"

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name_en,
            "agent_name_bn": self.name_bn,
            "satellite_instrument": "NASA SMAP L-band Radar/Radiometer (9km Grid)",
            "metrics": {
                "root_zone_moisture_m3_m3": root_moisture,
                "moisture_stress_percentage": stress_pct,
                "groundwater_vulnerability": gw_stress,
                "irrigation_cost_share_stat": cost_share
            },
            "status": health_status,
            "observations_bn": f"নাসার SMAP স্যাটেলাইটে মাটির শিকড় স্তরের আর্দ্রতা {root_moisture} m³/m³ পাওয়া গেছে (ঘাটতি: {stress_pct}%)। ভূগর্ভস্থ পানির চাপ: {gw_stress}।",
            "warning_bn": warning_bn,
            "recommendation_bn": rec_bn,
            "water_conservation_priority": health_status == "CRITICAL_WATER_DEPLETION"
        }

