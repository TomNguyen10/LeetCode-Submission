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
        ListNode adjacent = null;

        while (curr != null) {
            adjacent = curr.next;
            curr.next = prev;
            prev = curr;
            curr = adjacent;
        }

        return prev;
    }
}
