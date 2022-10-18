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
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null)
            return head;
        ListNode fast = head;
        ListNode slow = head;
        ListNode prev = null;
        while(fast != null && fast.next != null){
            fast = fast.next.next;
            prev = slow;
            slow = slow.next;
        }
        ListNode secondHead = prev.next;
        prev.next = null;
        ListNode first = sortList(head);
        ListNode second = sortList(secondHead);
        return mergeTwoLists(first, second);
    }
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list2 == null)   return list1;
        if(list1 == null)   return list2;
        
        ListNode dummy = new ListNode();
        ListNode tail = dummy;
        while(list1 != null && list2 != null){
            tail.next = list1.val < list2.val ? list1 : list2;
            if(list1.val < list2.val)
                list1 = list1.next;
            else
                list2 = list2.next;
            tail = tail.next;
        }
        if(list1 == null)
            tail.next = list2;
        if(list2 ==null)
            tail.next = list1;
        
        return dummy.next;
    }
}
