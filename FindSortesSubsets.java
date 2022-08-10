//basically it uses the concepts of subarrays of n elements
//which is (n*(n+1))/2 [1 + 2 + 3 + 4 + 5 + 6...+ (n-1)]
// if there is 1, 2, 3 sorted sequence then we can find subarrays, right

public class FindSortesSubsetsOrSubarrys {
    public static void main(String[] args) {
        int arr[] = {2,1, 4, 7, 3, 5};
        int totalCount = totalSubarrays(arr);
        System.out.println("total no of sorted subarrays are"+ totalCount);
    }
    


static int totalSubarrays(int[] arr) {

    int size = arr.length;
    int startIndex = 0;
    int endIndex = startIndex + 1;
    int totalCount = 0;
    
    while (startIndex < size && endIndex <size) {
     
           if (arr[startIndex] < arr[endIndex]) {
                 endIndex++;
                 if (endIndex == size) {
                    totalCount += counts(startIndex, endIndex-1);
                 }
                
                  
           } else {
               totalCount += counts(startIndex, endIndex);
               startIndex = endIndex;
               endIndex = startIndex + 1;
           }
    }
    reuturn totalCount;
    
} 

static int counts(int startIndex, int endIndex) {
   int totalele = (endIndex - startIndex);
   return (totalele * (totalele + 1))/2;

}

}
