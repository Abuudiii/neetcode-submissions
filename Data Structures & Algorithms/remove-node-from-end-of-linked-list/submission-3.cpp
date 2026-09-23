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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode();
        dummy->next = head;
        ListNode* prev = dummy;

        while (n) {
            head = head->next;
            n--;
        }

        while (head) {
            head = head->next;
            prev = prev->next;
        }

        prev->next = prev->next->next;
        return dummy->next;
    }
};
