#include <iostream>
#include <memory>
#include <vector>

int main() {
    // std::vector<std::vector<int>*> vptr;
    // Use smart pointers:
    std::vector<std::unique_ptr<std::vector<int>>> vptr;
    int input;
    int arrays, queries;
    int cursize;
    int outerv, innerv;

    // Read in number of arrays and number of queries:
    std::cin >> arrays >> queries;

    // Iterate over array info, populate arrays:
    for (int i = 0; i < arrays; ++i) {
        // vptr.push_back(new std::vector<int>);
        // Use smart pointers:
        vptr.push_back(std::unique_ptr<std::vector<int>>(new std::vector<int>));
        std::cin >> cursize;
        for (int j = 0; j < cursize; ++j) {
            std::cin >> input;
            vptr[i]->push_back(input);
        }
    }

    // Iterate over query info and process:
    for (int i = 0; i < queries; ++i) {
        std::cin >> outerv >> innerv;
        std::cout << vptr[outerv]->at(innerv) << '\n';
    }

    // Cleanup:
    // Obviated with smart pointers:
    /*
    for (auto i: vptr)
        delete i;
    */

    return 0;
}

