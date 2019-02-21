#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
    map<int,string> nums = {{1, "one"}, {2, "two"}, {3, "three"},
                            {4, "four"}, {5, "five"}, {6, "six"},
                            {7, "seven"}, {8, "eight"}, {9, "nine"}};
    int n;
    cin >> n;
    // std::numeric_limits::max - max value of type streamsize:
    // See: https://en.cppreference.com/w/cpp/types/numeric_limits/max
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Note - not checking for out of bounds input
    // Assumed to be [1-10^9]
    if (n >= 1 && n <= 9)
        cout << nums[n] << endl;
    else
        cout << "Greater than 9" << endl;

    return 0;
}

