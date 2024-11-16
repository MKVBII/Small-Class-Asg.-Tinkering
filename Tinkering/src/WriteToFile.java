import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter; 
import java.io.IOException; 
import java.io.FileNotFoundException; 
import java.io.File; 
import java.util.Scanner; 

    public class WriteToFile {

    /** "Java FileWriter(Write to a file), BroCode"
     *  Findings; 
     * creates text files and tinkers with them
     */
     public static void main(String[] args) {

        //needs to be surrounded by a try-catch blokc because its 
        //considered 'dangerous code' (code that involved lots potential errors)
        try {
            //Creates a new text file (poem.txt) IN YOUR CPU
            FileWriter writer = new FileWriter("poem.txt");
            writer.write("Roses are red \nviolets are blue");
            writer.append("a poem by yr boy");  
            writer.close(); 
        }
            catch (IOException e) {e.printStackTrace();} 

            //ALTERNATE METHOD

     try {
            //OVERWRITES THE FILE IF IT ALREADY EXISTS, AND CAN CREATE NEW ONES THAT DON'T
            BufferedWriter writer = new BufferedWriter(new FileWriter("poem.txt")); 
            writer.write("boopbeepbop"); 
            System.out.println(writer); 
            writer.close();

            FileReader reader = new FileReader("poem.txt"); 
            int characters = reader.read();
            while (characters != -1) {

                String string = "";
                String[] boop = string.split("bumpy butt");
                System.out.print((char)characters + "  " + boop);
                characters = reader.read(); 

            }

            reader.close();

           } catch (IOException e) {e.printStackTrace();}

        } 

        //METHOD FROM 1610 NOTES
        /**
         * 
         * @param fname file name 
         * @return number from a file
         * @throws FileNotFoundException if the file doesn't exist
         */
        public static int getNumberFromFile(String fname) throws FileNotFoundException{

                File file = new File(fname); 
                int number = -1; 

            if (!file.exists()) {

                throw new FileNotFoundException(); 

            }
            
            //attach the file stream to a scanner
            Scanner inFile = new Scanner(file);

            //if theres an integer return it; otherwise, error 
            if (inFile.hasNextInt())  {
                number = inFile.nextInt(); 
            } else {
                System.out.println("File " + fname + " contains no integer.");
                 inFile.close(); 
            }
            
            return number; 
        }

       /**  public static void main(String[] args) throws FileNotFoundException, IOException{

            Scanner input = new Scanner(System.in);
            String fileName; 

            try{ 

            FileWriter writer = new FileWriter("numbreFile.txt");
            writer.write("14"); 
            writer.close(); 

            } catch (IOException e) {

                e.printStackTrace(); 

            }   

            System.out.println("Enter a file name"); 
            fileName = input.nextLine(); 

            File file = new File(fileName); 
            input.close(); 

            if (!file.exists()) {

                throw new FileNotFoundException("File doesn't exist");

            } else {

            getNumberFromFile(fileName); 

            }

        }*/
    
    }