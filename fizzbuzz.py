total=0
for number in range(1,101):
    total+=number

    if number %3==0  and number%5==0:
        print("fizz buzz")
    elif number%3==0:
        print("fizz")
        
    elif number %5==0:
        print("buzz")
     
    else: 
        print(number)
    