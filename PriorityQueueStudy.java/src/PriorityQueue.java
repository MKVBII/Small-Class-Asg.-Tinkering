class PriorityQueue{

    public int[] H = new int[40]; // integer array representing the elements in the heap 
    public int size = -1;

    // Find the index of the parent node of a given node
    public int parent(int i) { //i = index of node you're trying to find the parent of
        return (i - 1) / 2;
    }

    // Find the index of left child of the given node
    public int leftChild(int i) {
        return ((2 * i) + 1);
    }

    // Find the index of the right child of the given node
    public int rightChild(int i) {
        return ((2 * i) + 2);
    }

    // Swap the node's data in order to maintain the heap property - Percolate up
    public void shiftUp(int i) {
        while (i > 0 && H[parent(i)] < H[i]) {

            // Swap parent and current node
            swap(parent(i), i);

            // Update i to parent of i
            i = parent(i);

        }

    }

    // Swap the node's data in order to maintain the heap property -Percolate dowm
    public void shiftDown(int i) {

        int maxIndex = i;

        // Left Child
        int l = leftChild(i);
        if (l <= size && H[l] > H[maxIndex]) {
            maxIndex = l;
        }

        // Right Child
        int r = rightChild(i);
        if (r <= size && H[r] > H[maxIndex]) {
            maxIndex = r;
        }

        // If i not same as maxIndex
        if (i != maxIndex) {
            swap(i, maxIndex);
            shiftDown(maxIndex);
        }
    }

    // insert a new element in the Binary Heap
    public void insert(int p) {

        size = size + 1;
        H[size] = p;

        // Swap up to maintain heap property
        shiftUp(size);
    }

    // Find the element with maximum priority
    public int extractMax() {

        int result = H[0];

        // Replace the value at the root with the value at last leaf node
        H[0] = H[size];
        size = size - 1;
        // Swap down the replaced element to maintain the heap property
        shiftDown(0);
        return result;
    }

    // Change the priority of an element
    public void changePriority(int i, int p) {

        int oldp = H[i];
        H[i] = p;
        if (p > oldp) {
            shiftUp(i);
        }
        else {
            shiftDown(i);
        }
    }

    // Find the current maximum element
    public int getMax() {

        return H[0];

    }

    // remove the element located at given index
    public void remove(int i) {

        H[i] = getMax() + 1;

        // Swap up the node to the root of the heap
        shiftUp(i);

        // Get the node with maximum value
        extractMax();

    }

    public void swap(int i, int j) {

        int temp= H[i];
        H[i] = H[j];
        H[j] = temp;

    }
}    