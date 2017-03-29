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
	ListNode* deleteDuplicates(ListNode* head) {
		ListNode *dummyhead = new ListNode(-1);
		if (!head)
			return NULL;
		dummyhead->next = head;
		ListNode *p1 = dummyhead;
		ListNode *p2 = head->next;
		while(p2)
		{
			if(p1->next->val != p2->val){
				p1 = p1->next;
				p2 = p2->next;
			}
			else{
				while(p2 && p1->next->val == p2->val)
					p2 = p2->next;
				p1->next = p2;
				if(p2)
					p2 = p2->next;
			}
		}
		return dummyhead->next;
	}
};