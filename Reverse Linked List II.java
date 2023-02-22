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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head == null || head.next == null)
            return head;

        ListNode dummy = new ListNode();
        ListNode traversor = head, prev = dummy, next = null;
        dummy.next = head;
        
        for(int i = 1; i <= right; i++){
            if(i + 1 == left)
                prev = traversor;
            if(i == right)
                next = traversor;
            traversor = traversor.next;
        }
        next.next = null;
        ListNode reversed = reverse(prev.next);
        prev.next.next = traversor;
        prev.next = reversed;

        return dummy.next;
    }
    public ListNode reverse(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode prev = null;
        ListNode current = head;
        while(current != null){
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }
}
