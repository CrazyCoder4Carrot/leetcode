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
    ListNode* insertionSortList(ListNode* head) {
        if (!head || !head->next)
            return head;
        ListNode *dummyhead = new ListNode(0);
        dummyhead->next = head;
        ListNode *ptr = head;
        int prevval = head->val;
        while (ptr && ptr->next) {
            if (ptr->next->val < prevval) {
                ListNode *tmp = dummyhead;
                while (tmp->next->val < ptr->next->val) {
                    tmp = tmp->next;
                }
                ListNode *target = ptr->next;
                ptr->next = ptr->next->next;
                target->next = tmp->next;
                tmp->next = target;
            }
            else {
                prevval = ptr->next->val;
                ptr = ptr->next;
            }
        }
        return dummyhead->next;
    }
};