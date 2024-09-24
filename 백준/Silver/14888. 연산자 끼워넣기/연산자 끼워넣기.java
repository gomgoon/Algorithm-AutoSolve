import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static int[] option;
    public static int max = -1000000000;
    public static int min = 1000000000;
    public static int n;
    public static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        option = new int[4];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++)
        {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i=0;i<4;i++) {
            option[i] = Integer.parseInt(st.nextToken());
        }

        for (int i=0;i<4;i++) {
            if (option[i] > 0)
                abcd(0, i, arr[0]);
        }

        System.out.println(max);
        System.out.println(min);
    }

    public static void abcd(int depth, int ar, int res) {
        if (depth == n - 1) {
            if (res < min)
                min = res;
            if (res > max)
                max = res;
            return;
        }

        for (int i=0;i<4;i++) {
            if (option[i] > 0) {
                option[i]--;

                switch (i) {
                    case 0:
                        abcd(depth + 1, i, res + arr[depth + 1]);
                        break;
                    case 1:
                        abcd(depth + 1, i, res - arr[depth + 1]);
                        break;
                    case 2:
                        abcd(depth + 1, i, res * arr[depth + 1]);
                        break;
                    case 3:
                        abcd(depth + 1, i, res / arr[depth + 1]);
                        break;
                }

                option[i]++;
            }
        }
    }
}
