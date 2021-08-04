import cmath
from pathlib import Path
import sys


class Complex:
    def __init__(self, real=0.0, imag=0.0):
        # Don't use _real/_imag, model Python class which uses real/imag:
        self.real = real
        self.imag = imag

    def __repr__(self):
        # Note - could also use j instead of i
        return f'<{self.real:-.2f}, {self.imag:-.2f}i>'

    def __str__(self):
        # Note - could also use j instead of i
        return f'{self.real:-.2f}{self.imag:+.2f}i'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        '''(a1 + b1i) * (a2 + b2i) = (a1a2 - b1b2) + (a1b2 + a2b1)i'''
        new_real = (self.real * other.real) - (self.imag * other.imag)
        new_imag = (self.real * other.imag) + (self.imag * other.real)
        return Complex(new_real, new_imag)

    def __truediv__(self, other):
        '''(a1 + b1i)/(a2 + b2i) =
           (a1a2 + b1b2)/(a2^2 + b2^2) + (a2b1 - a1b2)i/(a2^2 + b2^2)'''
        new_real = ((self.real * other.real) + (self.imag * other.imag))/(
                    other.real**2 + other.imag**2)
        new_imag = ((other.real * self.imag) - (self.real * other.imag))/(
                    other.real**2 + other.imag**2)
        return Complex(new_real, new_imag)

    # Note:  Concept difference
    # * The modulus for complex numbers is their absolute value or distance from the origin
    # * This is not the same for integers/real numbers where it's the remainder
    def __mod__(self, other):
        if other is not self:
            raise ValueError(f'Both arguments to mod must be the same object for complex numbers')
        return self.mod()

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def mod(self):
        # This is the modulus:
        # return (self.real**2 + self.imag**2)**(0.5)
        # But, challenge wants this formatted as a complex number - doesn't
        # really make sense, but that's the ask...
        return Complex((self.real**2 + self.imag**2)**(0.5))


def complex_print(n):
    print(f'{n.real:-.2f}{n.imag:+.2f}i')


def complex_mod(n):
    return (n.real**2 + n.imag**2)**(0.5)


def complex_builtins(a, b, c, d):
    complex1 = complex(a, b)
    complex2 = complex(c, d)

    complex_print(complex1 + complex2)
    complex_print(complex1 - complex2)
    complex_print(complex1 * complex2)
    complex_print(complex1 / complex2)

    complex_print(complex(complex_mod(complex1), 0))
    complex_print(complex(complex_mod(complex2), 0))


def complex_class(a, b, c, d):
    complex1 = Complex(a, b)
    complex2 = Complex(c, d)

    print(complex1 + complex2)
    print(complex1 - complex2)
    print(complex1 * complex2)
    print(complex1 / complex2)

    print(Complex((complex1 % complex1), 0))
    print(Complex((complex2 % complex2), 0))


def test_complex_class(a, b, c, d):
    complex1 = complex(a, b)
    complex2 = complex(c, d)
    complex3 = Complex(a, b)
    complex4 = Complex(c, d)

    print(f'Testing using {a}, {b}i and {c}, {d}i:\n')

    print(f'Adding {a}, {b}i and {c}, {d}i...')
    assert (complex1 + complex2).real == (complex3 + complex4).real
    assert (complex1 + complex2).imag == (complex3 + complex4).imag
    print(f'Subtracting {a}, {b}i and {c}, {d}i...')
    assert (complex1 - complex2).real == (complex3 - complex4).real
    assert (complex1 - complex2).imag == (complex3 - complex4).imag
    print(f'Multipying {a}, {b}i and {c}, {d}i...')
    assert (complex1 * complex2).real == (complex3 * complex4).real
    assert (complex1 * complex2).imag == (complex3 * complex4).imag
    print(f'Dividing {a}, {b}i and {c}, {d}i...')
    assert cmath.isclose((complex1/complex2).real, (complex3/complex4).real)
    assert cmath.isclose((complex1/complex2).imag, (complex3/complex4).imag)
    print(f'Modulus of {a}, {b}i...')
    assert complex_mod(complex1) == (complex3 % complex3)
    assert complex_mod(complex1) == (complex3 % complex3)
    print(f'Alternate modulus of {a}, {b}i...')
    assert complex_mod(complex1) == complex3.mod()
    print(f'Modulus of {c}, {d}i...')
    assert complex_mod(complex2) == (complex4 % complex4)
    print(f'Alternate modulus of {c}, {d}i...')
    assert complex_mod(complex2) == complex4.mod()

    print(f'\nAll tests passed!')


def main(args):
    if len(args) == 5:
        a = int(args[1])
        b = int(args[2])
        c = int(args[3])
        d = int(args[4])

        test_complex_class(a, b, c, d)
        return 0
    elif len(args) == 1:
        a, b = [int(i) for i in input().split()]
        c, d = [int(i) for i in input().split()]
    else:
        print(f'Usage:  {Path(args[0]).name}  [n1 n2 n3 n4]')
        sys.exit(1)

    '''
    # I like this approach from Hackerrank to read in the Complex numbers and
    # define them - more elegant then mine.  The print is also interesting.
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
    '''

    complex_builtins(a, b, c, d)
    print('=' * 72)
    complex_class(a, b, c, d)


if __name__ == '__main__':
    main(sys.argv)
