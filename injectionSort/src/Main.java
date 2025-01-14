import java.util.Arrays;

public class Main {
    public static void main(String[] args){
        int arr[] =  {57, 54, 27, 49, 45, 94, 78, 87, 89, 47, 29, 81, 45, 3, 74, 99, 73, 93, 53, 97};
        for (int i = 1 ; i < arr.length ; i++){
            int key = arr[i];
            int j = i-1;
            while(j>=0 && arr[j]> key){
               arr[j+1]=arr[j];
               j=j+1;
            }
            arr[j+1]= key;
        }
        System.out.println(Arrays.toString(arr));
    }
}
