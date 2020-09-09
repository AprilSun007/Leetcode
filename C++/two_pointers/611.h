//
// Created by Jinwen Sun on 9/8/20.
//

#ifndef TWO_POINTERS_611_H
#define TWO_POINTERS_611_H
#include <vector>
using namespace std;
class Solution_611 {
public:
    static int triangleNumber(vector<int>& nums) {
        if(nums.size() < 3){
            return 0;
        }
        sort(nums.begin(), nums.end());
        int cnt = 0;
        for(int strt = 0; strt < nums.size() - 2; strt++){
            int i = strt + 1;
            int j = strt + 2;
            while(i < nums.size()-1){
                while(j < nums.size() && nums[strt]+nums[i] < nums[j]){
                    j++;
                }
                cnt += max(0, j-i-1);
                i++;
            }
        }

    }
};
#endif //TWO_POINTERS_611_H
