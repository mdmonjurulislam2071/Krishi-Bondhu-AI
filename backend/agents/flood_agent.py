"""
Agent 1: Precipitation & Flood Agent (বৃষ্টিপাত ও বন্যা বিশ্লেষক)
Data Sources:
- NASA GPM IMERG (Global Precipitation Measurement)
- BMD (Bangladesh Meteorological Department) local flash flood data
"""

from typing import Dict, Any
from .base_agent import BaseAgent

class FloodAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="flood_agent",
            name_en="Precipitation & Flood Agent",
            name_bn="বৃষ্টিপাত ও বন্যা বিশ্লেষক",
            data_sources=["NASA GPM IMERG (GPM_3IMERGDF)", "BMD River Water Level"]
        )

    def evaluate(self, env_data: Dict[str, Any], farmer_input: Dict[str, Any]) -> Dict[str, Any]:
        gpm = env_data.get("nasa_gpm_imerg", {})
        daily_rain = gpm.get("daily_precipitation_mm", 2.0)
        flood_index = gpm.get("flood_vulnerability_index", 20)
        extreme_rain = gpm.get("extreme_rain_warning", False)
        reg_meta = env_data.get("region_metadata", {})
        flash_flood_prob = reg_meta.get("flood_risk", {}).get("flash_flood_prob", 0.1)

        # Risk level determination
        if flood_index > 70 or flash_flood_prob > 0.70:
            risk_level = "CRITICAL"
            warning_bn = "আগাম পাহাড়ি ঢল ও আকস্মিক বন্যার (Flash Flood) প্রবল ঝুঁকি রয়েছে। নিচু জমিতে দীর্ঘমেয়াদী বোরো বা সংবেদনশীল ফসল প্লাবিত হওয়ার সম্ভাবনা।"
            rec_bn = "দ্রুত ঘরে তোলার মতো স্বল্পমেয়াদী ফসল অথবা জলমগ্নতা-সহনশীল (যেমন: BRRI ধান ৫১/৫২) জাত নির্বাচন করুন।"
        elif flood_index > 40 or flash_flood_prob > 0.35:
            risk_level = "MODERATE"
            warning_bn = "মৌসুমি বর্ষাকালে মাঝারি প্লাবনের সম্ভাবনা।"
            rec_bn = "নিষ্কাশন সুবিধাযুক্ত জমিতে মাঝারি মেয়াদী রোপা আমন চাষ করা যেতে পারে।"
        else:
            risk_level = "LOW"
            warning_bn = "বন্যার ঝুঁকি অত্যন্ত কম। পানির অভাব বা খরা মোকাবিলায় জোর দিতে হবে।"
            rec_bn = "স্বাভাবিক সেচ বা বৃষ্টি-নির্ভর ফসল চাষের জন্য উপযুক্ত।"

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name_en,
            "agent_name_bn": self.name_bn,
            "satellite_instrument": "NASA GPM IMERG (0.1° Multi-satellite)",
            "metrics": {
                "daily_rainfall_mm": daily_rain,
                "flood_vulnerability_score": flood_index,
                "flash_flood_probability": flash_flood_prob,
                "extreme_event_flag": extreme_rain
            },
            "status": risk_level,
            "observations_bn": f"নাসার GPM স্যাটেলাইট অনুযায়ী দৈনিক গড় বৃষ্টিপাত {daily_rain} মিমি। সামগ্রিক প্লাবন ঝুঁকি সূচক {flood_index}/১০০।",
            "warning_bn": warning_bn,
            "recommendation_bn": rec_bn,
            "crop_restrictions": ["sensitive_to_submergence"] if risk_level == "CRITICAL" else []
        }

