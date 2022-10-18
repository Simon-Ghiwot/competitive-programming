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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode();
        ListNode traversor = dummy.next = head;
        ListNode tail = dummy;
        
        int count = 0;
        
        while(traversor != null){
            count++;
            if(count % k == 0){
                
                ListNode next = traversor.next;
                ListNode current = tail.next;
                ListNode prev = tail;
                
                while(current != next){
                    ListNode nxt = current.next;
                    current.next = prev;
                    prev = current;
                    current = nxt;
                }
                ListNode newTail = tail.next;
                tail.next.next = next;
                tail.next = prev;
                traversor = tail = newTail;
                
            }
            traversor = traversor.next;
        }
        return dummy.next;
    }
}
