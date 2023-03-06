
print("------------------------------------------")
print("---------Que numero es mayor--------------")
print("------------------------------------------")


# input

a = int(input("Digite el valor 1:" ))
b = int(input("Digite el valor 2: "))
c = int(input("Digite el valor 3: "))


# procesing


if (a>b) :
    if(a>c) :
        print("Mayor:  "+ str(a))
    else :
        print("Mayor: " + str(c))
else: 
    if(b>c) :
        print("mayor: " + str(b))
    else :
        print("mayor : " + str(c) )
        
    
    

