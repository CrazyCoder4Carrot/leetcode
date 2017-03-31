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
    bool isValidBST(TreeNode* root) {
        if(!root || (!root->left && !root->right))
            return true;
        return helper(root, NULL, NULL);
    }
    bool helper(TreeNode *node, TreeNode *low, TreeNode *high){
        if(!node)
            return true;
        if(low && low->val >= node->val || (high && high->val <= node->val))
            return false;
        return helper(node->left, low, node) & helper(node->right, node, high);
    }
};