/* First Line:  Size of array
 * Second Line:  N ints (array elements)
 * Macro creates:  Result = #
 */

#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    using namespace std;

    int size;
    vector<int> v;
    int diffelm;

    cin >> size;
    v.resize(size);

    for (auto& i: v) {
        cin >> i;
    }

    auto minelm = min_element(v.begin(), v.end());
    auto maxelm = max_element(v.begin(), v.end());

    diffelm = *maxelm - *minelm;


    cout << "Result = " << diffelm << '\n';

    return 0;
}

