from helper import log_file_running
from type_model import TypeModel

all_types = [
    TypeModel(
        name="Normal",
        receives={
            "super_effective": ["Fighting"],
            "not_very_effective": [],
            "immune": ["Ghost"]
        },
        deals={
            "super_effective": [],
            "not_very_effective": ["Rock", "Steel"],
            "immune": ["Ghost"]
        }
    ),
    TypeModel(
        name="Fire",
        receives={
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Ice", "Bug", "Steel", "Fairy"],
            "immune": []
        },
        deals={
            "super_effective": ["Grass", "Ice", "Bug", "Steel"],
            "not_very_effective": ["Fire", "Water", "Rock", "Dragon"],
            "immune": []
        }
    ),
    TypeModel(
        name="Water",
        receives={
            "super_effective": ["Electric", "Grass"],
            "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "immune": []
        },
        deals={
            "super_effective": ["Fire", "Ground", "Rock"],
            "not_very_effective": ["Water", "Grass", "Dragon"],
            "immune": []
        }
    ),
    TypeModel(
        name="Electric",
        receives={
            "super_effective": ["Ground"],
            "not_very_effective": ["Electric", "Flying", "Steel"],
            "immune": []
        },
        deals={
            "super_effective": ["Water", "Flying"],
            "not_very_effective": ["Electric", "Grass", "Dragon"],
            "immune": []
        }
    ),
    TypeModel(
        name="Grass",
        receives={
            "super_effective": ["Fire", "Ice", "Poison", "Flying", "Bug"],
            "not_very_effective": ["Water", "Electric", "Grass", "Ground"],
            "immune": []
        },
        deals={
            "super_effective": ["Water", "Ground", "Rock"],
            "not_very_effective": ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
            "immune": []
        }
    ),
    TypeModel(
        name="Ice",
        receives={
            "super_effective": ["Fire", "Fighting", "Rock", "Steel"],
            "not_very_effective": ["Ice"],
            "immune": []
        },
        deals={
            "super_effective": ["Grass", "Ground", "Flying", "Dragon"],
            "not_very_effective": ["Fire", "Water", "Ice", "Steel"],
            "immune": []
        }
    ),
    TypeModel(
        name="Fighting",
        receives={
            "super_effective": ["Flying", "Psychic", "Fairy"],
            "not_very_effective": ["Bug", "Rock", "Dark"],
            "immune": []
        },
        deals={
            "super_effective": ["Normal", "Ice", "Rock", "Dark", "Steel"],
            "not_very_effective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "immune": []
        }
    ),
    TypeModel(
        name="Poison",
        receives={
            "super_effective": ["Ground", "Psychic"],
            "not_very_effective": ["Fighting", "Poison", "Bug", "Grass", "Fairy"],
            "immune": []
        },
        deals={
            "super_effective": ["Grass", "Fairy"],
            "not_very_effective": ["Poison", "Ground", "Rock", "Ghost"],
            "immune": []
        }
    ),
    TypeModel(
        name="Ground",
        receives={
            "super_effective": ["Water", "Grass", "Ice"],
            "not_very_effective": ["Poison", "Rock"],
            "immune": ["Electric"]
        },
        deals={
            "super_effective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "not_very_effective": ["Grass", "Bug"],
            "immune": []
        }
    ),
    TypeModel(
        name="Flying",
        receives={
            "super_effective": ["Electric", "Ice", "Rock"],
            "not_very_effective": ["Grass", "Fighting", "Bug"],
            "immune": ["Ground"]
        },
        deals={
            "super_effective": ["Grass", "Fighting", "Bug"],
            "not_very_effective": ["Electric", "Rock", "Steel"],
            "immune": []
        }
    ),
    TypeModel(
        name="Psychic",
        receives={
            "super_effective": ["Bug", "Ghost", "Dark"],
            "not_very_effective": ["Fighting", "Psychic"],
            "immune": []
        },
        deals={
            "super_effective": ["Fighting", "Poison"],
            "not_very_effective": ["Psychic", "Steel"],
            "immune": []
        }
    ),
    TypeModel(
        name="Bug",
        receives={
            "super_effective": ["Fire", "Flying", "Rock"],
            "not_very_effective": ["Fighting", "Ground", "Grass"],
            "immune": []
        },
        deals={
            "super_effective": ["Grass", "Psychic", "Dark"],
            "not_very_effective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
            "immune": []
        }
    ),
    TypeModel(
        name="Rock",
        receives={
            "super_effective": ["Water", "Grass", "Fighting", "Ground", "Steel"],
            "not_very_effective": ["Normal", "Fire", "Poison", "Flying"],
            "immune": []
        },
        deals={
            "super_effective": ["Fire", "Ice", "Flying", "Bug"],
            "not_very_effective": ["Fighting", "Ground", "Steel"],
            "immune": []
        }
    ),
    TypeModel(
        name="Ghost",
        receives={
            "super_effective": ["Ghost", "Dark"],
            "not_very_effective": ["Poison", "Bug"],
            "immune": ["Normal", "Fighting"]
        },
        deals={
            "super_effective": ["Psychic", "Ghost"],
            "not_very_effective": ["Dark"],
            "immune": []
        }
    ),
    TypeModel(
        name="Dragon",
        receives={
            "super_effective": ["Ice", "Dragon", "Fairy"],
            "not_very_effective": ["Fire", "Water", "Electric", "Grass"],
            "immune": []
        },
        deals={
            "super_effective": ["Dragon"],
            "not_very_effective": ["Steel"],
            "immune": []
        }
    ),
    TypeModel(
        name="Dark",
        receives={
            "super_effective": ["Fighting", "Bug", "Fairy"],
            "not_very_effective": ["Ghost", "Dark"],
            "immune": ["Psychic"]
        },
        deals={
            "super_effective": ["Psychic", "Ghost"],
            "not_very_effective": ["Fighting", "Dark", "Fairy"],
            "immune": []
        }
    ),
    TypeModel(
        name="Steel",
        receives={
            "super_effective": ["Fire", "Fighting", "Ground"],
            "not_very_effective": ["Normal", "Grass", "Ice", "Flying", "Psychic", "Bug", "Rock", "Dragon", "Steel", "Fairy"],
            "immune": ["Poison"]
        },
        deals={
            "super_effective": ["Ice", "Rock", "Fairy"],
            "not_very_effective": ["Fire", "Water", "Electric", "Steel"],
            "immune": []
        }
    ),
    TypeModel(
        name="Fairy",
        receives={
            "super_effective": ["Poison", "Steel"],
            "not_very_effective": ["Fighting", "Bug", "Dark"],
            "immune": ["Dragon"]
        },
        deals={
            "super_effective": ["Fighting", "Dragon", "Dark"],
            "not_very_effective": ["Fire", "Poison", "Steel"],
            "immune": []
        }
    ),
]

if __name__ == "__main__":
    log_file_running()
    for type in all_types:
        print(f"{type} - {type.model_dump()}\n")