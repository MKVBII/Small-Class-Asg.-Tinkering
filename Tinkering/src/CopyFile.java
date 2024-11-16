import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

public class CopyFile {
    public static void main(String[] args) {

        try {

            BufferedWriter wtr = new BufferedWriter(new FileWriter("poem-copy.txt"));
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
