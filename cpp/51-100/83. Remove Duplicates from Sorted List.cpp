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
		if (!head)
			return NULL;
		if (!head->next)
			return head;
		ListNode* p1 = head;
		ListNode* p2 = head->next;
		int val = p1->val;
		if (val == p2->val) {
			while (p2 && val == p2->val) {
				p2 = p2->next;
			}
		}
		head->next = deleteDuplicates(p2);
		return head;
	}
};