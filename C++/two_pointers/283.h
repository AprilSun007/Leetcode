//
// Created by Jinwen Sun on 9/5/20.
//

#ifndef TWO_POINTERS_283_H
#define TWO_POINTERS_283_H

#endif //C___283_H
#include <vector>
using namespace std;
class Solution_283 {
public:
    static void moveZeroes(vector<int>& nums) {

        int i = 0;
        int j = 0;

        while(j < nums.size() ) {
            if (nums[j] != 0) {
                nums[i] = nums[j];
                i++;
            }
            j++;
        }

        while(i < nums.size()){
            nums[i] = 0;
            i++;
        }
    }
};