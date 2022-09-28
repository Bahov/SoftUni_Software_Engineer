class Zoo:
    __animals_count = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, animal_name):
        if species == 'mammal':
            self.mammals.append(animal_name)
        elif species == 'fish':
            self.fish.append(animal_name)
        elif species == 'bird':
            self.birds.append(animal_name)
    
        Zoo.__animals_count += 1
    
    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fish)}\n"
        elif species == 'bird':
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"
        
        result += f'Total animals: {Zoo.__animals_count}'
        return result

object_zoo = Zoo(input())
number_of_animals = int(input())

for i in range(number_of_animals):
    animal = input().split(' ')
    species = animal[0]
    animal_name = animal[1]
    object_zoo.add_animal(species, animal_name)

print(object_zoo.get_info(input()))