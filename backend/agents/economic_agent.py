"""
Agent 5: Farmer Priority & Economic Agent (কৃষকের অগ্রাধিকার ও অর্থনীতি)
Data Sources:
- Farmer Manual Input (Priority: Water Savings, Soil Recovery, Max Profit)
- Local wholesale market prices & irrigation diesel/electricity tariffs
"""

from typing import Dict, Any
from .base_agent import BaseAgent
from ..data.crop_database import CROPS

class EconomicAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="economic_agent",
            name_en="Farmer Priority & Economic Agent",
            name_bn="কৃষকের অগ্রাধিকার ও অর্থনীতি বিশ্লেষক",
            data_sources=["Farmer Preferences", "Local Market Rates", "BMDA Irrigation Tariffs"]
        )

    def evaluate(self, env_data: Dict[str, Any], farmer_input: Dict[str, Any]) -> Dict[str, Any]:
        priority = farmer_input.get("priority", "water_saving")  # "water_saving", "soil_health", "max_profit"
        land_area_bigha = float(farmer_input.get("land_area_bigha", 1.0))
        past_crop_id = farmer_input.get("past_crop", "boro_rice")
        past_crop = CROPS.get(past_crop_id, CROPS["boro_rice"])

        # Baseline cost with past crop (e.g. Boro Rice)
        baseline_irrigation_cost = past_crop["irrigation_cost_bdt"] * land_area_bigha
        baseline_input_cost = past_crop["input_cost_per_bigha_bdt"] * land_area_bigha
        baseline_revenue = (past_crop["expected_yield_mound_per_bigha"] * past_crop["market_price_per_mound_bdt"]) * land_area_bigha
        baseline_net_profit = baseline_revenue - (baseline_input_cost + baseline_irrigation_cost)

        # Comparative analysis for sustainable substitute (e.g., Mustard or Lentil)
        substitute_crop = CROPS["mustard"] if priority != "soil_health" else CROPS["lentil"]
        sub_irrigation_cost = substitute_crop["irrigation_cost_bdt"] * land_area_bigha
        sub_input_cost = substitute_crop["input_cost_per_bigha_bdt"] * land_area_bigha
        sub_revenue = (substitute_crop["expected_yield_mound_per_bigha"] * substitute_crop["market_price_per_mound_bdt"]) * land_area_bigha
        sub_net_profit = sub_revenue - (sub_input_cost + sub_irrigation_cost)

        irrigation_savings_bdt = max(0, baseline_irrigation_cost - sub_irrigation_cost)
        irrigation_savings_pct = round((irrigation_savings_bdt / baseline_irrigation_cost * 100), 1) if baseline_irrigation_cost > 0 else 0

        priority_labels = {
            "water_saving": "পানি ও সেচ খরচ বাঁচানো (Water Conservation)",
            "soil_health": "মাটির উর্বরতা ফিরিয়ে আনা (Soil Rejuvenation)",
            "max_profit": "সর্বোচ্চ আর্থিক লাভ (Profit Maximization)"
        }

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name_en,
            "agent_name_bn": self.name_bn,
            "data_source": "Local DAE Market Benchmarks & Farmer Input",
            "metrics": {
                "farmer_priority": priority,
                "farmer_priority_label": priority_labels.get(priority, priority),
                "land_area_bigha": land_area_bigha,
                "baseline_irrigation_cost_bdt": baseline_irrigation_cost,
                "projected_irrigation_cost_bdt": sub_irrigation_cost,
                "irrigation_cost_saved_bdt": irrigation_savings_bdt,
                "irrigation_savings_percentage": irrigation_savings_pct,
                "projected_net_profit_bdt": sub_net_profit
            },
            "status": "OPTIMIZED",
            "observations_bn": f"কৃষকের অগ্রাধিকার: {priority_labels.get(priority)}. জমিতে প্রচলিত ফসলের বদলে বিকল্প ফসল নিলে বিঘাপ্রতি প্রায় {int(irrigation_savings_bdt)} টাকা সেচ খরচ কমবে (সাশ্রয়: {irrigation_savings_pct}%)।",
            "economic_verdict_bn": f"কম খরচে লাভজনক ফসল নির্বাচন কৃষকের আর্থিক ঝুঁকি {irrigation_savings_pct}% কমিয়ে দেবে।"
        }

