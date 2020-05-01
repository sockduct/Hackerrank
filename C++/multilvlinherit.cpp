#include <iostream>

class Triangle {
public:
    void triangle() {
        std::cout << "I am a triangle\n";
    }
};

class Isosceles: public Triangle {
public:
    void isosceles() {
        std::cout << "I am an isosceles triangle\n";
    }
};

class Equilateral: public Isosceles {
public:
    void equilateral() {
        std::cout << "I am an equilateral triangle\n";
    }
};

int main() {
    Equilateral eql;

    eql.equilateral();
    // eql.isosceles();
    eql.Isosceles::isosceles();
    // eql.triangle();
    eql.Triangle::triangle();

    return 0;
}

