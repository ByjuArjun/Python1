
'''
characters = 0

introduce=input("Introduce yourself")

for i in introduce:
    characters = characters + 1
print(characters)
'''

'''
words = 1

introduce = input("Introduce yourself")

for i in introduce:
    if i == " ":
        words=words+1
print(words)
'''
'''
number = int(input("Give number"))

if number % 2 == 0:
    print("even")
else:
    print("odd")
'''

science = int(input("give science score"))
math = int(input('give math score'))
history = int(input("give history score"))
english = int(input("give english score"))


total = science + math + history + english
average = total/4
print(average)

if average >= 90:
    print("u are A")
elif average >=60 and average <90:
    print("B")
else:
    print("You fail(C)")

















