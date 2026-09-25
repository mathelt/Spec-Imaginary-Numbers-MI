import matplotlib.pyplot as plt

isBounded = 0
zNought = 0
zN = zNought

realPart = 0.6
complexPart = 0.4j
c = realPart + complexPart
print(c)

x = []
y = []


# iteratively calculate the next term of z_n and determine if the modulus exceeds two, returning whether it is bounded or not.
def CalculateZn1(zN, c, isBounded, iterations):
    i = 1
    while i <= (iterations) and isBounded != 1:
        Zn1 = (zN**2) + c
        zN = Zn1
        modulus = (Zn1.real**2) + (Zn1.imag**2)
        if modulus > 4:
            isBounded = 1
        #print(i , ", " ,isBounded)
        i = i+1
    return zN, isBounded

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

    return x, y

def createBoundedArray(x,y):
    a = 0
    boundedArray = []
    boundedReal = []
    boundedImaginary = []
    for i in range(len(y)):
        for i in range(len(x)):
            #Imaginary number issue
            complexNumber = complex(x[i], y[a])
            z, isBounded = CalculateZn1(0, complexNumber, 0, 100)
            if isBounded == True:
                boundedArray.append(complexNumber)
                boundedReal.append(x[i])
                boundedImaginary.append(y[a])

        a = a+1
    #print(boundedReal)
    #print(boundedImaginary)
    #print(boundedArray)
    return boundedReal, boundedImaginary


def createGraphMandelbrot(RealComponent, ImaginaryComponent):
    # define the coordinates
    x = RealComponent
    y = ImaginaryComponent

    #create the graph
    plt.scatter(x,y)

    #Format the graph
    plt.title("Mandlebrot Set Graph")
    plt.xlabel("Real Component")
    plt.ylabel("Imaginary Component")

    #Display the chart
    plt.savefig('Mandelbrot Graph')
    plt.show()


#program run
#print(CalculateZn1(0, c, 0, 20))

x, y = testNumberGenerator()
boundedReal, boundedImaginary = createBoundedArray(x,y)
createGraphMandelbrot(boundedReal, boundedImaginary)