#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<int> reverse1(const vector<int>& v) {
    vector<int> v2;

    for (int i=v.size()-1; i>=0; --i)
        v2.push_back(v[i]);

    return v2;
}

void reverse2(vector<int>& v) {
    int end = v.size() - 1;

    for (int i=0; i<v.size()/2; ++i)
        swap(v[i], v[end-i]);
}

int main() {
    int amount {0}, num {0};
    vector<int> intarray;

    cin >> amount;
    for (int i=0; i<amount; ++i) {
        cin >> num;
        intarray.push_back(num);
    }

    // intarray = reverse1(intarray);
    reverse2(intarray);
    for (int i:intarray)
        cout << i << ' ';

    return 0;
}

