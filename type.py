from pydantic import BaseModel, Field
from typing import List, Dict, Literal

DamageCategory = Literal["super_effective", "not_very_effective", "immune"]
PokemonType = Literal[ "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy" ]

def default_damage_dict():
    return {
        "super_effective": [],
        "not_very_effective": [],
        "immune": []
    }

class Type(BaseModel):
    name: str
    receives_damage: Dict[DamageCategory, List[str]] = Field(default_factory=default_damage_dict)
    deals_damage: Dict[DamageCategory, List[str]] = Field(default_factory=default_damage_dict)

    def set_defensive_relationship(self, damage_category: DamageCategory, type_list: List[PokemonType]):
        self.receives_damage[damage_category] = type_list

    def set_offensive_relationship(self, damage_category: DamageCategory, type_list: List[PokemonType]):
        self.deals_damage[damage_category] = type_list

    def __str__(self):
        return f"Type: {self.name}"
