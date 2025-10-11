## Inheritance

Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit properties and methods from another class. This helps to promote code reusability and establish a hierarchical relationship between classes.

### Explanation

In inheritance, a new class (known as the child or derived class) inherits attributes and behaviors (methods) from an existing class (known as the parent or base class). This allows the child class to extend or modify the functionalities of the parent class.

### Example

Here's a simple example to illustrate inheritance:

```python
# Parent class
class Animal:
    def speak(self):
        return "Animal sound"

# Child class
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Another Child class
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances of Dog and Cat
my_dog = Dog()
my_cat = Cat()

print(my_dog.speak())  # Output: Woof!
print(my_cat.speak())  # Output: Meow!
```

In this example, both `Dog` and `Cat` classes inherit from the `Animal` class. They override the `speak` method to provide their specific implementations while still being able to access properties and methods from the `Animal` class.