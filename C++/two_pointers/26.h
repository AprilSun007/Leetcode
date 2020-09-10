//
// Created by Jinwen Sun on 9/6/20.
//

#ifndef TWO_POINTERS_26_H
#define TWO_POINTERS_26_H
#include <vector>
using namespace std;
class Solution_26{
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        int j = 1;
        while (j < nums.size() ){
            if(nums[i] == nums[j]){
                j++;
            }
            else{
                nums[i+1] = nums[j];
                i++;
                j++;

            }
        }

        return (i+1);

    }
};
#endif //TWO_POINTERS_26_H
