#include <iostream>
#include "283.h"
#include "360.h"

int main() {
    vector<int> nums = {-4,-2,2,4};
    int a = 1;
    int b = 3;
    int c = 5;
    vector<int> res = Solution_360::sortTransformedArray(nums, a, b, c);
    for (auto i = res.begin(); i < res.end(); i++){
        cout << *i << ',';
    }
}
