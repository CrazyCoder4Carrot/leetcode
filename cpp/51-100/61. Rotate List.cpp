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
	ListNode* rotateRight(ListNode* head, int k) {
		if(!head)
			return NULL;
		int length = 0;
		ListNode *ptr = head;
		while(ptr){
			ptr = ptr->next;
			length ++;
		}
		k = k % length;
		ListNode *ptr1, *ptr2;
		ptr1 = ptr2 = head;
		while (k > 0) {
			ptr2 = ptr2->next;
			k--;
		}
		while (ptr2->next) {
			ptr1 = ptr1->next;
			ptr2 = ptr2->next;
		}
		ptr2->next = head;
		head = ptr1->next;
		ptr1->next = NULL;
		return head;

	}
};