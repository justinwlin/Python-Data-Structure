'''
You will define a class to represent a polynomial

Represent a polynomial as a list of its coefficients as a data members

Element in the list represents the constant, while each of the next elements represents the coefficent of
the next power in polynomial

note, the length of the coefficient list = p(x) is 1 + deg(p) where deg(p) is the degree
of the polynomial p.

Ex. p(x) = 2x^4 - 9x^3 + 0x^2 + 7x + 3 is [3, 7, 0, -9, 2]

'''

class Polynomial:
#Constructor that takes a list as an input and initiates a polynomial with coefficient given in the list.

    def __init__(self, lst=None):

        self.lst = lst #[1,2,3,4]

        if lst is None:
            self.lst = [0]
    
    def __str__(self):
        if self.lst != [0]:
            polynomialReturn = "p(x) = "
            counter = len(self.lst)

            for i in reversed(self.lst):
                polynomialReturn += str(i)
                polynomialReturn += "x^"
                polynomialReturn += str(counter)

                polynomialReturn += " + "

                counter -= 1

            return polynomialReturn[:-2]
        else:
            return "p(x) = 0"



poly = Polynomial([1,-2,3,4])
print(poly)
