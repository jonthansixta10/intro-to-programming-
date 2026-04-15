def get_number():
    n = input("enter a whole number\n->")
    try:
          n = int(n)
    except:
         print("you entered a word, please enter a number")
         get_number()      
    return n 

def divide(x):
    try:
           return 100 / x
    except:
         print("cannot divide by zero")     
         




num = get_number()
print(divide(num))

