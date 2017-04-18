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
	bool isSymmetric(TreeNode* root) {
		if(!root)
			return true;
		return helper(root->left, root->right);

	}
	bool helper(TreeNode *root1, TreeNode *root2) {
		if (!root1 && !root2)
			return true;
		if ((!root1 && root2) || (root1 && !root2))
			return false;
		if(root1->val == root2->val){
			return helper(root1->left , root2->right) && helper(root1->right, root2->left);
		}
		else
			return false;

	}
};