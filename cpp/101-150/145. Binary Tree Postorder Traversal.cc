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
    vector<int> postorderTraversal(TreeNode* root) {
    	vector<int> res;
    	stack<TreeNode *> s;
    	TreeNode *p = root;
    	while(stack.size() || p != NULL){
    		if(p != NULL){
    			stack.push(p);
    			res.insert(res.begin(), p->val);
    			p = p->right;
    		}
    	}
    }
};