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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode dummy = new ListNode();
        ListNode tail = dummy;
        
        while(l1 != null || l2 != null){
            
            int num1 = l1 == null ? 0 : l1.val;
            int num2 = l2 == null ? 0 : l2.val;
            int sum = num1 + num2 + carry;
            carry = sum / 10;
            
            tail.next = new ListNode(sum % 10);
            tail = tail.next;
            if(l1 != null)  l1 = l1.next;
            if(l2 != null)  l2 = l2.next;
            
        }
        if(carry == 1)
            tail.next = new ListNode(1);
        return dummy.next;
    }
}
