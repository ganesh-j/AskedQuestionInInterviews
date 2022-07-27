public class MyClass {
    public static void main(String args[]) {
       int a[] = { -2, 2, -3, 1 };
       //sum of all positive numbers
       int currSum = 0;
       for (int i = 0; i < a.length; i++) {
          if (a[i] > 0)
            currSum += a[i];
       }
       if (currSum % 2 == 0) {
           //this is max sum
           System.out.println("max-sum is"+currSum);
           return;
       }
       
       //substract positive odd number or add negative odd number. Keep track of it
       int ans = Integer.MIN_VALUE;
       for (int i  = 0; i < a.length; i++) {
           if (a[i] % 2 != 0) {
               
                if (a[i] < 0) {
                    ans  = Math.max(ans, (currSum + a[i]));
                } else {
                    ans  = Math.max(ans, (currSum - a[i]));
                }
           }
       }
       System.out.println("max-sum is:"+ ans);
       
       return ;
    }
}