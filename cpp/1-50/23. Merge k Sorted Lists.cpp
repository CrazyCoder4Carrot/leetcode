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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty())
            return NULL;
        return helper(lists, 0, lists.size() - 1);
    }
    ListNode* helper(vector<ListNode*>& lists, int low, int high)
    {
        if (low > high)
            return NULL;
        if (low == high)
            return lists[low];
        int mid = (low + high) / 2;
        ListNode *left = helper(lists, low, mid);
        ListNode *right = helper(lists, mid + 1, high);
        return merge(left, right);
    }
    ListNode* merge(ListNode *l1, ListNode *l2)
    {
        ListNode *dummyhead = new ListNode(0);
        ListNode *ptr = dummyhead;
        while (l1 && l2)
        {
            ptr->next = (l1->val < l2->val) ? l1 : l2;
            ptr = ptr->next;
            if (l1->val < l2->val)
                l1 = l1->next;
            else
                l2 = l2->next;
        }
        ptr->next = l1 ? l1 : l2;
        return dummyhead->next;
    }
};