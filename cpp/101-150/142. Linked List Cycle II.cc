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
    ListNode *detectCycle(ListNode *head) {
    	ListNode *slow = head;
    	ListNode *fast = head;
    	ListNode *tmp = NULL;
    	while(slow && fast && fast->next){
    		slow = slow->next;
    		fast = fast->next->next;
    		if(slow == fast){
    			tmp = slow;
    			break;
    		}
    	}
    	if(!tmp)
    		return NULL;
    	while(tmp != head){
    		tmp = tmp->next;
    		head = head->next;
    	}
    	return tmp;
    }
};