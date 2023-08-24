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
    public int pairSum(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        ListNode curr = head;
        ListNode prev = null;
        ListNode adjacent = null;

        while (curr != slow) {
            adjacent = curr.next;
            curr.next = prev;
            prev = curr;
            curr = adjacent;
        }

        int max = Integer.MIN_VALUE;
        
        while (slow != null) {
            int value = slow.val + prev.val;
            max = Math.max(value, max);
            slow = slow.next;
            prev = prev.next;
        }

        return max;
    }
}
