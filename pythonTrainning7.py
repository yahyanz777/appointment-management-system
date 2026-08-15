
try:
    x = int(input("Enter number     :   "))
    a=[i for i in range( x+1 )]
    print(a)
    for i in range(x+1):
       print(a[i]/(a[i]+1)) 
except NameError:
    print("Check your variables")
except IndexError:
    print("high index")
except ZeroDivisionError:
    print("Cannot be")
except ValueError:
    print("value")
except TypeError:
    print("Type")
except RuntimeError:
    print("something went wrong")
except Exception as e:
    print(e)
else :
    print("no errors")
finally:
    print("done ")
