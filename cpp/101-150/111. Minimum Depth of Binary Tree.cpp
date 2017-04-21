/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 #include<climits>
class Solution {
public:
	int minDepth(TreeNode* root) {
		if(!root)
			return 0;
		if(!root->left && !root->right)
			return 1;
		int left, right;
		left = right = INT_MAX;
		if(root->left)
			left = minDepth(root->left);
		if(root->right)
			right = minDepth(root->right);
		return min(left, right) + 1;
	}
};