//
// Created by Jinwen Sun on 9/6/20.
//

#ifndef TWO_POINTERS_80_H
#define TWO_POINTERS_80_H
#include <vector>
using namespace std;
class Solution_80 {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        int j = 1;
        int cnt = 1;
        while (j < nums.size() ){
            if(nums[i] == nums[j]){
                if(cnt == 1){
                    nums[i+1] = nums[j];
                    i++;
                    j++;
                    cnt = 2;
                }else if (cnt == 2){
                    j++;
                }
            }
            else{
                nums[i+1] = nums[j];
                i++;
                j++;
                cnt = 1;
            }
        }

        return (i+1);

    }
};


#endif //TWO_POINTERS_80_H
