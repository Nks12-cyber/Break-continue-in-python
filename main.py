# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
user = int(input('enter any number '))
while True:
    
    if user<=100:
        user = int(input('enter any number '))
        continue
    if user>100:
        print("congo! you entered a number which is grater than 100")
        break
