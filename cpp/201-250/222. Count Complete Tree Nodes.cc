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
    int countNodes(TreeNode* root) {
        if(!root)
            return 0;
        int leftcnt = 0, rightcnt = 0;
        auto l = root;
        auto r = root;
        while(l){
            l = l->left;
            leftcnt++;
        }
        while(r){
            r = r->right;
            rightcnt++;
        }
        if(leftcnt == rightcnt)
            return pow(2, leftcnt) - 1;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};