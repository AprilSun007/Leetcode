//
// Created by Jinwen Sun on 9/7/20.
//

#ifndef TWO_POINTERS_142_H
#define TWO_POINTERS_142_H
#include <cstddef>
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
    };

class Solution_142 {
public:
    ListNode* detectCycle(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return NULL;
        }
        ListNode* i = head;
        ListNode* j = head;
        ListNode* z = head;

        while(j != NULL && j->next != NULL){
            i = i->next;
            j = j->next->next;
            if(i == j){
                break;
            }
        }

        if(j == NULL || j->next == NULL){
            return NULL;
        }
        while(z != i){
            i = i->next;
            z = z->next;
        }
        return i;

    }
};
#endif //TWO_POINTERS_142_H
