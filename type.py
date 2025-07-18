class Type:
    def __init__(self, name):
        self.name = name
        self.weak_to = []
        self.strong_against = []
        self.resist = []
        self.immune_to = []

    def add_weakness(self, type_name):
        self.weak_to.append(type_name)

    def add_strength(self, type_name):
        self.strong_against.append(type_name)

    def add_resistance(self, type_name):
        self.resist.append(type_name)

    def add_immunity(self, type_name):
        self.immune_to.append(type_name)

    def __str__(self):
        return f"Type: {self.name}"
