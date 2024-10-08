import random

def get_color(color_number=4):
    # Making sure is a number and not a string
    color_number = int(color_number)

    switcher = {
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    
    return switcher.get(color_number,"Invalid Color Number")

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌

def get_allStudentColors():
    example_color = get_color(1)
    students_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ✅ ↓ your loop here ↓ ✅
    for student in range(0,10):
        randomNumber = random.randint(0,3)
        chosenColor = get_color(randomNumber)
        students_array[student] = chosenColor
    return students_array

print(get_allStudentColors())
