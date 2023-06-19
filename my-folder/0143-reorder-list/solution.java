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
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode second = slow.next;
        ListNode prev = null;
        ListNode theNext = null;

        while (second != null) {
            theNext = second.next;
            second.next = prev;
            prev = second;
            second = theNext;
        }

        slow.next = null;
        ListNode first = head;
        second = prev;
        
        while (second != null) {
            ListNode one = first.next;
            ListNode two = second.next;
            first.next = second;
            second.next = one;
            first = one;
            second = two;
        }

    }
}
