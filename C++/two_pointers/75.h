//
// Created by Jinwen Sun on 9/6/20.
//

#ifndef TWO_POINTERS_75_H
#define TWO_POINTERS_75_H
#include <vector>
using namespace std;
class Solution_75{
public:
    static void  sortColors(vector<int>& nums) {
        int i = 0;
        int j = nums.size() -1;
        int index = 0;

        while((index < j) && (i < j) ){
            if(nums[index] == 0){
                nums[index] = nums[i];
                nums[i] = 0;
                index ++;
                i++;
            } else if (nums[index] == 2){
                nums[index] = nums[j];
                nums[j] = 2;
                // note here index is not incremented!
                j --;

            }else{
                index ++;
            }
        }

    }

};

#endif //TWO_POINTERS_75_H
