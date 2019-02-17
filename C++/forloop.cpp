/*
 * James Small, 02/17/2019
 * My solution for HackerRank Challenge:
 * Practice, C++, Introduction, For Loop
 *
 * Tutorial:
 * for (<init-expr>; <exit-expr>; <update-expr>)
 *     <statement>;
 */
// Needed for C++ cin/cout
#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    // Complete the code.
    int a, b;
    map<int, string> digit = {{1, "one"}, {2, "two"}, {3, "three"},
                              {4, "four"}, {5, "five"}, {6, "six"},
                              {7, "seven"}, {8, "eight"}, {9, "nine"}};

    // Assuming valid input
    cin >> a >> b;

    // Input constrained to be positive integers (>= 0)
    for (int i = a; i <= b; ++i) {
        if (i <= 9)
            cout << digit[i] << '\n';
        else if (i % 2 == 0)
            cout << "even\n";
        else
            cout << "odd\n";
    }
    
    return 0;
}

