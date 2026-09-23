/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode();
        ListNode* currHead = dummy;

        while (list1 && list2) {
            if (list1->val < list2->val) {
                currHead->next = list1;
                currHead = list1;
                list1 = list1->next;

            } else if (list1->val > list2->val) {
                currHead->next = list2;
                currHead = list2;
                list2 = list2->next;

            } else {
                currHead->next = list1;
                currHead = list1;
                list1 = list1->next;

            }
        }

        if (list1) {
            currHead->next = list1;
        } else if (list2) {
            currHead->next = list2;
        }

        return dummy->next;
    }
};
