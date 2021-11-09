#include <iostream>

struct Complex {
    int a, b;

    explicit Complex(int ainit=0, int binit=0): a{ainit}, b{binit} { }
};

Complex operator+(const Complex& lhs, const Complex& rhs) {
    Complex result;

    result.a = lhs.a + rhs.a;
    result.b = lhs.b + rhs.b;

    return result;
}

std::ostream& operator<<(std::ostream& ostr, const Complex& c) {
    ostr << c.a << "+i" << c.b;
    return ostr;
}

std::istream& operator>>(std::istream& ostr, Complex& c) {
    ostr >> c.a;
    ostr.ignore(2);
    ostr >> c.b;

    return ostr;
}

int main() {
    Complex a, b, res;

    std::cin >> a >> b;
    res = a + b;
    std::cout << res << '\n';

    return 0;
}

