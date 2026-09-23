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

        while (curr) {
            // Populate Map
            nodeMap[curr] = new Node(curr->val);

            // Move Pointer
            curr = curr->next;
        }

        Node* secondCurr = head;

        while (secondCurr) {
            Node* copiedNode = nodeMap[secondCurr];

            copiedNode->next = nodeMap[secondCurr->next];
            copiedNode->random = nodeMap[secondCurr->random];
        
            secondCurr = secondCurr->next;
        }

        return nodeMap[head];

    }
};
