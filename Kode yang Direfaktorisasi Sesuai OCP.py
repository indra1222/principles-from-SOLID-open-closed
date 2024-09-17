class Food:
    def description(self):
        pass

class Dodol(Food):
    def description(self):
        return "Dodol Garut: Makanan manis dari ketan dan gula."

class Keripik(Food):
    def description(self):
        return "Keripik Singkong: Camilan renyah yang gurih."

class Peuyeum(Food):
    def description(self):
        return "Peuyeum: Tape singkong fermentasi yang manis."

class FoodCalculator:
    def print_description(self, foods):
        for food in foods:
            print(food.description())

# Penggunaan
foods = [Dodol(), Keripik(), Peuyeum()]
calculator = FoodCalculator()
calculator.print_description(foods)
