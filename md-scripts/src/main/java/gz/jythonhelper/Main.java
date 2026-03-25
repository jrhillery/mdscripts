package gz.jythonhelper;

import java.io.File;

public class Main {

   private static void generatePy(String outputDir, String... files) {
      EasyJython ej = new EasyJython(outputDir);
      ej.setLibs(new String[0]);
      ej.generatePys(files);

   } // end generatePy(String, String[], String...)

   public static void main(String[] args) {
      if (args.length > 1) {
         String outputDir = args[0];
         String[] files = args[1].split(File.pathSeparator);
         generatePy(outputDir, files);
      } else {
         System.out.println("Missing argument; need <output directory> and <source directories path>");
      }

   } // end main(String[])

} // end class Main
