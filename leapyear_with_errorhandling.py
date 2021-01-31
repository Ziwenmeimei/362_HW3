#function to check a year as leap or not
def isLeap(y):
    if(y%4) == 0: #check divisible by 4
        if(y%100) == 0: #check divisible by 100
            if(y%400) == 0: #check divisible by 400
                return True #return true
            else:
                return False #return false
        else:
            return True #return true
    else:
        return False #return False

try:
    #input the year
    y = (int)(input("Enter the year: "))
    if(isLeap(y)): #call isLeap() method to check a year as leap or not
        print("Leap year") #print leap year
    else:
        print("Not leap year") #print not leap year
except ValueError:
    print("This is not a year. Try to run the program again.")