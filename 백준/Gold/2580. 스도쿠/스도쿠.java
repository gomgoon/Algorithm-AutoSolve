import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static int[][] arr;

    public static void main(String[] args) throws IOException {
        arr = new int[9][9];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        if(sudoku())
        {
            for (int i=0;i<9;i++) {
                for (int j=0; j<9; j++) {
                    System.out.print(arr[i][j] + " ");
                }
                System.out.println();
            }
        }
    }

    public static boolean sudoku() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (arr[i][j] == 0) {
                    for (int n = 1; n <= 9; n++) {
                        if (isValid(i, j, n)) {
                            arr[i][j] = n;
                            if(sudoku())
                                return true;
                            arr[i][j] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    public static boolean isValid(int i, int j, int n) {
        for (int row = 0; row < 9; row++) {
            if (arr[row][j] == n)
                return false;
        }
        for (int col = 0; col < 9; col++) {
            if (arr[i][col] == n)
                return false;
        }
        int box_x = (i / 3) * 3;
        int box_y = (j / 3) * 3;
        for (int row = box_x; row < box_x + 3; row++) {
            for (int col = box_y; col < box_y + 3; col++) {
                if (arr[row][col] == n)
                    return false;
            }
        }

        return true;
    }
}