import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException; 
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.LineNumberReader;
import java.io.File;
import java.io.FileInputStream; 

public class ReadFile {
    
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
        public static void main(String[] args) {

            /*try {
            FileReader reader = new FileReader("poem.txt");
            int data = reader.read(); 
            while (data != -1) {//-1 is what 'read()' returns when the end of the file is reached
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
            } */
            

         

        //ALTERNATE METHOD
        File file = new File("poem.txt"); 
        try {

        //    BufferedReader reader = new BufferedReader(new FileReader("poem.txt")); 
            String string = readFromInputStream(new FileInputStream(file));

          //  while ((string = reader.readLine()) != null) 
          LineNumberReader lineCounter = new LineNumberReader(new FileReader("poem.txt"));
            int lineCount = 0; 
            String lineRead = ""; 

            while ((lineRead = lineCounter.readLine()) != null) {

            lineCount = lineCounter.getLineNumber(); 
        
        }

            System.out.println(string + " " + lineCount);
            //reader.close(); 

        } catch(IOException e) {

            e.printStackTrace(); 

        }


    } 

    private static String readFromInputStream(InputStream inputStream) throws IOException{

    StringBuilder resultStringBuilder = new StringBuilder(); 
    try {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));

        String line; 
        while ((line = bufferedReader.readLine()) != null) {

            resultStringBuilder.append(line).append("\n"); 

        }
 
    } catch (IOException e) {
        e.printStackTrace(); 
      }

    return resultStringBuilder.toString(); 

}

}




