#include <iostream>

// Box class
// Private Data:
// Dimensions length=l, breadth=b, height=h
class Box {
public:
    // Constructor:
    Box(int length=0, int breadth=0, int height=0):
        l{length}, b{breadth}, h{height} {}
    // Copy Constructor:
    Box(const Box& box):
        l{box.l}, b{box.b}, h{box.h} {}
    // Methods:
    int getLength() const { return l; }
    int getBreadth() const { return b; }
    int getHeight() const { return h; }
    long long CalculateVolume() const {
        return l * b * static_cast<long long>(h);
    }
    // External helpers:
    friend bool operator<(Box lhs, Box rhs);
    friend std::ostream& operator<<(std::ostream& ostr, const Box& box);
private:
    int l;
    int b;
    int h;
};


bool operator<(Box lhs, Box rhs) {
    // Not how I'd do it, but per specs:
    if (lhs.l < rhs.l) {
        return true;
    } else if (lhs.b < rhs.b && lhs.l == rhs.l) {
        return true;
    } else if (lhs.h < rhs.h && lhs.b == rhs.b && lhs.l == rhs.l) {
        return true;
    } else {
        return false;
    }
}

std::ostream& operator<<(std::ostream& ostr, const Box& box) {
    /* Specs call for no parenthesis or commas:
    ostr << '(' << box.getLength() << ", " << box.getBreadth()
         << ", " << box.getHeight() << ')';
    */
    ostr << box.getLength() << ' ' << box.getBreadth()
         << ' ' << box.getHeight();
    return ostr;
}

void test();
void test2();

int main() {
    test();
    test2();
}

void test() {
    Box box1 {1, 1, 1};
    Box box2 {3, 2, 8};
    Box box3 {2, 1, 9};
    Box box4;  // Test default initialization
    Box box5 = box3;  // Test copy constructor

    std::cout << "box1 < box2:  " << (box1 < box2) << '\n';
    std::cout << "box1 < box3:  " << (box1 < box3) << '\n';
    std::cout << "box1 < box5:  " << (box1 < box5) << '\n';
    std::cout << "box2 < box3:  " << (box2 < box3) << '\n';
    std::cout << "box2 < box5:  " << (box2 < box5) << '\n';
    std::cout << "box4 < box1:  " << (box4 < box1) << '\n';
    std::cout << "box1 volume:  " << box1.CalculateVolume() << '\n';
    std::cout << "box2 volume:  " << box2.CalculateVolume() << '\n';
    std::cout << "box3 volume:  " << box3.CalculateVolume() << '\n';
    std::cout << "box4 volume:  " << box4.CalculateVolume() << '\n';
    std::cout << "box5 volume:  " << box5.CalculateVolume() << '\n';
    std::cout << "box1:  " << box1 << '\n';
    std::cout << "box2:  " << box2 << '\n';
    std::cout << "box3:  " << box3 << '\n';
    std::cout << "box4:  " << box4 << '\n';
    std::cout << "box5:  " << box5 << '\n';
}

void test2() {
    using namespace std;

    int n;
	cin >> n;
	Box temp;

	for(int i = 0; i < n; i++) {
		int type;
		cin >> type;
		if (type == 1) {
			cout<<temp<<endl;
		}
		if (type == 2) {
			int l, b, h;
			cin >> l >> b >> h;
			Box NewBox(l, b, h);
			temp = NewBox;
			cout << temp << endl;
		}
		if (type == 3) {
			int l, b, h;
			cin >> l >> b >> h;
			Box NewBox(l, b, h);
			if(NewBox < temp) {
				cout << "Lesser\n";
			} else {
				cout << "Greater\n";
			}
		}
		if (type == 4) {
			cout << temp.CalculateVolume() << endl;
		}
		if (type == 5) {
			Box NewBox(temp);
			cout << NewBox << endl;
		}
	}
}