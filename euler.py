import math
from matplotlib import pyplot

def equation1():
    f = lambda t,y: t*y
    return f

def equation2():
    f = lambda t,y: y*(1+(t**2))
    return f

def equation3():
    f = lambda t,y: (49/5) - ((3*y)/20)
    return f

def equation4():
    f = lambda t,y: t+1+(1/t)-((2*y)/t)
    return f

def equation5():
    f = lambda t,V: (-1400) + (t*math.exp(-t)) - (V/0.05)
    return f

def equation6():
    f = lambda t,V: (-1360) + (math.exp(-t/(0.03))) - (math.exp(-t/(0.04)))- (V/0.05)
    return f

def Euler(f, t0, tf, y0, n):
    h = (tf -t0)/n

    t = []
    y = []

    t.append(t0)
    y.append(y0)

    for i in range(n+1):
        tx = t[i]+h
        t.append(tx)

        y1 = y[i]+(h*(f(t[i], y[i])))
        y.append(y1)

    for j in range(n+1):
        print("%0.1f %f"%(t[j], y[j]))

    pyplot.plot(t, y, 0)
    pyplot.xlabel("Value of t")
    pyplot.ylabel("Value of y")
    pyplot.title("Approximate Solutions of IVPs using Euler's Method")
    pyplot.show()

    return

def main():
    try:
            print("\n 1: dy/dt = yt\n 2: dy/dt=y(1+t^2)\n 3: dy/dt = 9.8 - 0.15y\n 4: t(dy/dt) + 2y = t^2-t+1\n 5: dV/dt + (1/0.05)V = -1400 +te^-t\n 6: dV/dt + (1/0.05)V = -1360+e^(-t/0.03)-e(-t/0.04)\n")
            response = input("Please select a sample equation from the above options\nEnter number or enter 'q' to quit: ")

            while(response != "q"):

                response = int(response)

                a = float(input("\nPlease enter 't0': "))
                c = float(input("\nPlease enter 'y(t0)': "))
                b = float(input("\nPlease enter 'y(tfinal)': "))
                n = int(input("\nPlease enter 'Number of steps (n)': "))


                if(0<response<7):

                    if(response == 1):
                        Euler(equation1() , a, b, c, n)
                    elif(response == 2):
                        Euler(equation2() , a, b, c, n)
                    elif(response == 3):
                        Euler(equation3() , a, b, c, n) 
                    elif(response == 4):
                        Euler(equation4() , a, b, c, n)
                    elif(response == 5):
                        Euler(equation5() , a, b, c, n)
                    elif(response == 6):
                        Euler(equation6() , a, b, c, n)
                            
                else:
                    print("Wrong input")

                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                print("\n 1: dy/dt = yt\n 2: dy/dt=y(1+t^2)\n 3: dy/dt = 9.8 - 0.15y\n 4: t(dy/dt) + 2y = t^2-t+1\n 5: dV/dt + (1/0.05)V = -1400 +te^-t\n 6: dV/dt + (1/0.05)V = -1360+e^(-t/0.03)-e(-t/0.04)\n")
                response = input("Please select a sample equation from the above options\nEnter number or enter 'q' to quit: ")

    except ValueError:
        print("\nError: Invalid Input\n")

if __name__ == "__main__":
    main()