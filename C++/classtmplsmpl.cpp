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

using std::string;

// General templated class
template <typename T>
class AddElements {
private:
    T m_data;
public:
    AddElements(T data=T()): m_data{data} { }
    T add(T more_data) const { return m_data + more_data; }
};

// string specialization of above templated class:
template<>
class AddElements<string> {
private:
    string m_data;
public:
    AddElements(string data): m_data{data} { }
    string concatenate(string more_data) { return m_data + more_data; }
};


int main() {
    std::size_t lines;
    string line_types;
    int int1, int2;
    float float1, float2;
    string str1, str2;

    std::cin >> lines;

    for (size_t i = 0; i < lines; ++i) {
        std::cin >> line_types;
        if (line_types == "string") {
            std::cin >> str1 >> str2;
            AddElements<string> mycol_strs(str1);
            std::cout << mycol_strs.concatenate(str2) << '\n';
        } else if (line_types == "int") {
            std::cin >> int1 >> int2;
            AddElements<int> mycol_ints(int1);
            std::cout << mycol_ints.add(int2) << '\n';
        } else if (line_types == "float") {
            std::cin >> float1 >> float2;
            AddElements<float> mycol_floats(float1);
            std::cout << mycol_floats.add(float2) << '\n';
        } else {
            std::cout << "Error:  Unexpected type ``" << line_types << "''\n";
            return -1;
        }
    }

    return 0;
}

