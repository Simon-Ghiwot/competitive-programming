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
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null)
            return head;
        ListNode dummy = new ListNode(0, head);
        ListNode traversor = head, tail = head;
        while(traversor != null){
            if(traversor.val != tail.val){
                tail = tail.next = traversor;
            }
            traversor = traversor.next;
        }
        tail.next = null;
        return dummy.next;
    }
}
