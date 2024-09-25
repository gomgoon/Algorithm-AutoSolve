import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static long[] arr;
    public static int n;
    public static int T;
    public static int[] aristhic;
    public static int max,min;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        arr = new long[101];
        for(int i = 0; i <= 100; i++){
            if (i < 3)
                arr[i] = 1;
            else
                arr[i] = arr[i - 2] + arr[i - 3];
        }
        for(int i=0; i < T; i++){
            n = Integer.parseInt(br.readLine());
            System.out.println(arr[n-1]);
        }
    }
}