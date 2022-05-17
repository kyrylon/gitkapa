print ("Hello there")

T = input ("Do you wanna play with numbers? (Y/N)")

if T == "Y":
    
    a = float (input ("Choose the number a:"))

    b = float (input ("Choose the number b:"))

    c = input ("Do you wanna know the sum of these numbers? (Y/N)")

    d = a+b

    l = a-b
    if c == "Y":
        print ("The  Sum of a and b is", d)
    else:
        print ("What do you want then?\n" "Maybe other operations?")

else:
    print ("Sorry then. Goodbye as i cannot do anything else yet!")

