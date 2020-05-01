#include <iostream>
#include <memory>

class Rectangle {
protected:
    int m_width;
    int m_height;
public:
    Rectangle(int width=1, int height=1): m_width{width}, m_height{height} { }
    virtual ~Rectangle() = default;

    // virtual void display() {
    void display() {
        std::cout << m_width << ' ' << m_height << '\n';
    }
};

class RectangleArea: public Rectangle {
public:
    // void display() override {
    void display() {
        std::cout << m_width * m_height << '\n';
    }

    void read_input() {
        std::cin >> m_width >> m_height;
    }
};

int main() {
    std::unique_ptr<Rectangle> upr = std::make_unique<RectangleArea>();
    RectangleArea* raptr;

    raptr = dynamic_cast<RectangleArea*>(upr.get());
    if (raptr) {
        raptr->read_input();
    }
    upr->display();
    if (raptr) {
        raptr->display();
    }

    return 0;
}

