# Python - Inheritance

This directory contains implementation files for Python Inheritance tasks, covering:
- Object attributes and methods lookup.
- Class inheritance and subclass validation.
- Exception raising and input validation.
- Subclasses of base geometry shapes (Rectangle and Square).

## Tasks

* **0. Lookup**: Function `lookup(obj)` returning the list of available attributes/methods of an object.
* **1. My list**: Class `MyList` that inherits from `list` with a `print_sorted` method.
* **2. Exact same object**: Function `is_same_class(obj, a_class)` checking if an object is exactly an instance of a class.
* **3. Same class or inherit from**: Function `is_kind_of_class(obj, a_class)` checking if an object is an instance or subclass instance.
* **4. Only sub class of**: Function `inherits_from(obj, a_class)` checking if an object is an instance of a subclass.
* **5. Geometry module**: Empty class `BaseGeometry`.
* **6. Improve Geometry**: Method `area` raising an Exception.
* **7. Integer validator**: Method `integer_validator` validating positive integers.
* **8. Rectangle**: Class `Rectangle` inheriting from `BaseGeometry` with private width and height.
* **9. Full rectangle**: Class `Rectangle` with `area` implementation and custom `__str__`.
* **10. Square #1**: Class `Square` inheriting from `Rectangle` with size validation.
* **11. Square #2**: Class `Square` inheriting from `Rectangle` with custom `__str__`.
