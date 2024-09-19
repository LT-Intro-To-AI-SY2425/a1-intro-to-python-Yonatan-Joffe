# Complete your individualized AI problems here


#number game
import random
def guesser():
    number = random.randint(1,100)
    condition = False
    while not condition:
        userinput = input("enter a number between 1,100: ")
        guess = int(userinput)
        if guess == number:
            condition = True
            print("congrates the number was ", number)
            return
        if guess >= number:
            print("Guess was to high. Try again:")
        if guess <= number:
            print("Guess was to low. Try again:")

guesser()



# Age calc

def calc():
    month = int(input("what month is it in number form: "))
    day = int(input("what day is it: "))
    year = int(input("what year is it: "))
    birthmonth = int(input("what month were you born in number form: "))
    birthday = int(input("day of month you were born: "))
    birthyear = int(input("what year were you born: "))
    age_month = (month - birthmonth)
    age_day = (day - birthday)
    age_year = (year - birthyear)
    if (month, day) < (birthmonth, birthday):
        age_year -= 1
    if age_month < 0:
        age_month += 12

    if age_day < 0:
        age_month -= 1
        age_day += 30
    print("your age is", age_year, "years ", age_month, "months ", age_day, "days" )


calc()

#count vowels
def count():
    word = str(input("input a word: "))
    vowels = ["a", "e", "i","o", "u", "A", "E", "I", "O", "U"]
    counter = 0
    for char in word:
        if char in vowels:
            counter += 1
    print("the word ", word, "has", counter, "vowels")
count()







   
    


