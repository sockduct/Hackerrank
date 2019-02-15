/*
 * James Small, 02/15/2019
 * My solution for HackerRank Challenge:
 * Practice, C++, Introduction, Basic Data Types
 */
// First two needed for C++
#include <iomanip>
#include <iostream>
// This one needed for scanf/printf
#include <cstdio>

using namespace std;

int main() {
    // Complete the code.
    // Input:  int, long, char, float, and double
    int a;
    // Hackerrank used long int, but this doesn't work with
    // Visual Studio (C++) 2017
    long long int b;
    char c;
    float d;
    double e;

    // Using C++ style:
    // Could also enable commas with:
    // cout.imbue(locale("en_US.utf8"));
    // Comment this section out by changing // to /* ... */
    //
    cin >> a >> b >> c >> d >> e;
    cout << a << '\n' << b << '\n' << c << '\n' << fixed
         << setprecision(3) << d << '\n' << setprecision(9)
         << e << '\n';
    //
    
    // Alternatively using C style:
    // Enable this section by commenting out C++ style and
    // changing /* ... */ to //
    /*
    // Hackerrank used %ld to match up with long int
    // Per our adjustment above must use %lld
    scanf("%d %lld %c %f %lf", &a, &b, &c, &d, &e);
    printf("%d\n%lld\n%c\n%.3f\n%.9lf\n", a, b, c, d, e);
    */

    return 0;
}

