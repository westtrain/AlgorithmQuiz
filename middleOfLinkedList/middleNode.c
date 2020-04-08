/*
 * Given a non-empty, singly linked list with head node head, return a middle node of linked list.
 * If there are two middle nodes, return the second middle node.
 *
 * Example 1:
 * Input: [1,2,3,4,5]
 * Output: Node 3 from this list (Serialization: [3,4,5])
 * The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
 * Note that we returned a ListNode object ans, such that:
 * ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
 *
 * Example 2:
 * Input: [1,2,3,4,5,6]
 * Output: Node 4 from this list (Serialization: [4,5,6])
 * Since the list has two middle nodes with values 3 and 4, we return the second one.
 *
 * Note:
 * The number of nodes in the given list will be between 1 and 100
 *
 * Runtime: 0 ms
 * Memory Usage: 5.2 MB
 */
struct ListNode* middleNode(struct ListNode* head){
    int i = 0, len = 0;
    struct ListNode* node = head;
    while (node)
    {
        len++;
        node = node->next;
    }
    while (i < len / 2)
    {
        head = head->next;
        i++;
    }
    return head;
}

/* 
 * sample 0ms submission from leetcode.
 *
struct ListNode* middleNode(struct ListNode* head){
    struct ListNode *slow = head;
    struct ListNode *fast = head;
    while(slow&&fast&&fast->next)
    {
        slow=slow->next;
        fast=fast->next->next;
    }
    return slow;
}
*/
