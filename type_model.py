from helper import log_main_file
from pydantic import BaseModel, Field
from typing import List, Dict, Literal

DamageCategory = Literal["super_effective", "not_very_effective", "immune"]
PokemonType = Literal["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

def default_damage_dict():
    return {
        "super_effective": [],
        "not_very_effective": [],
        "immune": []
    }

class TypeModel(BaseModel):
    name: str
    deals: Dict[DamageCategory, List[str]] = Field(default_factory=default_damage_dict)
    receives: Dict[DamageCategory, List[str]] = Field(default_factory=default_damage_dict)

    def __str__(self):
        return f"Type: {self.name}"


if __name__ == "__main__":
    log_main_file()
