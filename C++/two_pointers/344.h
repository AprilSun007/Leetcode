//
// Created by Jinwen Sun on 9/7/20.
//

#ifndef TWO_POINTERS_344_H
#define TWO_POINTERS_344_H
#include <vector>
using namespace std;
class Solution_344 {
public:
    void reverseString(vector<char>& s) {
        if(s.size() > 0){
            auto i = s.begin();
            auto j = s.end() - 1;
            while(i < j){
                swap(*i, *j);
                i++;
                j--;
            }
        }

    }
};

#endif //TWO_POINTERS_344_H
