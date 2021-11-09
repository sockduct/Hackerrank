#include <chrono>
#include <iomanip>
#include <iostream>
#include <locale>
#include <tuple>
#include <vector>

// Long in MSVC same as int, for 10e9 need long long int:
using bigint = long long int;
using qvec = std::vector<std::tuple<int, int, bigint>>;

bigint arrmanip(int n, qvec queries) {
    auto beginfunc = std::chrono::high_resolution_clock::now();
    std::vector<bigint> arr(n, 0);
    bigint maxval = 0;

    // Iterate through array and perform requested operations...
    for (const auto& [left, right, inc]: queries) {
        for (bigint i = left - 1; i < right; ++i) {
            arr[i] += inc;
        }
    }

    auto endfunc = std::chrono::high_resolution_clock::now();
    auto funcdur = std::chrono::duration_cast<std::chrono::microseconds>(endfunc - beginfunc);
    std::cout << "Completed array manipulation in " << funcdur.count() << " microseconds\n";

    for (const auto& i: arr) {
        if (i > maxval) {
            maxval = i;
        }
    }

    endfunc = std::chrono::high_resolution_clock::now();
    funcdur = std::chrono::duration_cast<std::chrono::microseconds>(endfunc - beginfunc);
    std::cout << "Found array maximum value in " << funcdur.count() << " microseconds\n";

    return maxval;
}

int main() {
    auto beginfunc = std::chrono::high_resolution_clock::now();
    int n, m;
    qvec queries;
    int a, b;
    bigint k, res;

    std::cin >> n >> m;
    for (int line = 0; line < m; ++line) {
        std::cin >> a >> b >> k;
        queries.push_back(std::make_tuple(a, b, k));
    }
    auto endfunc = std::chrono::high_resolution_clock::now();
    auto funcdur = std::chrono::duration_cast<std::chrono::microseconds>(endfunc - beginfunc);

    std::cout.imbue(std::locale(""));
    std::cout << "Read in queries in " << funcdur.count() << " microseconds\n";
    res = arrmanip(n, queries);
    std::cout << std::fixed << res << "\n";
}
