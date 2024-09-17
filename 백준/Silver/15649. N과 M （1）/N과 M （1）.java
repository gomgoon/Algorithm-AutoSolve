import java.util.Scanner;

public class Main {
    public static boolean[] visit;
    public static int[] arr;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int N, M;

        N = scanner.nextInt();
        M = scanner.nextInt();
        visit = new boolean[N];
        arr = new int[M];
        dfs(N, M, 0);
    }

    public static void dfs(int n, int m, int depth) {
        if (depth == m) {
            for (int val : arr) {
                System.out.print(val + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visit[i]) {

                visit[i] = true;
                arr[depth] = i + 1;
                dfs(n, m, depth + 1);

                visit[i] = false;
            }
        }
    }

}