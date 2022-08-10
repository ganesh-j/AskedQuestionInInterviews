// below is bruteforce approach
// optimized approach: 
//get modified input string = input sting  + input string
//find whether pattern is present in input string or not
//modifiedString.substring(inputString)
import java.util.*;

class StringRotationOfAnotherstring {
    public static void main(String[] args) {
  
        String input = "CBA";
        String output = "ABC";
        HashMap<String, Boolean> res = new HashMap<String, Boolean>();
        
        while (true) {
  
            String temp = rotate(input)
            
            if (res.containsKey(temp)) {
                return fase;
            } else {
                res.put(temp, true);
            }
            
            if (temp.equals(output)) {
              return true;
            }
            input = temp;
        }
    }
  
    public static String rotate(String input) {
         char[] temp = input.toCharArray();
         char[] res = new char[temp.length];
         int size = res.length;
         for (int i = 0; i < size; i++) {
              int newIndex = (i+1) % size;
              res[newIndex] = temp[i];
         }
         return String.valueOf(res);
    }
  }
  