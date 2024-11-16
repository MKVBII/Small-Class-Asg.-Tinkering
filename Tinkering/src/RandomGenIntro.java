import java.util.Random; 

public class RandomGenIntro {
    
    public static void main(String[] args) {

    // > generates pseudo random numbers (not truly random numbers)
         // unbounded limit is just about -2 billion to 2 billion
        Random random = new Random(); 

        int x = random.nextInt(1, 11);// for the bound # to be included, at +1 to the end or 
        double y = random.nextDouble(4.0);
        boolean z = random.nextBoolean(); 
      

        System.out.println(x + " " + y + " " + z); 
    
    }
     
}
