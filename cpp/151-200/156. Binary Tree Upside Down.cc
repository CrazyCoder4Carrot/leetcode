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
    TreeNode* upsideDownBinaryTree(TreeNode* root) {
        if (!root)
            return NULL;
        if (!root->left && !root->right)
            return root;
        return helper(root, NULL);
    }
    TreeNode* helper(TreeNode *root, TreeNode *parent) {
        if (!root)
            return NULL;
        if (!root->left && !root->right) {
            root->left = parent->right;
            root->right = parent;
            return root;
        }
        TreeNode *left = helper(root->left, root);
        root->left = parent ? parent->right : NULL;
        root->right = parent;
        return left;
    }
};