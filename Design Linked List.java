class MyLinkedList {
    private Node head, tail;
    private int size;
    public MyLinkedList() {
        head = tail = null;
        size = 0;
    }
    
    public int get(int index) {
        if(index >= size)
            return -1;
        Node traversor = head;
        for(int i = 0; i < index; i++){
            traversor = traversor.next;
        }
        return traversor.val;
    }
    public void addAtHead(int val) {
        Node temp = new Node(val);
        if(head == null)
            head = tail = temp;
        else{
            temp.next = head;
            head = temp;
        }
        size++;
    }
    
    public void addAtTail(int val) {
        Node t = head;
        Node temp = new Node(val);
        if(head == null)
            head = tail = temp;
        else{
            tail.next = temp;
            tail = temp;
        }
        size++;
    }
    private Node findPrev(int index){
        Node traversor = head;
        Node prev = null;
        for(int i = 0; i < index; i++){
            prev = traversor;
            traversor = traversor.next;
        }
        return prev;
    }
    public void addAtIndex(int index, int val) {
        if(index > size)    return;

        Node temp = new Node(val);
        Node prev = findPrev(index);

        if(head == null)
            head = tail = temp;
        else if(prev == null){
            temp.next = head;
            head = temp;
        }
        else{
            temp.next = prev.next;
            prev.next = temp;
            if(prev == tail){
                tail = temp;
            }
        }
        size++;
    }
    
    public void deleteAtIndex(int index) {
        if(index >= size || index < 0)
            return;
        Node prev = findPrev(index);
        if(head == tail)
            head = tail = null;
        else if(prev == null)
            head = head.next;
        else{
            prev.next = prev.next.next;
            if(prev.next == null){
                tail = prev;
            }
        }
        size--;
    }
    
    class Node{
        int val;
        Node next;
        Node(int v){
            val = v;
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
