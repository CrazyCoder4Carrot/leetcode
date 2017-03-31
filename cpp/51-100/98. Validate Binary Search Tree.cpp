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
    bool helper(TreeNode *node, int pre){
        if(!node)
            return true;
        if()
    }
};