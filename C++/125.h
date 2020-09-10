//
// Created by Jinwen Sun on 9/7/20.
//

#ifndef TWO_POINTERS_125_H
#define TWO_POINTERS_125_H
#include<string>
#include<vector>
#include<locale>
using namespace std;
class Solution_125 {
public:
    static bool isPalindrome(string s) {
        if(s.size() == 0){
            return true;
        }
        auto i = s.begin();
        auto j = s.end()-1;
        while(i < j){
            while((!isalnum(*i)) && (i < j)){
                i++;
            }
            while((!isalnum(*j)) && (i < j)){
                j--;
            }
            if(tolower(*i) == tolower(*j)){
                i++;
                j--;
            }
            else{
                return false;
            }

        }
        return true;
    }
};

#endif //TWO_POINTERS_125_H
