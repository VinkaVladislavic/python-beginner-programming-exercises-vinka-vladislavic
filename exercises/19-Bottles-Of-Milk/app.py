# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for i in range(99, -1, -1):
        if i > 2:
            print(str(i) + " bottles of milk on the wall, " + str(i) + " bottles of milk.")
            print("Take one down and pass it around, " + str(i-1) + " bottles of milk on the wall.")
        elif i == 2:
            print(str(i) + " bottles of milk on the wall, " + str(i) + " bottles of milk.")
            print("Take one down and pass it around, " + str(i-1) + " bottle of milk on the wall.")
        elif i == 1:
            print(str(i) + " bottle of milk on the wall, " + str(i) + " bottle of milk.")
            print("Take one down and pass it around, no more bottles of milk on the wall.")
        else:
            print("No more bottles of milk on the wall, no more bottles of milk.")
            print("Go to the store and buy some more, 99 bottles of milk on the wall.")
    
    return None

number_of_bottles()