from helper import log_main_file
from type_instances import all_types
from type_model import DamageCategory
from typing import get_args

ranked_types_detailed = [{
        "name": t.name,
        "deals_super_effective": len(t.deals["super_effective"]),
        "deals_not_very_effective": len(t.deals["not_very_effective"]),
        "deals_immune": len(t.deals["immune"]),
        "receives_super_effective": len(t.receives["super_effective"]),
        "receives_not_very_effective": len(t.receives["not_very_effective"]),
        "receives_immune": len(t.receives["immune"]),
    } for t in all_types]

sorting_category = "deals_super_effective"

ranked_types_detailed_sorted = sorted(
    ranked_types_detailed,
    key=lambda x: x[sorting_category],
    reverse=True
)

if __name__ == "__main__":
    log_main_file()
    print(f"data sorted by - {sorting_category}")
    for t in ranked_types_detailed_sorted:
        print(f"{t['name']} {t[sorting_category]}")

