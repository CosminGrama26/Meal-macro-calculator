class Food:
    def __init__(self, name, fat, carbs, protein):
        self._fat = 0
        self._carbs = 0
        self._protein = 0
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.calories = (self.fat * 9) + (self.carbs * 4) + (self.protein * 4)

    def __str__(self):
        return f"{self.name} has {self.fat} fat, {self.carbs} carbs and {self.protein} protein"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def fat(self):
        return self._fat

    @fat.setter
    def fat(self, fat):
        if float(fat) + self.carbs + self.protein > 100:
            print("Macro sum cannot exceed 100g!")
            raise ValueError
        if float(fat) < 0:
            print("Macro value cannot be below 0!")
            raise ValueError
        self._fat = float(fat)

    @property
    def carbs(self):
        return self._carbs

    @carbs.setter
    def carbs(self, carbs):
        if self.fat + float(carbs) + self.protein > 100:
            print("Macro sum cannot exceed 100g!")
            raise ValueError
        if float(carbs) < 0:
            print("Macro value cannot be below 0!")
            raise ValueError
        self._carbs = float(carbs)

    @property
    def protein(self):
        return self._protein

    @protein.setter
    def protein(self, protein):
        if self.fat + self.carbs + float(protein) > 100:
            print("Macro sum cannot exceed 100g!")
            raise ValueError
        if float(protein) < 0:
            print("Macro value cannot be below 0!")
            raise ValueError
        self._protein = float(protein)

    @property
    def grams(self):
        return self._grams

    @grams.setter
    def grams(self, grams):
        self._grams = int(grams)
