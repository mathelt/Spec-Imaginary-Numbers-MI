isBounded = 0
zNought = 0
zN = zNought

realPart = -2
complexPart = 0j
c = realPart + complexPart
print(c)

# iteratively calculate the next term of z_n and determine if the modulus exceeds two, returning whether it is bounded or not.
def CalculateZn1(zN, c, isBounded, iterations):
    i = 1
    while i <= (iterations) and isBounded != 1:
        Zn1 = (zN**2) + c
        zN = Zn1
        modulus = (Zn1.real**2) + (Zn1.imag**2)
        if modulus > 4:
            isBounded = 1
        print(i , ", " ,isBounded)
        i = i+1
    return zN

def testNumberGenerator():
    x = []
    y = []
    real = -2
    imaginary = -1.5
    
    while real <= 1:
        x.append(real)
        real = round((real + 0.01), 5)

    while imaginary <= 1:
        y.append(imaginary)
        imaginary = round((imaginary + 0.01), 5)

def createBoundedArray():
    #Test
    print()

#program run
print(CalculateZn1(0, c, 0, 20))
testNumberGenerator()