public class SimpleFileIO {

    public static void writeToFile(String filename, String content) {
        try {
            java.io.FileWriter fileWriter = new java.io.FileWriter(filename);
            fileWriter.write(content);
            fileWriter.close();
        } catch (java.io.IOException e) {
            System.err.println("An error occurred while writing to the file: " + e.getMessage());
        }
    }


    public static void main(String[] args) {
        String filename = "output.txt";
        String content = "This is some sample text.";
        writeToFile(filename, content);
    }
}