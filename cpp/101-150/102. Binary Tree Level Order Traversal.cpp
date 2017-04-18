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
	vector<vector<int>> levelOrder(TreeNode* root) {
		vector<vector<int>> res;
		if(!root)
			return res;
		vector<TreeNode *> level;
		level.push_back(root);
		while(level.size() != 0){
			vector<TreeNode *> temp;
			vector<int> level_vals;
			for(auto node : level){
				level_vals.push_back(node->val);
				if(node->left)
					temp.push_back(node->left);
				if(node->right)
					temp.push_back(node->right);
			}
			res.push_back(level_vals);
			level = temp;
		}
		return res;
	}
};