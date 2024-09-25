import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static int[] arr;
    public static int n;
    public static int[] aristhic;
    public static int max,min;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        for (int i=0;i<n;i++) {
            if(i==0 || i==1)
                arr[i] = i+1;
            else
                arr[i] = (arr[i - 1] + arr[i - 2]) % 15746;
        }
        System.out.println(arr[n-1]);
    }
}