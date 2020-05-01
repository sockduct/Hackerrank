#include <cmath>
#include <iomanip>
#include <iostream>

int main() {
    int testcases;
    double a, b, c;

    using namespace std;
    using bigint = long long int;

    cin >> testcases;
	cout << setiosflags(ios::uppercase);
	cout << setw(0xf) << internal;

    for (auto i = 0; i < testcases; ++i) {
        cin >> a >> b >> c;

        cout << setprecision(0) << showbase << nouppercase << left
                << hex << static_cast<bigint>(a) << '\n'
             << setprecision(2) << showpos << right << setfill('_')
                << fixed << setw(15) << b << '\n'
             << setprecision(9) << scientific << uppercase << noshowpos
                << c << '\n';
    }

    return 0;
}

