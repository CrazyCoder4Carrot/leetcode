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
	TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
		if(preorder.empty())
			return NULL;
		int end = preorder.size();
		return helper(preorder, 0, end - 1, inorder, 0, end - 1);
	}
	TreeNode* helper(vector<int> &preorder, int pstart, int pend, vector<int> &inorder, int istart, int iend){
		if(pstart > pend)
			return NULL;
		int rootval = preorder[pstart];
		TreeNode *root = new TreeNode(rootval);
		if(pstart == pend){
			return root;
		}
		int i = istart;
		for(; i <= iend; i++){
			if(inorder[i] == rootval)
				break;
		}
		int left_len = i - istart;
		root->left = helper(preorder, pstart + 1, pstart + left_len, inorder, istart, i - 1);
		root->right = helper(preorder, pstart + left_len + 1, pend, inorder, i + 1, iend);
		return root;
	}
};