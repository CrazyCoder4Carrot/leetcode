/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
	void connect(TreeLinkNode *root) {
		TreeLinkNode *prev = root;
		while (prev) {
			TreeLinkNode *first = prev->left;
			TreeLinkNode *cur = first;
			while (prev && cur) {
				cur->next = prev->right;
				cur = cur->next;
				prev = prev->next;
				if (prev) {
					cur->next = prev->left;
					cur = cur->next;
				}
			}
			prev = first;
		}
	}
};