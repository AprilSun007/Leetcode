//
// Created by Jinwen Sun on 9/7/20.
//

#ifndef TWO_POINTERS_345_H
#define TWO_POINTERS_345_H
#include <string>
#include <vector>
using namespace std;
class Solution_345 {
public:
    static string reverseVowels(string s) {
        if (s.size() == 0){
            return s;
        }

        auto i = s.begin();
        auto j = s.end() - 1;

        vector<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        while(i < j){
            if(find(vowels.begin(), vowels.end(), *i) == vowels.end()){
                i++;
            }
            if(find(vowels.begin(), vowels.end(), *j) == vowels.end()){
                j--;
            }
            if(find(vowels.begin(), vowels.end(), *i) != vowels.end()  && find(vowels.begin(), vowels.end(), *j) != vowels.end()){
                swap(*i, *j);
                i++;
                j--;
            }
        }

        return s;

    }
};

#endif //TWO_POINTERS_345_H
