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
    public ListNode partition(ListNode head, int x) {
       if(head == null || head.next == null)
            return head;

        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode traversor = head, prev = dummy, pivot = dummy;

        while(traversor != null){
            if(traversor.val < x){
                prev.next = traversor.next;
                traversor.next = pivot.next;
                pivot.next = pivot = traversor;
            }
            prev = traversor;
            traversor = traversor.next;
        }

        return dummy.next; 
    }
}
