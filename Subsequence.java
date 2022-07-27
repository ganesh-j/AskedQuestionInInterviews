import java.util.*;

//subsequence is based on the concept
//case1: take the element
//case2: do not take the element
public class Main {
    static int count = 0;
    
    public static void main(String[] args) {

        int nums[] = new int[]{1, 2, 3};
        int k = 2;
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> list = new ArrayList<Integer>();
        subsequence(nums, 0, k, res, list);
        
        System.out.println("total is"+count);
        
        for (int i = 0; i < res.size(); i++) {
            int len = res.get(i).size();
            for (int j = 0; j < len; j++) {
                System.out.println("number is"+res.get(i).get(j));
                System.out.println(",");
            }
            System.out.println("New subseuence is");
            
        }
        
    }

    public static void subsequence(int[] nums, int currIndex, int k, ArrayList<ArrayList<Integer>> res, ArrayList<Integer> currList) {
        
        

        //if (currList.size() == k) {
        if (currIndex >= nums.length) {
            count++;
           // System.out.println("showing subseuence");
            //for (int i = 0; i < currList.size(); i++) {
            //    System.out.println("values are"+ currList.get(i));
            //}
            res.add(currList);
            return;
        }


        ArrayList<Integer> temp = new ArrayList<Integer>();
        for (int j = 0; j < currList.size(); j++) {
                temp.add(currList.get(j));
        }
        currList.add(nums[currIndex]);
        //include
        subsequence(nums, currIndex+1, k, res, currList);
        //exclude
        subsequence(nums, currIndex+1, k, res, temp);
    
    }   
}
