def karatsuba_mult(numbers, numLength):
    a = numbers[0][0:2]      #Getting the values by slicing
    b = numbers[0][2:4]  
    c = numbers[1][0:2]
    d = numbers[1][2:4]

    """PreStep"""
    astring = ""        
    for i in a:              #Joining to the empty string in order to get necessary values next
        astring += str(i)
    resA = int(astring)

    bstring = ""
    for i in b:
        bstring += str(i)
    resB = int(bstring)

    cstring = ""
    for i in c:
        cstring += str(i)
    resC = int(cstring)

    dstring = ""
    for i in d:
        dstring += str(i)
    resD = int(dstring)

    """Main Steps"""
    func1 = (10**numLength)*(resA*resC)     #The Implementation of the "third grade" multiplication with the actual algorithm 
    func2 = (10**(numLength/2))*((resA*resD)+(resB*resC))
    func3 = resB*resD
    total = float(func1) + float(func2) + float(func3)
    
    return float(total)
    
numLength = int(input("numLength: "))           #Getting user input and splitting in order to iterate through the numbers
usIn = input("Numbers to multiply: ").split()
lst = []
for i in usIn:
    res = list(map(int, i))
    lst.append(res)


print(karatsuba_mult(lst, numLength))


