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
    int sumNumbers(TreeNode* root) {
    	int sum = 0;
    	helper(root, 0, sum);
    	return sum;
    }
    void helper(TreeNode *root, int curSum, int &sum){
    	if(!root)
    		return;
    	curSum = curSum * 10 + root->val;
    	if(!root->left && !root->right){
    		sum += curSum;
    		return;
    	}
    	if(root->left)
    		helper(root->left, curSum, sum);
    	if(root->right)
    		helper(root->right, curSum, sum);
    }
};