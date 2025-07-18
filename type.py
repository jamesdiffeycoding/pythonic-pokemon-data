from pydantic import BaseModel, Field
from typing import List, Dict


class Type(BaseModel):
    name: str
    receives_damage: Dict[str, List[str]] = Field(default_factory=lambda: {
        "super_effective": [],
        "not_very_effective": [],
        "immune": []
    })
    deals_damage: Dict[str, List[str]] = Field(default_factory=lambda: {
        "super_effective": [],
        "not_very_effective": [],
        "immune": []
    })

    def set_defensive_weaknesses(self, type_list: List[str]):
        self.receives_damage["super_effective"] = type_list

    def set_defensive_resistances(self, type_list: List[str]):
        self.receives_damage["not_very_effective"] = type_list

    def set_defensive_immunities(self, type_list: List[str]):
        self.receives_damage["immune"] = type_list

    def set_offensive_strengths(self, type_list: List[str]):
        self.deals_damage["super_effective"] = type_list

    def set_offensive_ineffectivenesses(self, type_list: List[str]):
        self.deals_damage["not_very_effective"] = type_list

    def set_offensive_immunities(self, type_list: List[str]):
        self.deals_damage["immune"] = type_list

    def __str__(self):
        return f"Type: {self.name}"
