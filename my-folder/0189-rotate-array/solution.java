class Solution {
    public void rotate(int[] arr, int k) {
        int n = arr.length;
        k = k % n;
        reverseArray(arr , 0 , n-1);
        reverseArray(arr , 0 , k-1);
        reverseArray(arr , k , n-1);
    }
    
    public void reverseArray(int[]arr , int start , int end){
        for(int i=start , j=end ; i<j ; i++ , j--) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
}


