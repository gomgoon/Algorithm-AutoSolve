import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

    public static int N;
    public static boolean[][] chess;
    public static int res=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        chess = new boolean[N][N];

        solve(0);
        System.out.println(res);
    }

    public static void solve(int row) {
        if(row == N) {
            res++;
            return;
        }

        for (int i = 0; i< N; i++) {
            if (queen(row, i)) {
                chess[row][i] = true;
                solve(row + 1);
                chess[row][i] = false;
            }
        }
    }

    public static boolean queen(int row, int col) {
        for (int i = 0; i < row; i++) {
            if (chess[i][col] == true) {
                return false;
            }
        }

        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (chess[i][j] == true) {
                return false;
            }
        }

        for (int i = row - 1, j = col + 1; i >= 0 && j < N; i--, j++) {
            if (chess[i][j] == true) {
                return false;
            }
        }

        return true;
    }
}