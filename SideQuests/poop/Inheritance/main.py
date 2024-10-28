class Animal:
    def __init__(self, name) -> None:
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
#
#
# class Dog(Animal):
#
#     def speak(self):
#         print("WOOF!")
#
#
# class Cat(Animal):
#
#     def speak(self):
#         print("MEOW!")
#
#
# class Mouse(Animal):
#
#     def speak(self):
#         print("SQUEEK!")
#
#
# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mickey")


class Prey(Animal):

    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):

    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey, Animal):
    pass


class Hawk(Predator, Animal):
    pass


class Fish(Prey, Predator, Animal):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

print(rabbit.sleep())
print(fish.flee())
