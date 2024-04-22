class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode prev = dummy;
        ListNode current = head;
        
        while (current != null) {
            boolean duplicate = false;
            while (current.next != null && current.val == current.next.val) {
                current = current.next;
                duplicate = true;
            }
            if (duplicate) {
                prev.next = current.next;
            } else {
                prev = prev.next;
            }
            current = current.next;
        }
        
        return dummy.next;
    }
}

