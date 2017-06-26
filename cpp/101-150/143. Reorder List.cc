/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
    	if(!head || !head->next)
    		return;
    	vector<ListNode *> nodelist;
    	ListNode *ptr = head;
    	int count = -1;
    	while(ptr){
    		nodelist.push_back(ptr);
    		ListNode *tmp = ptr->next;
    		ptr->next = NULL;
    		ptr = tmp;
    		count++;
    	}
    	for(int i = 0; i < nodelist.size() / 2; i++){
    		 nodelist[i]->next = nodelist[count - i];
    	}
    	for(int i = count; i > nodelist.size()/2; i--)
    		nodelist[i]->next = nodelist[count + 1 - i];
    }
};