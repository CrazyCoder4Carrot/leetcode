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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        return res;
    }
    void preorder(TreeNode *root, int depth, vector<vector<int>> &res){
    	if(!root)
    		return;
    	if(depth == res.size()){
    		res.push_back(vector<int> ());
    	}
    	if(depth % 2 == 1){
    		res[depth].insert(0, root->val);
    	}
    	else{
    		res[depth].push_back(root->val);
    	}
    	preorder(root->left, depth + 1, res);
    	preorder(root->right, depth + 1, res);
    }
};