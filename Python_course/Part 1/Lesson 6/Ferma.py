class Animals:
    feed = 0
    speak = ""
    name = ""
    weight = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feeding(self):
        self.feed += 10

    def speaking(self):
        if self.speak == "ko-ko-ko":
            print("It's hen")
        elif self.speak == "muu":
            print("It's cow")
        elif self.speak == "beee":
            return "It's sheep"
        elif self.speak == "ga-ga-ga":
            print("It's goose")
        elif self.speak == "be-be":
            print("It's goat")
        elif self.speak == "krya-krya":
            print("It's duck")
        else:
            print("Animal not found")


class Cow(Animals):
    milk = 100
    speak = "muu"

    def milking(self):
        self.milk -= 25


class Hen(Animals):
    eggs = 100
    speak = "ko-ko-ko"

    def collect_eggs(self):
        self.eggs -= 20


class Sheep(Animals):
    hair = 100
    speak = "beee"

    def cut_hair(self):
        self.hair -= 20


class Duck(Animals):
    eggs = 50
    speak = "krya-krya"

    def collect_eggs(self):
        self.eggs -= 10


class Goat(Animals):
    milk = 60
    speak = "be-be"

    def milking(self):
        self.milk -= 10


class Goose(Animals):
    eggs = 40
    speak = "ga-ga-ga"

    def collect_eggs(self):
        self.eggs -= 6


duck1 = Duck("Кряква", 25)
goat1 = Goat("Рог", 57)
goat2 = Goat("Копыто", 48)
goose1 = Goose("Серый", 24)
goose2 = Goose("Белый", 29)
cow1 = Cow("Манька", 138)
sheep1 = Sheep("Барашек", 87)
sheep2 = Sheep("Кудрявый", 90)
hen1 = Hen("Ко-Ко", 8)
hen2 = Hen("Кукареку", 5)

dict_animals = {"Рог": goat1.weight, "Копыто": goat2.weight, "Серый": goose1.weight, "Белый": goose2.weight, "Манька":
    cow1.weight, "Барашек": sheep1.weight, "Кудрявый": sheep2.weight, "Ко-Ко": hen1.weight,
                "Кукареку": hen2.weight}

animal_weight = 0
animal_name = ""
all_weight = 0

for key, value in dict_animals.items():
    all_weight += value
    if value > animal_weight:
        animal_weight = value
        animal_name = key

print("Общий вес всех животных:", str(all_weight) + "кг")
print("Самое тяжолое животное:", animal_name, animal_weight)
