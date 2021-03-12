class Animal:
    def __init__(self, age, weight, height, area, is_alive=True):
        self.age = age
        self.weight = weight
        self.height = height
        self.area = area
        self.is_alive = is_alive

    def __str__(self):
        return f"{self.__class__.__name__} (age = {self.age}, " \
               f"weight = {self.weight})"


class Dog(Animal):

    def __init__(self, color, name, age, weight, height, area, is_alive=True,
                 breed=None, is_vaccinated=False, owner=None):
        super().__init__(age, weight, height, area, is_alive)
        self.color = color
        self.name = name
        self.breed = breed
        self.is_vaccinated = is_vaccinated
        self.owner = owner

    def __str__(self):
        return f"{self.__class__.__name__} (color = {self.color}, name = {self.name}, " \
               f"area = {self.area})"


bird = Animal(3, 1, 0.7, 'United States')
print(bird)

richard = Dog('white', 'Richard', 0.5, 3, 0.3, 'Azerbaijan', 'Nigar M.')
print(richard)
print(richard.color)
print(richard.age)
