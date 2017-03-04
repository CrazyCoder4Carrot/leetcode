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
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL)
            return NULL;
        if(head->next == NULL)
            return head;
        ListNode *dummyhead = new ListNode(0);
        dummyhead->next = head;
        ListNode *ptr = dummyhead;
        while(ptr)
        {
            cout<<ptr->val<<" ";
            ptr = ptr->next;
        }
        ListNode *ptr1 = dummyhead;
        ListNode *ptr2 = head;
        ListNode *ptr3 = ptr2->next;
        cout<<head->next<<endl;
        while(ptr1 && ptr2 && ptr3)
        {
            ptr1->next = ptr3;
            ptr2->next = ptr3->next;
            ptr3->next = ptr2;
            ptr1 = ptr2;
            ptr2 = ptr2->next;
            ptr3 = ptr2? ptr2->next : NULL;
        }
        return dummyhead->next;
    }
};