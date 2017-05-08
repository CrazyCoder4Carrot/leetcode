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
    void recoverTree(TreeNode* root) {

        TreeNode *node1 = NULL;
        preorder(TreeNode *root, node1);
        TreeNode *node2 = NULL;
        
    }
    void preorder(TreeNode* root, int pre){
    	if(root->left){
    		preorder(root->left, pre);
    	}
    	if(pre && pre ->val > root->val)
    		return root;
    	if(!pre)
    		pre = root->val;
    	if(root->right){
    		preorder(root->right, pre);
    	}
    }
};