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
	vector<vector<int>> levelOrderBottom(TreeNode* root) {
		vector<vector<int>> res;
		if(!root)
			return res;
		vector<TreeNode *> queue;
		queue.push_back(root);
		while(!queue.empty()){
			vector<TreeNode *> temp;
			vector<int> level;
			for(auto node: queue){
				level.push_back(node->val);
				if(node->left)
					temp.push_back(node->left);
				if(node->right)
					temp.push_back(node->right);
			}
			res.push_back(level);
			queue = temp;
		}
		reverse(res.begin(), res.end());
		return res;
	}
};