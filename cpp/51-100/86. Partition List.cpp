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
		ListNode *p2 = dummyhead1;
		ListNode *p3 = dummyhead2;
		while(head){
			int val = p1->next->val;
			if(val < x){
				p2->next = new ListNode(val);
				p2 = p2->next;
			}
			else{
				p3->next = new ListNode(val);
				p3 = p3->next;
			}
			head = head->next;
		}
		p2->next = dummyhead2->next;
		return dummyhead1->next;
	}
};