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
	vector<vector<int>> pathSum(TreeNode* root, int sum) {
		vector<vector<int>> res;
		vector<int> path;
		helper(root, sum, path, res);
		return res;
	}
	void helper(TreeNode *root, int sum, vector<int> path, vector<vector<int>> &res) {
		if(!root)
			return;
		if(root->val == sum && !root->right && !root->left) {
			path.push_back(root->val);
			res.push_back(path);
		}
		sum -= root->val;
		path.push_back(root->val);
		helper(root->left, sum, path, res);
		helper(root->right, sum, path, res);
		path.pop()
		return;
	}
};