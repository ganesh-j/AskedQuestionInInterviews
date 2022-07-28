//show difference between == and equals
//Need to take special care in case of STRINGS
//Integers are fine
public class MyClass {
    public static void main(String args[]) {
      String a = new String("a"); //as both are pointing to string buffer space, now changed the constant to memory location
      String b = "a";
      
      
      if (a == b) {
          System.out.println("Equal");
      } else {
          System.out.println("Not Equal");
      }
     
     if (a.equals(b)) {
         System.out.println("Both string are equal");
     }
     
    }
}