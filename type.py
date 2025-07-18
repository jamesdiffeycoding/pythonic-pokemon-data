class Type:
    def __init__(self, name):
        self.name = name
        self.receives_damage = {
            "super_effective": [],
            "not_very_effective": [],
            "immune": []
        }
        self.deals_damage = {
            "super_effective": [],
            "not_very_effective": [],
            "immune": []
        }

    def set_defensive_weaknesses(self, type_list):
        self.receives_damage["super_effective"] = type_list

    def set_defensive_resistances(self, type_list):
        self.receives_damage["not_very_effective"] = type_list

    def set_defensive_immunities(self, type_list):
        self.receives_damage["immune"] = type_list

    def set_offensive_strengths(self, type_list):
        self.deals_damage["super_effective"] = type_list

    def set_offensive_ineffectivenesses(self, type_list):
        self.deals_damage["not_very_effective"] = type_list

    def set_offensive_immunities(self, type_list):
        self.deals_damage["immune"] = type_list

    def __str__(self):
        return f"Type: {self.name}"
