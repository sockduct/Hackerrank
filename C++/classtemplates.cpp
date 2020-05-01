/*
 * Given input:
 * - string = concat
 * - int|float = add
 * x Line 1:  n (int), how many additional lines
 * x Line n:  types (pair of ints|floats|strings)
 * 
 * Output:  Based on type use appropriate method
 *
 * Create template class AddElements with member add()
 * - create specialization for string with member concatentate()
 *
 */

#include <iostream>
#include <string>

// Forward declarations:
template <typename T> class AddElements;
template <typename T> std::istream& operator>>(std::istream&, AddElements<T>&);
template <typename T> std::ostream& operator<<(std::ostream&, const AddElements<T>&);

// General templated class
template <typename T>
class AddElements {
private:
    T m_first;
    T m_second;
public:
    AddElements(T first=T(), T second=T()): m_first{first}, m_second{second} { }
    T add() const { return m_first + m_second; }

    // Note:  AddElements cannot be const since sending values into it:
    friend std::istream& operator>> <>(std::istream&, AddElements&);
    /* Alternatively:
    // Use this and can eliminate forward declarations:
    friend std::istream& operator>>(std::istream& istr, AddElements& ae) {
        istr >> ae.m_first >> ae.m_second;
        return istr;
    }
     */
    // Note:  AddElements must be const here or won't work:
    friend std::ostream& operator<< <>(std::ostream&, const AddElements&);
};

template <typename T>
std::istream& operator>>(std::istream& istr, AddElements<T>& ae) {
    istr >> ae.m_first >> ae.m_second;
    return istr;
}

template <typename T>
std::ostream& operator<<(std::ostream& ostr, const AddElements<T>& ae) {
    ostr << ae.add();
    return ostr;
}

// string specialization of above templated class:
template<>
class AddElements<std::string> {
private:
    std::string m_first;
    std::string m_second;
public:
    std::string concatenate() const { return m_first + m_second; }

    friend std::istream& operator>> (std::istream&, AddElements&);
    friend std::ostream& operator<< (std::ostream&, const AddElements&);
};

std::istream& operator>>(std::istream& istr, AddElements<std::string>& ae) {
    istr >> ae.m_first >> ae.m_second;
    return istr;
}

std::ostream& operator<<(std::ostream& ostr, const AddElements<std::string>& ae) {
    ostr << ae.concatenate();
    return ostr;
}

int main() {
    std::size_t lines;
    std::string line_types;
    AddElements<int> mycol_ints;
    AddElements<float> mycol_floats;
    AddElements<std::string> mycol_strs;

    std::cin >> lines;

    for (size_t i = 0; i < lines; ++i) {
        std::cin >> line_types;
        if (line_types == "string") {
            std::cin >> mycol_strs;
            std::cout << mycol_strs << '\n';
        } else if (line_types == "int") {
            std::cin >> mycol_ints;
            std::cout << mycol_ints << '\n';
        } else if (line_types == "float") {
            std::cin >> mycol_floats;
            std::cout << mycol_floats << '\n';
        } else {
            std::cout << "Error:  Unexpected type ``" << line_types << "''\n";
            return -1;
        }
    }

    return 0;
}

