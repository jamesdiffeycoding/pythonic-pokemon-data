from helper import log_main_file
from type_instances import all_types
from type_model import DamageCategory
from typing import get_args, Literal

all_types_counts = [{
        "name": t.name[:5],
        "deals": {
            "super_effective": len(t.deals["super_effective"]),
            "not_very_effective": len(t.deals["not_very_effective"]),  # fixed
            "immune": len(t.deals["immune"]),
        },
        "receives": {
            "super_effective": len(t.receives["super_effective"]),
            "not_very_effective": len(t.receives["not_very_effective"]),  # fixed
            "immune": len(t.receives["immune"]),
        }
    } for t in all_types]

def sorted_all_types_counts(direction: Literal["deals", "receives"], sorting_category: str):
    sorted_data = sorted(
        all_types_counts,
        key=lambda x: x[direction][sorting_category],
        reverse=True
    )
    return [(t["name"], t[direction][sorting_category]) for t in sorted_data]

if __name__ == "__main__":
    log_main_file()
    for direction in ["deals", "receives"]:

        for category in get_args(DamageCategory):
            print(f'{category} - {sorted_all_types_counts(direction, category)}')
