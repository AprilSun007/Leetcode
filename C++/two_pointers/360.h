//
// Created by Jinwen Sun on 9/5/20.
//

#ifndef TWO_POINTERS_360_H
#define TWO_POINTERS_360_H
#include <vector>
#include <stdlib.h>
using namespace std;
class Solution_360{
public:
    static vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
        vector<int> res(nums.size());
        int i = 0;
        int j = nums.size() - 1;
        if(a > 0){
            int index = nums.size() - 1;
            while(i <= j){
                if(transform(nums[i], a, b, c) > transform(nums[j], a, b, c)){
                    res[index--] = transform(nums[i], a, b, c);
                    i++;
                }else{
                    res[index--] = transform(nums[j], a, b, c);
                    j--;
                }
            }

        }else{

            while(i < j){
                if(transform(nums[i], a, b, c) > transform(nums[j], a, b, c)){
                    res.push_back(transform(nums[i], a, b, c));
                    i++;
                }else{
                    res.push_back( transform(nums[j], a, b, c));
                    j--;
                }
            }


        }

        return res;

    }

    static int transform(const int num, const int a, const int b, const int c){
        return a*num*num + b*num + c;
    }


};

#endif //TWO_POINTERS_360_H
