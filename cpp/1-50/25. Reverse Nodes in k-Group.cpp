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
	ListNode* reverseKGroup(ListNode* head, int k) {
		if (!head)
			return NULL;
		if (k <= 1)
			return head;
		ListNode *dummyhead = new ListNode(0);
		dummyhead->next = head;
		ListNode *left = dummyhead;
		ListNode *end = left;
		while (true)
		{
			int temp = k;
			ListNode *start = left->next;
			while (temp && left && end)
			{
				cout << temp << " " << end->val << endl;
				end = end->next;
				temp--;
			}
			if (end == NULL && temp >= 0)
				break;
			cout << temp << " " << endl;
			ListNode *right = end->next;
			end->next = NULL;
			reverse(start);
			left->next = end;
			start->next = right;
			if (!right)
				break;
			left = start;
			end = left;
			ListNode *ptr = dummyhead;
			while(ptr)
			{
				cout<<ptr->val<<" ";
				ptr = ptr->next;
			}
			cout<<"/n"<<endl;
		}
		return dummyhead->next;
	}
	ListNode *reverse(ListNode *cur)
	{
		if (!cur)
			return NULL;
		if (!cur->next)
			return cur;
		ListNode *next = cur->next;
		cur->next = NULL;
		ListNode *other = reverse(next);
		next->next = cur;
		return other;
	}
};