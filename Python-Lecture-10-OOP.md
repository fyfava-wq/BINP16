# BINP16 — Lecture 10: Fundamentals of Object-Oriented Programming (OOP)
## Git Cheat Sheet

Based on the Lecture 10 PDF and the accompanying Python demonstration and exercise files.

---

## 1. What is object-oriented programming?

Object-oriented programming (OOP) organises code into **classes** and **objects**.

- **Class:** a blueprint describing the attributes and methods that its objects have.
- **Object / instance:** a particular item created from a class.
- **Attribute:** data stored on an object.
- **Method:** a function defined inside a class that describes behaviour.
- **Constructor (`__init__`)**: initialises a new object's attributes.
- **`self`:** refers to the particular object whose instance method is running.

Think of the class as a blank student form and each object as a completed student record (Lecture 10 PDF, pages 2–5).

```python
class Bacteria:
    def __init__(self, species, genome_size):
        self.species = species
        self.genome_size = genome_size

    def describe(self):
        print(f"{self.species}: {self.genome_size} Mb")

b1 = Bacteria("E. coli", 5.0)
b2 = Bacteria("B. subtilis", 4.2)

b1.describe()  # E. coli: 5.0 Mb
b2.describe()  # B. subtilis: 4.2 Mb
```

### Understand `self`

When you call:

```python
b1.describe()
```

Python passes `b1` as the first argument to the instance method. Conceptually, this is similar to:

```python
Bacteria.describe(b1)
```

Therefore, `self.species` refers to the species stored in the object calling the method. `self` is used in ordinary instance methods too—not only in `__init__`.

## 2. The four principles of OOP

The lecture introduces four core principles (PDF, page 7).

| Principle | Meaning | Key idea |
|---|---|---|
| **Inheritance** | A child class gets attributes and methods from a parent class | Reuse code |
| **Polymorphism** | The same method name can behave differently for different objects | One interface, different behaviour |
| **Encapsulation** | Keep data and related methods together and control access to data | Protect/validate updates |
| **Abstraction** | Expose essential functionality while hiding implementation details | Simple public interface |

---

## 3. Inheritance

**Inheritance** allows a child class to reuse attributes and methods from a parent class and add its own features.

- **Parent / base class:** defines common attributes and behaviour.
- **Child / derived class:** inherits from the parent and can add specialised attributes or methods.
- `class Child(Parent):` declares inheritance.
- `super().__init__(...)` calls the parent constructor.

Example from the bacterial-classification exercise:

```python
class Bacteria:
    def __init__(self, species, genome_size):
        self.species = species
        self.genome_size = genome_size

    def describe(self):
        print("Species:", self.species)
        print("Genome size:", self.genome_size, "Mb")


class PathogenicBacteria(Bacteria):
    def __init__(self, species, genome_size, disease):
        super().__init__(species, genome_size)
        self.disease = disease

    def show_disease(self):
        print("Disease:", self.disease)


class BeneficialBacteria(Bacteria):
    def __init__(self, species, genome_size, benefit):
        super().__init__(species, genome_size)
        self.benefit = benefit

    def show_benefit(self):
        print("Benefit:", self.benefit)


b1 = PathogenicBacteria(
    "Mycobacterium tuberculosis", 4.4, "Tuberculosis"
)
b2 = BeneficialBacteria(
    "Lactobacillus acidophilus", 2.0, "Supports gut health"
)

b1.describe()      # inherited method
b1.show_disease()  # child-specific method
b2.describe()      # inherited method
b2.show_benefit()  # child-specific method
```

**Remember:** `PathogenicBacteria` does not automatically have `show_benefit()`. That method belongs to `BeneficialBacteria`, not the shared parent class.

### Inheritance pattern

```python
class Parent:
    def __init__(self, common_value):
        self.common_value = common_value

    def common_method(self):
        print(self.common_value)


class Child(Parent):
    def __init__(self, common_value, extra_value):
        super().__init__(common_value)
        self.extra_value = extra_value

    def child_method(self):
        print(self.extra_value)
```

---

## 4. Polymorphism

**Polymorphism** means “many forms”: the same method name can produce different behaviour depending on the object's class.

### Method overriding

A child class overrides a method by defining a method with the same name as a method inherited from the parent.

```python
class Organism:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print("Name:", self.name)

    def reproduce(self):
        print("Organisms reproduce in different ways")


class Bacteria(Organism):
    def reproduce(self):
        print("Bacteria reproduce by binary fission")


class Fungi(Organism):
    def reproduce(self):
        print("Fungi reproduce by spores")


class Plants(Organism):
    def reproduce(self):
        print("Plants reproduce by seeds")


organisms = [
    Bacteria("E. coli"),
    Fungi("Aspergillus"),
    Plants("Sunflower")
]

for organism in organisms:
    organism.describe()   # inherited from Organism
    organism.reproduce()  # behaviour depends on the object's class
```

The loop uses the same call, `organism.reproduce()`, for each object. Each class supplies its own behaviour.

**Key distinction:**
- Inheritance provides shared functionality.
- Overriding changes inherited behaviour.
- Polymorphism lets you call the same method across different object types.

---

## 5. Encapsulation

**Encapsulation** keeps data and the methods that work with it together inside a class, while controlling how attributes are accessed or modified (PDF, pages 17–21).

### Python attribute naming conventions

| Syntax | Common name | Meaning |
|---|---|---|
| `self.name` | Public | Intended to be accessed directly |
| `self._name` | Protected (convention) | Signals that an attribute is intended for internal use and subclasses |
| `self.__name` | Private / name-mangled | Python changes the internal name to discourage accidental access |

Python's single underscore is a convention, not strict access enforcement. Double leading underscores trigger **name mangling**; they do not make data absolutely inaccessible.

```python
class Student:
    def __init__(self, name, marks, age):
        self.name = name       # public
        self._marks = marks    # protected convention
        self.__age = age       # name-mangled


student = Student("Rahul", 85, 20)

print(student.name)    # Rahul
print(student._marks)  # 85 (accessible, but intended for internal use)
# print(student.__age) # AttributeError
```

The double-underscore attribute is internally name-mangled to `_Student__age`, so `student._Student__age` can technically access it. In normal code, use a public method or property instead.

### Getter and setter methods

- **Getter:** returns an attribute's value; usually does not need a new value as an argument.
- **Setter:** accepts a new value, validates it, and updates the attribute only when valid.

Lecture example: bacterial genome size must be greater than zero.

```python
class Bacteria:
    def __init__(self, species, genome_size):
        self.__species = species
        self.__genome_size = genome_size

    def get_species(self):
        return self.__species

    def get_genome_size(self):
        return self.__genome_size

    def set_genome_size(self, genome_size):
        if genome_size > 0:
            self.__genome_size = genome_size
        else:
            print("Invalid genome size")

    def describe(self):
        print(
            f"Species: {self.__species}, "
            f"Genome size: {self.__genome_size} Mb"
        )


b1 = Bacteria("E. coli", 5.0)
b2 = Bacteria("B. subtilis", 4.2)

b1.describe()
b2.describe()

b1.set_genome_size(5.5)
b1.describe()  # genome size is now 5.5 Mb

b2.set_genome_size(-3.0)  # Invalid genome size
print(b2.get_genome_size())  # remains 4.2
```

A setter protects the object from invalid updates by checking the value before changing the attribute.

### Marks validation example

```python
class Student:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print(f"{marks} is an invalid mark")

    def get_marks(self):
        return self.__marks


student = Student(85)
student.set_marks(1000)       # invalid; value is not changed
print(student.get_marks())    # 85
```

---

## 6. Abstraction

**Abstraction** hides unnecessary implementation details and exposes the essential functionality to the user (PDF, pages 24–25).

The student-grade exercise makes the grade-calculation method internal and exposes a public method to display the result:

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

    def display_result(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        grade = self.__calculate_grade()
        print("Grade:", grade)


student = Student("Rahul", 95)
student.display_result()
```

The user calls `display_result()` without needing to know the internal steps used to calculate the grade.

**Important distinction:** in this lecture's example, abstraction is demonstrated using a public method and a double-underscore internal method (name mangling). The PDF also introduces the idea of abstract base classes, but does not require advanced abstract-class code.

---

## 7. Special methods

| Method | Purpose in the lecture |
|---|---|
| `__init__(self, ...)` | Initialise a new object's attributes |
| `__del__(self)` | Destructor method, called when an object is being finalised |

Example:

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __del__(self):
        print(f"Destructor called for {self.name}")
```

`del student` removes that name/reference; it does not guarantee that the destructor message appears immediately in every Python environment. Avoid relying on `__del__` for important cleanup.

---

## 8. Quick comparison

| Concept | Question to ask | Example from Lecture 10 |
|---|---|---|
| Class/object | What is the blueprint, and what is one instance? | `Bacteria` and `b1 = Bacteria(...)` |
| `self` | Which object is this method working on? | `self.species` |
| Inheritance | Which attributes/methods are reused from a parent? | `PathogenicBacteria(Bacteria)` |
| `super()` | How does the child call the parent constructor? | `super().__init__(species, genome_size)` |
| Polymorphism | How can the same method name behave differently? | `organism.reproduce()` |
| Overriding | How does a child replace inherited behaviour? | `Bacteria.reproduce()` |
| Encapsulation | How are attribute updates controlled? | `set_genome_size()` validates input |
| Getter | How do I retrieve a protected internal value through a method? | `get_genome_size()` |
| Setter | How do I validate and update a value? | `set_genome_size(5.5)` |
| Abstraction | What public action can I use without knowing its internal details? | `display_result()` |

---

## 9. Common errors and reminders

- **Forgetting `self`:** instance methods normally declare `self` as their first parameter.
- **Forgetting `self.`:** writing `species = species` does not store an instance attribute; use `self.species = species`.
- **Forgetting `super().__init__(...)`:** child classes may fail to initialise the parent attributes.
- **Calling a child-only method on the wrong class:** `show_benefit()` is not available on a `PathogenicBacteria` object in the lecture example.
- **Expecting `__age` to be public:** `student.__age` raises `AttributeError` in the demonstration because of name mangling.
- **Skipping validation:** a setter should reject invalid input without overwriting the previous valid value.
- **Confusing abstraction with inheritance:** inheritance is reuse from a parent; abstraction hides implementation details behind a simpler interface.
- **Overriding the wrong method name:** the method name must match the parent method for overriding to occur.

---

## 10. Practice questions

Try answering these without looking at the notes above.

1. What is the difference between a class and an object?
2. What does `self` refer to?
3. Why does a child class call `super().__init__(...)`?
4. In the bacterial example, which methods are inherited by `PathogenicBacteria`?
5. What is method overriding?
6. How does the `organism.reproduce()` loop demonstrate polymorphism?
7. What is the difference between `self.name`, `self._name`, and `self.__name`?
8. Why does `set_genome_size(-3.0)` leave the previous genome size unchanged?
9. How does `display_result()` demonstrate abstraction?
10. What is the difference between a getter and a setter?

---

## Source materials

Based on the uploaded **Lecture10.Fundamentals_of_OOP.pdf** and these accompanying scripts:

- `Lecture10.OOP.py`
- `Lecture10.Exercise.class.py`
- `Lecture10.Exercise.inheritance.py`
- `Lecture10.Exercise.polymorphism.py`
- `Lecture10.Exercise.encapsulation.py`
- `Lecture10.Exercise.abstraction.py`

PDF page references in this sheet refer to the 26-page lecture PDF.
