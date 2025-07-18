from type_instances import all_types
from type_model import DamageCategory
from typing import get_args

print("--")



if __name__ == "__main__":
    for type in all_types:
        for category in get_args(DamageCategory):
            print(f"\n{type} - {category}")
            print(f"deals: {type.deals[category]}")
            print(f"receives: {type.receives[category]}")
