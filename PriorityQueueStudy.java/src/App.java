public class App {
    public static void main(String[] args) throws Exception {

            PriorityQueue pq = new PriorityQueue();

            /* 
               68
              /  \
            43    28
           /  \  /  \
          34 20  17  21 
         /  \
        23  31

            Create a priority queue shown in example in a binary max heap form.
            Queue will be represented in the form of array as:
            68 43 28 34 20 17 21 23 31 */

            // Insert the elements to the priority queue
            pq.insert(68);
            pq.insert(43);
            pq.insert(28);
            pq.insert(34);
            pq.insert(20);
            pq.insert(17);
            pq.insert(21);
            pq.insert(23);
            pq.insert(31);

            int i = 0;

            // Priority queue before extracting maximum value
            System.out.print("Elements in the Priority Queue : ");

            while (i <= pq.size) {
                System.out.print(pq.H[i] + " ");
                i++;
            }
            System.out.print("\n");

            // Node with maximum priority in the heap
            System.out.print("Node with maximum priority : " + pq.extractMax() + "\n");

            // Priority queue after removing maximum value
            System.out.print("Priority queue after " + "Removing maximum : ");
            int j = 0;

            while (j <= pq.size) {
                System.out.print(pq.H[j] + " ");
                j++;
            }
            System.out.print("\n");

            // Change the priority of element present at index 2 to 13
            pq.changePriority(2, 13);
            System.out.print("Priority queue after " + "changing the priority at index 2 :");
            int k = 0;

            while (k <= pq.size) {
                System.out.print(pq.H[k] + " ");
                k++;
            }
            System.out.print("\n");

            // Remove element at index 3
            pq.remove(3);
            System.out.print("Priority queue after " + "removing the element at index 3 : ");
            int l = 0;

            while (l <= pq.size) {
                System.out.print(pq.H[l] + " ");
                l++;
            }

                System.out.println("\nparent: ");
                System.out.println(pq.parent(0));
            
        }
    }

