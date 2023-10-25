a=input("Please enter a: ")
b=input("Please enter b: ")
c=input("Please enter c: ")
while a>b:
    if b>c:
        print(a,b,c)
        break
    else:
        if a>c:
            print(a,c,b)
            break
        else:
            print(c,a,b)
            break
else:
    if b>c:
        if a>c:
            print(a,c,b)
        else:
            print(c,a,b)    
    else:
        print(c,b,a)
