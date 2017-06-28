/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
    	if(!head)
    		return NULL;
    	RandomListNode *newhead = new RandomListNode(0);
    	map<RandomListNode *, RandomListNode *> dict;
    	RandomListNode *ptr = head;
    	RandomListNode *newptr = newhead;
    	while(ptr){
    		newptr->next = new RandomListNode(ptr->label);
    		newptr->next->random = ptr->random;
    		dict[ptr] = newptr->next;
    		newptr = newptr->next;
    		ptr = ptr->next;
    	}
    	newptr = newhead->next;
    	while(newptr){
    		newptr->random = dict[newptr->random];
    		newptr = newptr->next;
    	}
    	RandomListNode *res = newhead->next;
    	delete newhead;
    	return res;
    }
};