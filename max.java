import java.util.Arrays; 
public class greater
{ 
public static void main(String[] args)
{ 
 int ar[] = {10, 324, 45, 90, 9808}
 int max = Arrays.stream(ar).max().getAsInt(); 
 System.out.println("Largest in given array is " +max); 
 } 
 } 
