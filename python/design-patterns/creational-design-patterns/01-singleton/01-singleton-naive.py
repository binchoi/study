
"""
Singleton is a creational design pattern that lets you ensure that a class has only one instance,
while providing a global access point to this instance.

This pattern solves two problems (thereby violating the Single Responsibility Principle):
1. Ensure that a class has just a single instance. This is generally to control access to some shared
   resource such as a database or a file.
   This behavior is impossible to achieve using regular constructor whose call must always yield a new object.
2. Provide a global access point to that instance. One must be able to access the object from anywhere in the
   program but also protect that instance from being overwritten by other code.

All implementations of the Singleton have these two steps in common:
1. Make the default constructor private, to prevent other objects from using the new operator with the Singleton
   class.
2. Create a static creation method that acts as a constructor. Under the hood, this method calls the private
   constructor to create an object and saves it in a static field. All following calls to this method return the
   cached object.
"""


# Naive Singleton [using metaclass method]

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print("Some business logic has been executed")


if __name__ == "__main__":
    id_set = set()
    for i in range(10):
        new_instance = Singleton()  # __call__ is called, checks _instances [={"Singleton"->singleton_object}]
        id_set.add(id(new_instance))
    if len(id_set) == 1:
        print("Singleton worked!")
    else:
        print("Singleton failed...")
