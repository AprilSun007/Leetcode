//
// Created by Jinwen Sun on 9/6/20.
//

#ifndef TWO_POINTERS_633_H
#define TWO_POINTERS_633_H
#include <math.h>
using namespace std;
class Solution_633 {
public:
    bool judgeSquareSum(int c) {
        long j = round(sqrt(c));
        long i = 0;

        while(i <= j){
            if (i*i + j*j > c){
                j--;
            }else if(i*i + j*j < c){
                i++;
            }else{
                return true;
            }
        }

        return false;

    }
};

#endif //TWO_POINTERS_633_H
