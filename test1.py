name = input("Напишіть своє ім'я: ")
status = input("Хто ви по статусу: ")
age = int(input("Скільки тобі років:"))
if name == "Андрій":
    print("Привіт", name , "це ти")
else:
    print("Вибачь ти не той хто потрібен ((")

if status == "Інженер":
    print("Ваш статус:", status)
else:
    print("Ви не інженер")

if age < 18:
    print("Ти ще малий для такого")
elif age == 18:
    print("Те що треба")
elif age > 18:
    print("Да ти вже ветеран")
else:
    print("Error")