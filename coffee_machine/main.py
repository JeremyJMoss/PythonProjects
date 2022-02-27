class CoffeeMachine:
    def __init__(self):
        self._milk = 2000
        self._water = 1000
        self._coffee = 500

    @property
    def milk(self):
        return self._milk

    @milk.setter
    def milk(self, ml: int):
        self._milk = ml

    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, ml: int):
        self._water = ml

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, g: int):
        self._coffee = g

    def fill_milk(self, ml: int):
        self._milk += ml

    def fill_water(self, ml: int):
        self._water += ml

    def add_coffee(self, g: int):
        self._coffee += g

    def use_milk(self, ml):
        if self._milk < ml:
            print("Not enough milk!")
            return False
        self._milk -= ml
        return True

    def use_water(self, ml):
        if self._water < ml:
            print("Not enough water!")
            return False
        self._water -= ml
        return True

    def use_coffee(self, g):
        if self._coffee < g:
            print("Not enough coffee!")
            return False
        self._coffee -= g
        return True

    def make_latte(self, shots: int = 1):
        if self.use_milk(85) and self.use_water(30 * shots) and self.use_coffee(9 * shots):
            return f"Here is your Latte with {shots} shots"
        return "Please fill the machine!"

    def make_cappuccino(self, shots: int = 1):
        if self.use_milk(85) and self.use_water(30 * shots) and self.use_coffee(9 * shots):
            return f"Here is your Cappuccino with {shots} shots"
        return "Please fill the machine!"

    def make_espresso(self, shots: int = 1):
        if self.use_water(30 * shots) and self.use_coffee(9 * shots):
            return f"Here is your Espresso with {shots} shots"
        return "Please fill the machine!"

    def make_piccolo(self, shots: int = 1):
        if self.use_milk(40) and self.use_water(30 * shots) + self.use_coffee(9 * shots):
            return f"Here is your Piccolo Latte with {shots} shots"
        return "Please fill the machine!"

    def make_coffee(self):
        coffee = input("What coffee would you like?\nlatte\ncappuccino\nespresso\npiccolo\n")
        shots = int(input("How many shots would you like? "))
        if coffee == "latte":
            made_coffee = self.make_latte(shots)
        elif coffee == "cappuccino":
            made_coffee = self.make_cappuccino(shots)
        elif coffee == "espresso":
            made_coffee = self.make_espresso(shots)
        elif coffee == "piccolo":
            made_coffee = self.make_piccolo(shots)
        print(made_coffee)


coffee_machine = CoffeeMachine()
coffee_machine.make_coffee()
coffee_machine.make_coffee()
