"""
Agent 2: Thermal & Drought Stress Agent (তাপমাত্রা ও খরা বিশ্লেষক)
Data Sources:
- NASA MODIS Terra/Aqua Land Surface Temperature (MOD11A2)
- Local heatwave alerts and dry spell projections
"""

from typing import Dict, Any
from .base_agent import BaseAgent

class DroughtAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="drought_agent",
            name_en="Thermal & Drought Stress Agent",
            name_bn="তাপমাত্রা ও খরা বিশ্লেষক",
            data_sources=["NASA MODIS Terra/Aqua LST (MOD11A2)", "Evapotranspiration Index"]
        )

    def evaluate(self, env_data: Dict[str, Any], farmer_input: Dict[str, Any]) -> Dict[str, Any]:
        modis = env_data.get("nasa_modis_lst", {})
        lst_c = modis.get("calibrated_lst_celsius", 34.0)
        heat_index = modis.get("drought_heat_stress_index", 45)
        evapo_risk = modis.get("thermal_evapotranspiration_risk", "MODERATE")

        if lst_c > 39.0 or heat_index > 75:
            stress_level = "SEVERE"
            warning_bn = f"মাটির উপরিভাগের তাপমাত্রা মারাত্মক উচ্চ ({lst_c}°C)! অতিরিক্ত বাষ্পীভবনে জমি দ্রুত শুকিয়ে খরা সৃষ্টি করবে।"
            rec_bn = "উচ্চ পানির চাহিদাসম্পন্ন ফসল বাদ দিয়ে খরা-সহনশীল ও গভীর শিকড়ের ফসল (যেমন: সরিষা, তিল, মসুর ডাল) বেছে নিন।"
        elif lst_c > 35.0 or heat_index > 50:
            stress_level = "MODERATE"
            warning_bn = f"মাটির তাপমাত্রা মাঝারি উষ্ণ ({lst_c}°C)। গ্রীষ্ম ও প্রাক-বর্ষায় আর্দ্রতা ধরে রাখতে মালচিং বা কভার ক্রপ প্রয়োজন।"
            rec_bn = "মাঝারি তাপমাত্রাসহনশীল ফসল নির্বাচন করুন এবং সেচের ব্যবধান সঠিক রাখুন।"
        else:
            stress_level = "MILD"
            warning_bn = f"তাপমাত্রা ও বাষ্পীভবনের হার সহনশীল মাত্রায় রয়েছে ({lst_c}°C)।"
            rec_bn = "তাপমাত্রাজনিত কোনো সংকট নেই; সাধারণ মৌসুমি ফসল চাষ সম্ভব।"

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name_en,
            "agent_name_bn": self.name_bn,
            "satellite_instrument": "NASA MODIS Thermal Spectroradiometer (1km LST)",
            "metrics": {
                "land_surface_temp_c": lst_c,
                "drought_heat_stress_score": heat_index,
                "evapotranspiration_risk": evapo_risk
            },
            "status": stress_level,
            "observations_bn": f"নাসার MODIS LST সেন্সর অনুযায়ী ভূমির তাপমাত্রা {lst_c}°C রেকর্ড করা হয়েছে। বাষ্পীভবন চাপ: {evapo_risk}।",
            "warning_bn": warning_bn,
            "recommendation_bn": rec_bn,
            "drought_flag": stress_level == "SEVERE"
        }

