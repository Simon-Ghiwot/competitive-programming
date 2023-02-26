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
    public ListNode oddEvenList(ListNode head) {
        if(head == null || head.next == null)
            return head;
        ListNode even = new ListNode(-1), odd = new ListNode(-1);
        ListNode evenTail = even, oddTail = odd, traversor = head;

        int position = 0;
        while(traversor != null){
            if(position % 2 == 0)
                evenTail = evenTail.next = traversor;
            else
                oddTail = oddTail.next = traversor;
            
            traversor = traversor.next;
            position++;
        }

        evenTail.next = odd.next;
        oddTail.next = null;

        return even.next;
    }
}
