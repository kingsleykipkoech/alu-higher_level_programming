# Python - Input/Output

This directory contains implementation files for Python Input/Output tasks, covering:
- File reading and writing.
- Serialization and deserialization using JSON format.
- Class conversion to/from JSON dictionary.
- Interview preparation with Pascal's Triangle.

## Tasks

* **0. Read file**: Function `read_file(filename="")` reading UTF8 text file.
* **1. Write to a file**: Function `write_file(filename="", text="")` writing string and returning character count.
* **2. Append to a file**: Function `append_write(filename="", text="")` appending string and returning added character count.
* **3. To JSON string**: Function `to_json_string(my_obj)` returning JSON representation.
* **4. From JSON string to Object**: Function `from_json_string(my_str)` deserializing JSON string.
* **5. Save Object to a file**: Function `save_to_json_file(my_obj, filename)` saving object in JSON to text file.
* **6. Create object from a JSON file**: Function `load_from_json_file(filename)` deserializing file JSON.
* **7. Load, add, save**: Script `7-add_item.py` adding command line arguments to JSON list.
* **8. Class to JSON**: Function `class_to_json(obj)` returning instance dict for JSON serialization.
* **9. Student to JSON**: Class `Student` representing a student.
* **10. Student to JSON with filter**: Class `Student` with attributes filter.
* **11. Student to disk and reload**: Class `Student` with reload from dictionary.
* **12. Pascal's Triangle**: Function `pascal_triangle(n)` generating Pascal's Triangle.
