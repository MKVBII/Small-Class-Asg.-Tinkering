import java.io.File;
import java.io.FileWriter;
import java.io.IOException; 
import java.io.FileReader; 
import java.io.FileNotFoundException;
import java.io.*; //gives us access to

public class FileResearch {

    /** KEY FINDINGS
     * -try-catch methods are needed when using code that can potentially
     *  produce alot of errors 
     * 
     */
     

    //BRO CODE

    /** "The File Class, BroCode" (intro, creating a file)
     * Findings;
     * 
     * Methods; 
     * -exists(); self explanatory 
     * -getPath(); prints whatever is in the constructor of the particular file (like the "" after pathname: below)
     * -getAbsolutePath(); prints the location details of the file
     * -isFile(); returns true or false depending on whether or not your file is in fact a file
     * -delete(); deletes the file FROM YOUR CPU
     */
     /** public static void main(String[] args) throws Exception {

       // need to write "copyFileLocation/fileName.extension"
        File file  = new File("/Users/mikebrown/Downloads/Untitled.txt"); 

        if (file.exists()) {
            System.out.println(file.getPath()); 
            System.out.println(file.getAbsolutePath());
            System.out.println(file.isFile());  

            }
            else 
            System.out.println("No file"); 
         } */

    /** "Java FileWriter(Write to a file), BroCode"
     *  Findings; 
     * creates text files and tinkers with them
     */
   /**  public static void main(String[] args) {

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
     } */
        
        /** "Java FileReader" (read a file), BroCode 
         *   Findings; 
         *  -FileReader allows us to read the contents of a file as a 
         *   stream of characters one by one 
         *  -Read() returns an int value that contains the byte value 
         *   (which can be cast as a character value)
         *  -When read() returns -1, there is no omre data to be read
         *  -printStackTrace() is a tool that prints the throwable along
         *  with other details like the line number and class name where the 
         *  exception occured 
         */
        /**public static void main(String[] args) {

            try {
            FileReader reader = new FileReader("poem.txt");
            int data = reader.read(); 
            while (data != -1) {
                System.out.println((char)data); 
                data = reader.read();//allows the reader to move to successing characters
            }
            reader.close(); 
            } 
            catch (FileNotFoundException e) {//for reader
                e.printStackTrace(); 
            }
            catch (IOException e) {//for reader.read()
                e.printStackTrace(); 
            }
            

        } */

        /** "Java File IO (Reading, Writing, Copying)", Keep On Coding
         * 
         */

        public static void main(String[] args) {
          
            //WRITING to a file
           /**try {
            //OVERWRITES THE FILE IF IT ALREADY EXISTS, AND CAN CREATE NEW ONES THAT DON'T
            BufferedWriter writer = new BufferedWriter(new FileWriter("poem.txt")); 
            writer.write("boop\nbeep\nbop"); 
            System.out.println(writer); 
            writer.close();

            FileReader reader = new FileReader("poem.txt"); 
            int characters = reader.read();
            while (characters != -1) {

                System.out.print((char)characters);
                characters = reader.read(); 

            }

            reader.close();

           } catch (IOException e) {

           e.printStackTrace();

           } */

           //READING to a file
           /**  try {

            BufferedReader reader = new BufferedReader(new FileReader("poem.txt")); 
            String string;

            while ((string = reader.readLine()) != null) {

                System.out.println(string);

            }
            reader.close(); 

           } catch (Exception e) {

            e.printStackTrace(); 

           } */

           //COPYING a file
           try {

            BufferedWriter wtr = new BufferedWriter( new FileWriter("poem-copy.txt"));
            BufferedReader reader = new BufferedReader(new FileReader("poem.txt")); 
            String string;

            while ((string = reader.readLine()) != null) {

                wtr.write(string + "\n"); 

            }
            reader.close(); 
            wtr.close(); 

           } catch (Exception e) {

            e.printStackTrace(); 

           }
           
        }
}
