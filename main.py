class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

p1 = Person("Ali", 25)
p2 = Person("Ali", 25)
p3 = Person("Vali", 30)

print(hash(p1) == hash(p2))  # True
print(hash(p1) == hash(p3))  # False
```

Kodda `__hash__` metodi `Person` klassining har bir obyekti uchun unikal qiymatni qaytaradi. Bu qiymat obyektning `name` va `age` atributlarining kombinatsiyasi bo'lib, u obyektlarning tengligini tekshirish uchun ishlatiladi.
