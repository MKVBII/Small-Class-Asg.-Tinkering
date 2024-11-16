public class LinkedList<T> {

    Node<T> head;
    Node<T> tail;
    int itemCount; 

    public LinkedList() {

        this.head = null; 
        this.tail = null;
        this.itemCount = 0;

    }

    public void insert(T data) {

        Node<T> newNode = new Node<>(data);

        if (head == null) {

            this.head = newNode;

        }

        newNode.setNext(head); 
        head.setPrev(newNode); 
        head = newNode; 
        itemCount++;

    }

    public int getSize() {

        return this.itemCount;

    }

    public boolean isEmpty() {

        return itemCount == 0;
    }

    public String toString() {

        Node<T> walker = head;
        String display = "";

        for (int i = 1; i <= itemCount; i++) {


            display += walker.getData() + " ";
            walker = walker.getNext();

        }

        return display; 

    }
    
}
