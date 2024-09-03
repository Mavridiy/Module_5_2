
class House:


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        first_floor = 1
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            while first_floor <= new_floor:
                print(first_floor)
                first_floor += 1

    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return (f'Назавние: {self.name}, кол-во этажей: { self.number_of_floors}')

h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)
# h1.go_to(5)
# h2.go_to(10)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))




