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
        ListNode* currNode = head;
        ListNode* prevNode = nullptr;

        while (currNode) {
            // Reference to next node
            ListNode* next = currNode->next;

            // Unlink and iterate
            currNode->next = prevNode;
            prevNode = currNode;
            currNode = next;
        }

        return prevNode;
    }
};
