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
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		ListNode *dummyhead = new ListNode(0);
		ListNode *ptr = dummyhead;
		while (l1 && l2)
		{
			if (l1->val < l2->val) {
				ptr->next = l1;
				l1 = l1->next;
			}
			else {
				ptr->next = l2;
				l2 = l2->next;
			}
			ptr = ptr->next;
		}
		ptr->next = l1 ? l1 : l2;
		return dummyhead->next;
	}
};