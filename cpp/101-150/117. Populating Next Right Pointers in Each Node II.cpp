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
		while(prev){
			while(prev){
				if(prev->left || prev->right)
					break;
				prev = prev->next;
			}
			if(!prev)
				break;
			TreeLinkNode *first;
			if(prev->left)
				first = prev->left;
			else
				first = prev->right;
			TreeLinkNode *cur = first;
			while(cur){
				while(prev){
					if(prev->left && prev->left != cur){
						cur->next = prev->left;
						break;
					}
					if(prev->right && prev->right != cur){
						cur->next = prev->right;
						prev= prev->next;
						break;
					}
					prev = prev->next;
				}
				cur = cur->next;
			}
			prev = first;
		}
	}
};