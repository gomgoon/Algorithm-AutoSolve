import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static long[] arr;
    public static int n;
    public static long plus;
    public static long next;
    public static long max = -1000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0;i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            next += arr[i];
            plus += arr[i];
            if(plus > next)
                next = plus;
            if (arr[i] < 0)
                plus = 0;
            if (max < next)
                max = next;
        }
        System.out.println(max);
    }
}