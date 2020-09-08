//
// Created by Jinwen Sun on 9/7/20.
//

#ifndef TWO_POINTERS_680_H
#define TWO_POINTERS_680_H
#include <string>
class Solution_680 {
public:
    static bool validPalindrome(string s) {
        return check(s, 0, 0, s.size()-1);
    }
private:
    static bool check(string s, int cnt, int i, int j){
        if(s.size() == 0){
            return true;
        }

        while(i < j){
            while((!isalnum(s[i])) && (i < j)){
                i++;
            }
            while((!isalnum(s[j])) && (i < j)){
                j--;
            }
            if(tolower(s[i]) == tolower(s[j])){
                i++;
                j--;
            }
            else {
                if (cnt == 1) {
                    return false;
                }
                else{
                    cnt ++;
                    return check(s, cnt, i+1, j) || check(s, cnt, i, j-1);

                }
            }
        }
        return true;
    }

};

#endif //TWO_POINTERS_680_H
