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
	ListNode* partition(ListNode* head, int x) {
		ListNode *dummyhead1 = new ListNode(0);
		ListNode *dummyhead2 = new ListNode(0);
		ListNode *p1 = dummyhead1;
		ListNode *p2 = dummyhead2;
		while(head){
			int val = head->val;
			if(val < x){
				p1->next = head;
				p1 = p1->next;
			}
			else{
				p2->next = head;
				p2 = p2->next;
			}
			head = head->next;
		}
		p1->next = dummyhead2->next;
		p2->next = NULL;
		return dummyhead1->next;
	}
};