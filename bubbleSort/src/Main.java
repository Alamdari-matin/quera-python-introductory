import java.util.Arrays;

public class Main {
    public static void main(String[] args){
        int arr[] =  {57, 54, 27, 49, 45, 94, 78, 87, 89, 47, 29, 81, 45, 3, 74, 99, 73, 93, 53, 97};
        for(int x = 1 ; x <19 ;x++){
            for(int i = 0 ; i<(arr.length-x); i++) {
               int f;
               if (arr[i] > arr[i + 1]) {
                   f = arr[i];
                   arr[i] = arr[i + 1];
                   arr[i + 1] = f;
                }
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}
