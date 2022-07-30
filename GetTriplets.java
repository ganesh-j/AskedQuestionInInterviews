import java.util.*;

public class GetTriplets {
    public static void main(String[] args) {
        int[] arr = new int[]{0, -1, 2, -3, 1};
        int target = 0;
        ArrayList<ArrayList<Integer>> res = getTriplets(arr, target);
        for (int i = 0; i < res.size(); i++) {
            ArrayList<Integer> temp = res.get(i);
            for (int j = 0; j < temp.size(); j++) {
                System.out.println(temp.get(j));
                System.out.println(",");
            }
            System.out.println("");
        }
    }
    

public static ArrayList<ArrayList<Integer>> getTriplets(int[] arr, int target) {
    Arrays.sort(arr);
    ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
    for(int i = 0; i < arr.length - 1; i++) {
           int remainingSum = target - (arr[i]);
           int low = i+1;
           int end = arr.length - 1;

           
           while (low < end) {
               if (arr[low] + arr[end] > remainingSum) {
                    end--;
               } else if (arr[low] + arr[end] < remainingSum) {
                    low++;
               } else if (arr[low] + arr[end] == remainingSum) {
                     ArrayList<Integer> currRes = new ArrayList<Integer>();
                    //add elements into arraylist
                     currRes.add(arr[i]);
                     currRes.add(arr[low]);
                     currRes.add(arr[end]);
                     res.add(currRes);
                     low++;
                     end--;
               }
                 
           }
    }
    return res;

}

}