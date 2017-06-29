class Solution {
public:
    TreeNode* upsideDownBinaryTree(TreeNode* root) {
        return helper(root, NULL);
    }
    TreeNode* helper(TreeNode *root, TreeNode *parent) {
        if (!root)
            return NULL;
        if (!root->left && !root->right) {
            root->left = parent ? parent->right : NULL;
            root->right = parent;
            return root;
        }
        TreeNode *left = helper(root->left, root);
        root->left = parent ? parent->right : NULL;
        root->right = parent;
        return left;
    }
};