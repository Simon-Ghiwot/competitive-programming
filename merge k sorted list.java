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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0 || lists == null)
            return null;
        
        while(lists.length != 1){
            List<ListNode> merged = new ArrayList<>();
            for(int i = 0; i < lists.length; i += 2){
                ListNode first = lists[i];
                ListNode second = i + 1 < lists.length ? lists[i + 1] : null;
                merged.add(mergeTwoLists(first, second));
            }  
            lists = merged.toArray(new ListNode[0]);
        }
        return lists[0];
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
