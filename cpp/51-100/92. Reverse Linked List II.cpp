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
	ListNode* reverseBetween(ListNode* head, int m, int n) {
		ListNode *dummyhead = new ListNode(0);
		dummyhead->next = head;
		ListNode *p1, *p2;
		p1 = p2 = dummyhead;
		while (m > 1) {
			p1 = p1->next;
			m--;
		}
		while (n > 0) {
			p2 = p2->next;
			n--;
		}
		ListNode *p3 = p2->next;
		p2->next = NULL;
		ListNode *newtail = p1->next;
		p1->next = reverse(p1->next);
		newtail->next = p3;
		return dummyhead->next;
	}
	ListNode *reverse(ListNode *head) {
		if (!head->next)
			return head;
		ListNode *temp = head->next;
		ListNode *p = reverse(head->next);
		head->next = NULL;
		temp->next = head;
		return p;
	}
};