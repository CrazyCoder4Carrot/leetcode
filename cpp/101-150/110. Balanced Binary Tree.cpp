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
	bool isBalanced(TreeNode* root) {
		return helper(root) != -1;
	}
	int helper(TreeNode *root){
		if(!root)
			return 0;
		int left = helper(root->left);
		if(left == -1)
			return -1;
		int right = helper(root->right);
		if(right == -1)
			return -1;
		if(abs(left - right) > 1)
			return -1;
		return max(left, right) + 1;
	}
};