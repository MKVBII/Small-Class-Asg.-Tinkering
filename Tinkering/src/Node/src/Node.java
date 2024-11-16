class Node<T> {

    Node<T> previous; 
    T data;
    Node<T> next; 

    public Node(T item) {

        this.previous = null;
        this.data = item;
        this.next = null; 

    }

    public T getData() {

        return data;

    }

    public void setNext(Node<T> nextNode) {

        this.next = nextNode; 

    }

    public Node<T> getNext() {

        return this.next; 

    }

    public void setPrev(Node<T> prevNode) {

        this.previous = prevNode; 

    }

    public Node<T> getPrev() {

        return this.previous;

    }

}