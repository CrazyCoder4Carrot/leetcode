/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	TreeNode* sortedListToBST(ListNode* head) {
		return helper(head, NULL);
	}
	TreeNode* helper(ListNode *begin, ListNode *end){
		if(begin == end)
			return NULL;
		if(begin->next == end){
			TreeNode *root = new TreeNode(begin->val);
			return root;
		}
		ListNode *slow, *fast;
		slow = fast = begin;
		while(fast != end && fast->next != end){
			slow = slow->next;
			fast = fast->next->next;
		}
		ListNode *mid = slow;
		TreeNode *root = new TreeNode(mid->val);
		root->left = helper(begin, mid);
		root->right = helper(mid->next, end);
		return root;
	}
};