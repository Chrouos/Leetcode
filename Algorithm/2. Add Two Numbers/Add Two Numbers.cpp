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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *temp1 = l1, *temp2 = l2, *first = new ListNode(),
                 *prev = new ListNode();

        bool carry = false, isFirst = true;  //是否進位
        while (temp1 != nullptr || temp2 != nullptr || carry) {
            int addNum = 0;

            if (temp1 != nullptr && temp2 != nullptr) {
                addNum = temp1->val + temp2->val;
                temp1 = temp1->next;
                temp2 = temp2->next;

            } else if (temp1 == nullptr && temp2 != nullptr) {
                addNum = temp2->val;
                temp2 = temp2->next;
            } else if (temp1 != nullptr && temp2 == nullptr) {
                addNum = temp1->val;
                temp1 = temp1->next;
            }

            if (carry) {
                carry = false;
                addNum++;
            }

            //假設大於 10
            if (addNum / 10) {
                carry = true;
                addNum %= 10;
            }

            if (isFirst) {
                first = new ListNode(addNum);
                prev = first;
                isFirst = false;
            } else {
                ListNode* newNode = new ListNode(addNum);
                prev->next = newNode;
                prev = newNode;
            }
        }

        return first;
    }
};