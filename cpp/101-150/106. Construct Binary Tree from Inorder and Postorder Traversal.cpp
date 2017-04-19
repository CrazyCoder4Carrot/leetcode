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
	TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
		if (postorder.empty())
			return NULL;
		int end = postorder.size();
		return helper(inorder, 0, end - 1, postorder, 0, end - 1);
	}
	TreeNode* helper(vector<int> &inorder, int istart, int iend, vector<int> &postorder, int pstart, int pend) {
		if (pstart > pend)
			return NULL;
		int rootval = postorder[pend];
		TreeNode *root = new TreeNode(rootval);
		if (pstart == pend) {
			return root;
		}
		int i = istart;
		for (; i <= iend; i++) {
			if (inorder[i] == rootval)
				break;
		}
		int left_len = i - istart;
		root->left = helper(inorder, istart, i - 1, postorder, pstart, pstart + left_len - 1);
		root->right = helper(inorder, i + 1, iend, postorder, pstart + left_len, end - 1);
		return root;
	}
};