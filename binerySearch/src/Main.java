import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int arr[] =  {57, 54, 27, 49, 45, 94, 78, 87, 89, 47, 29, 81, 45, 3, 74, 99, 73, 93, 53, 97};

        // bubble sort
        for (int y = 1 ; y < arr.length-1 ; y++) {
            for (int i = 0; i < arr.length-y; i++) {
                if (arr[i] > arr[i + 1]) {
                    int f = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = f;
                }
            }
        }

        System.out.print("Enter num you want: ");
        int p = scanner.nextInt();
        int x1 = 0;
        int x2 = arr.length -1 ;
        int R = -1 ;

        while ( x1 <= x2 ){
            int mid = (x2+x1)/2;

            if ( p == arr[mid] ){
                R = mid ;
                break;
            }

            if ( p < arr[mid]){
                x2 = mid-1;
            }
            else{
                x1 = mid +1 ;
            }
        }

        if (R!=-1) {
            System.out.println(R);
        }
        else{
            System.out.println("your num is not found !");
        }
        //System.out.println(Arrays.toString(arr));
    }
}
