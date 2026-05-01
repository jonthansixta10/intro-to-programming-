my_dict = {"Alice": "A",
            "Bob": "B",
            "Charlie": "C",
            "David": "A",
            "Eve": "B"
           }
print(my_dict)
for name, grade in my_dict.items():
    print(f"{name}: {grade}")
