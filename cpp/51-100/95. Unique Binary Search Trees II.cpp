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
	vector<TreeNode*> generateTrees(int n) {
	    vector<TreeNode *> res;
	    if(n == 0)
	    return res;
		return generator(1, n);
	}
	vector<TreeNode *> generator(int s, int e) {
		vector<TreeNode *> res;
		if (s > e) {
		    res.push_back(NULL);
			return res;
		}
		for (int i = s; i <= e; i++) {
			vector<TreeNode *> left_nodes = generator(s, i - 1);
			vector<TreeNode *> right_nodes = generator(i + 1, e);
			for(auto left: left_nodes)
				for(auto right: right_nodes)
				{
					TreeNode *root = new TreeNode(i);
					root->left = left;
					root->right = right;
					res.push_back(root);
				}
		}
		return res;
	}
};