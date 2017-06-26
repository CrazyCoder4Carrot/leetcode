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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if (!root)
            return res;
        stack<TreeNode *> stack;
        stack.push(root);
        while (stack.size()) {
            TreeNode *tmp = stack.top();
            res.push_back(tmp->val);
            stack.pop();
            if (tmp->right) {
                stack.push(tmp->right);
            }
            if (tmp->left) {
                stack.push(tmp->left);
            }
        }
        return res;
    }
};