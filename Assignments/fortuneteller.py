import random


print("i am a fortune teller and i will predict your future")

q1 = input("what is your name\n->")
q2 = input("what is your favorite color\n->")
q3 = input("what is you favorite animal\n->")


def fortune_teller():
    fortune = [
        "you will hit the jackpot in the next 80 years",
        "you will meet someone today",
        "you will break a leg in the next week",
        "you will find a case of a million dollars",
        "the sun will blow up some time in the future",
        "you will be happy before you die ",
        "you will find a nickle",
        "you will become a movie star",
        "you will get drafted",
        "you will live in a big house",

    ]

    return random.choice(fortune),

fortune = fortune_teller()
print(f"your fortune is: {fortune}")