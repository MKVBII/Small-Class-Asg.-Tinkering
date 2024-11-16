import java.io.File;

public class FileIntro {
    
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
     public static void main(String[] args) throws Exception {

       // need to write "copyFileLocation/fileName.extension" if
       //the file was created outside of the project folder
        File file  = new File("/Users/mikebrown/Downloads/Untitled.txt"); 

        if (file.exists()) {
            System.out.println(file.getPath()); 
            System.out.println(file.getAbsolutePath());
            System.out.println(file.isFile());  
            file.delete();

            }
            else 
            System.out.println("No file"); 
         } 

}
