import matplotlib.pyplot as plt
import csv

x = []
y = []
c = 0.355 + 0.355j

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

def createBoundedArray(x,y,c):
    a = 0
    boundedArray = []
    boundedReal = []
    boundedImaginary = []
    for i in range(len(y)):
        for i in range(len(x)):
            #Imaginary number issue
            complexNumber = complex(x[i], y[a])
            zN, isBounded = CalculateZn1(complexNumber, c, 0, 25)
            if isBounded == 0:
                boundedArray.append(complexNumber)
                boundedReal.append(x[i])
                boundedImaginary.append(y[a])

                boundedArray = [str(x) for x in boundedArray]

                componentArray = [[boundedReal[i], boundedImaginary[i]] for i in range(len(boundedReal))]
                
                # data = boundedArray # [boundedReal, boundedImaginary]
                #Adding the complex numbers to a csv
                with open ('JuliaBoundComplex.csv', 'w', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(componentArray)

        a = a+1
    #print(boundedReal)
    #print(boundedImaginary)
    #print(boundedArray)
    return boundedReal, boundedImaginary


def createGraphJulia(RealComponent, ImaginaryComponent):
    # define the coordinates
    x = RealComponent
    y = ImaginaryComponent

    #create the graph
    plt.scatter(x,y,s=1)

    #Format the graph
    plt.title("Julia Set Graph")
    plt.xlabel("Real Component")
    plt.ylabel("Imaginary Component")

    #Display the chart
    plt.savefig('Julia Graph')
    plt.show()



x, y = testNumberGenerator()
boundedReal, boundedImaginary = createBoundedArray(x,y, 0.355+0.355j)
createGraphJulia(boundedReal, boundedImaginary)

print(len(boundedReal), len(boundedImaginary))