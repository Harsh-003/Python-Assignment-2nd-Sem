#Assignment 4
#name: Harshveer Singh
#sid: 21107069
#branch: mechanical
print('Q1')
num = int(input("Hey user , enter any student's marks: "))
if num < 25:
  print("F")
elif num > 25 and num < 40:
  print("E")
elif num > 40 and num < 50:
  print("D")
elif num > 50 and num < 60:
  print("C")
elif num > 60 and num < 80:
  print("B")
elif num > 80:
  print("A")

print('Q2')
print("To check whether a year is a leap year or not ")
year = int(input("Hey User, Enter a year "))
if year % 4 ==0 and year % 100 != 0:
  print(" year is a leap year ")
elif year % 100 == 0:
  print(" Year is not a leap year ")
elif year % 400 == 0:
  print(" year is a leap year ")
else:
  print(" Year is not a leap year ")

print('Q3')
import random 

for i in range(1,11):
    a = random.randint(1,10)
    b = random.randint(1,10)
    ans = int(input(f'Question{i}:{a}x{b}='))
    if ans==a*b:
        print("Correct")
    else:
        print(" Incorrect. Correct answer is",a*b)

print('Q4')
for i in range(200):
    if i % 5 ==2 and i % 6 == 3 and i % 7 == 2:
        print(i)
