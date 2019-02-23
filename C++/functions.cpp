#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

// Add `int max_of_four(int a, int b, int c, int d)` here.
int max_of_four(int a, int b, int c, int d) {
    vector<int> nums {a, b, c, d};
    // max_element returns an iterator which we use to access
    // the appropriate vector value:
    return *max_element(begin(nums), end(nums));

    /* Solution from HackerRank Editorial:
       return max(max(a,b), max(c,d));
    */
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

