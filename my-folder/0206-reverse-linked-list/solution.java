/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;

        ListNode curr = head;
        ListNode prev = null;
        ListNode theNext = null;

        while (curr != null) {
            theNext = curr.next;
            curr.next = prev;
            prev = curr;
            curr = theNext;
        }

        return prev;
    }
}
