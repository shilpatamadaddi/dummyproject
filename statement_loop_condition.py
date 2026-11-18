#statement
from email.contentmanager import raw_data_manager

age = 25
if age >= 21:
    print("eligibl for voting")
else:
    print("not eligible")

score = 100
if score >=90:
    print("A")
elif score >=75:
    print("B")
else:
    print("C")

#loop
for i in range(10):
    print(i)

name = "ram"
print(name)
for i in name:
    print(i)

#while condition
count = 0
while count <5:
    count += 1
    print(count)

#string
text = "hi shilpa"
print(len(text))
print(text.count("is"))
print(text.lower())
print(text.upper())
print(text.replace("shilpa", "tamadaddi"))
names = text.split(' ')
print(names)
print("hi" in text)

