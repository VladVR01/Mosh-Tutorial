phone = input("phone: ")
digits = {"1": "one",
          "2": "two",
          "3": "three",
          "4": "four"
          }

for ch in phone:
    print(digits.get(ch))
