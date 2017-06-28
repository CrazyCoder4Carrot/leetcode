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
    ListNode* sortList(ListNode* head) {
    	return mergeSort(head);
    }
    ListNode *mergeSort(ListNode *head){
    	if(!head || !head->next)
    		return head;
    	ListNode *dummyhead = new ListNode(0);
    	dummyhead->next = head;
    	ListNode *slow = dummyhead, *fast = dummyhead;
    	while(fast && fast->next){
    		slow = slow->next;
    		fast = fast->next->next;
    	}
    	ListNode *second = slow->next;
    	slow->next = NULL;
    	ListNode *l1 = mergeSort(head);
    	ListNode *l2 = mergeSort(second);
    	return merge(l1, l2);

    }
    ListNode *merge(ListNode *l1, ListNode *l2){
    	ListNode *dummyhead = new ListNode(0);
    	ListNode *ptr = dummyhead;
    	while(l1 && l2){
    		if(l1->val < l2->val){
    			ptr->next = l1; 
    			l1 = l1->next;
    		}
    		else{
    			ptr->next = l2;
    			l2 = l2->next;
    		}
    		ptr = ptr->next;
    	}
    	ptr->next = l1?l1:l2;
    	ListNode *res = dummyhead->next;
    	delete dummyhead;
    	return res;
    }
};