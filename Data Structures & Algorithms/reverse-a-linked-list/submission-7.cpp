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
    ListNode* reverseList(ListNode* head) {
        // Two pointers to iterate over list
        ListNode* curr = head;
        ListNode* prev = nullptr;

        while (curr) {
            // Reference to next node
            ListNode* next = curr->next;

            // Reverse link and iterate
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
};
