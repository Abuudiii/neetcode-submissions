/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        map<Node*, Node*> nodeMap;
        Node* curr = head;
        nodeMap[NULL] = NULL;

        // Populating map with copies
        while (curr) {
            nodeMap[curr] = new Node(curr->val);
            curr = curr->next;
        }

        curr = head;

        // Build new list
        while (curr) {
            Node* copiedNode = nodeMap[curr];

            // Building list
            copiedNode->next = nodeMap[curr->next];
            copiedNode->random = nodeMap[curr->random];

            // Iterate
            curr = curr->next;
        }

        return nodeMap[head];
    }
};
















