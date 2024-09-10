import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n;
        char[][] arr;
        n = scanner.nextInt();
        arr = new char[n][n];

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                arr[i][j] = '*';
            }
        }

        whole(arr, 0, 0, n);

        for(int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }
    }

    public static void whole(char[][] arr, int x, int y, int third)
    {
        int tmp = third/3;
        if (third < 3)
            return;

        whole(arr, x, y, tmp);
        whole(arr, x + tmp, y, tmp);
        whole(arr, x + (tmp*2), y, tmp);

        whole(arr, x, y + tmp, tmp);
        whole(arr, x + (tmp*2), y + tmp, tmp);

        whole(arr, x, y + (tmp*2), tmp);
        whole(arr, x + tmp, y + (tmp*2), tmp);
        whole(arr, x + (tmp*2), y + (tmp*2), tmp);

        for (int i = x+tmp; i < x+(tmp*2); i++) {
            for (int j = y+tmp; j < y+(tmp*2); j++) {
                arr[i][j] = ' ';
            }
        }
    }
}
