/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {      
        int carry = 0;
        ListNode *head = new ListNode(0);
        head->val = 0;
        ListNode *ptr = head;
        while(l1 || l2|| carry)
        {
            int l1val = l1?l1->val:0;
            int l2val = l2?l2->val:0;
            int temp = l1val + l2val + carry;
            ptr->next = new ListNode(temp%10);
            ptr = ptr->next;
            carry = temp/10;
            l1 = l1?l1->next:NULL;
            l2 = l2?l2->next:NULL;
        }
        return head->next;
    }
};