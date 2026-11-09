"""
Base Agent Module: Defines the standardized contract for all specialist agents.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    def __init__(self, agent_id: str, name_en: str, name_bn: str, data_sources: list):
        self.agent_id = agent_id
        self.name_en = name_en
        self.name_bn = name_bn
        self.data_sources = data_sources

    @abstractmethod
    def evaluate(self, env_data: Dict[str, Any], farmer_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes satellite and local data to produce an expert evaluation report.
        Must return a structured dictionary containing status, scores, warnings, and recommendations.
        """
        pass

