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
    int maxPathSum(TreeNode* root) {
    	int res = INT_MIN;
    	maxtoroot(root, res);
    	return res;
    }
    int maxtoroot(TreeNode *root, int &res){
    	if(!root)
    		return 0;
    	int l = maxtoroot(root->left, res);
    	int r = maxtoroot(root->right, res);
    	if(l < 0)
    		l = 0;
    	if(r < 0)
    		r = 0;
    	res = max(res, l + r + root->val);
    	return root->val + max(l, r);
    }
};