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
	vector<int> res;
	vector<int> inorderTraversal(TreeNode* root) {
		dfs(root);
		return res;
	}
	void dfs(TreeNode *root){
		if(!root)
			return;
		if(root->left)
			dfs(root->left);
		res.push_back(root->val);
		if(root->right)
			dfs(root->right);
	}
};