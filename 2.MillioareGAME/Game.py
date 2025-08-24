print("NOTE: All prizes will be awarded in Indian Rupees.\n\n")
questions = [
    ["Which fruit was once called a “love apple”?", "Pomegranate", "Strawberry", "Cherry",  "Tomato", 4],
    ["What is special about the number zero in mathematics?", "It is the only even prime number", "It has no Roman numeral representation", "It is always positive", "It cannot be used in computers", 2], 
    ["Which country has a national flag that is NOT rectangular?", "Switzerland", "Nepal", "Bhutan", "Vatican City", 2],
    ["What is the only letter that does not appear in the name of any U.S. state?", "Q", "X", "Z", "J", 1],
    ["Which planet rotates backwards compared to most other planets?", "Mar", "Neptune",  "Venus","Jupiter", 3],
    ["The oldest known written recipe in the world is for what?", "Bread", "Beer", "Cheese", "Soup", 2],
    ["Which animal can hold its breath longer than a dolphin?", "Crocodile", "Tortoise", "Elephant",  "Sloth", 4],
    ["Which city is nicknamed “The City of Canals”?", "Venice", "Amsterdam", "Bangkok", "Bruges", 1],
    ["The sound of which animal is officially banned as a ringtone in Japan (for being too stressful)?", "Dog", "Cat", "Crow", "Rooster", 3],
    ["What is the only food that never spoils naturally?", "Honey", "Rice", "Salt", "Sugar", 1],
    ["What does the pass statement do in Python?", "Exits the program", "Skips the current loop", "Does nothing", "Raises an error", 3]
]

prizes = [1000, 5000, 10000, 25000, 50000, 70000, 100000, 250000, 500000, 750000, 1000000]
total = 0
i = 0

for question in questions:

    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a = int(input("\nPlease enter your answer.\nPress 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if(question[5] == a):
        print("\nYour answer is correct!!")
    else:
        print(f"\nYour answer is Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!\n")
        break
    total += prizes[i]
    print(f"Congratulations,You have won {prizes[i]}\n\n")
    i += 1