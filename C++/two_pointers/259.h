//
// Created by Jinwen Sun on 9/9/20.
//

#ifndef TWO_POINTERS_259_H
#define TWO_POINTERS_259_H
#include <vector>
using namespace std;
class Solution_259 {
public:
    static int threeSumSmaller(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int cnt = 0;
        for(int i= 0; i<nums.size(); i++){
            int j = i + 1;
            int k = nums.size() - 1;
            while(j < k){
                while(j < k && nums[i] + nums[j] + nums[k] >= target){
                    k--;
                }
                cnt += k-j;
                j++;
            }
        }
        return cnt;

    }
};
#endif //TWO_POINTERS_259_H
