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
    public void reorderList(ListNode head) {

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode curr = slow.next;
        slow.next = null;

        ListNode prev = null;
        while (curr != null) {
            ListNode adj = curr.next;
            curr.next = prev;
            prev = curr;
            curr = adj;
        }

        while (prev != null && head != null) {
            ListNode top = head.next;
            ListNode bot = prev.next;
            head.next = prev;
            prev.next = top;
            head = top;
            prev = bot;
        }

    }
}
