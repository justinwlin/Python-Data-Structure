import math

def e_approx(x):
    e=0
    for i in range(0, x): #From 0, to the range of x...
        e = e + (1 / math.factorial(i)) #Add to e... 1 / factorial i... the number of terms depending from x
    return e


def main():
    for n in range(3):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)

main()