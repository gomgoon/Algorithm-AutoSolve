import java.util.Scanner;

public class Main {

    static int cnt = 0;
    static int result = -1;
    static int k;

    public static void main(String[] args) {
        int n;
        int[] arr;
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        k = scanner.nextInt();
        arr = new int[n + 1];
        for (int i = 0; i < n; i++){
            arr[i] = scanner.nextInt();
        }

        merge_sort(arr, 0, n-1);
        System.out.println(result);
    }

    public static void merge_sort(int[] arr, int p, int r) {
        if (p < r) {
            int q = (p + r) / 2;
            merge_sort(arr, p, q);   // 왼쪽 부분 정렬
            merge_sort(arr, q + 1, r); // 오른쪽 부분 정렬
            merge(arr, p, q, r);    // 병합
        }
    }

    public static void merge(int[] arr, int p, int q, int r) {
        int[] tmp = new int[r - p + 1];
        int i = p, j = q + 1, t = 0;

        // 두 배열을 병합
        while (i <= q && j <= r) {
            if (arr[i] <= arr[j]) {
                tmp[t++] = arr[i++];
            } else {
                tmp[t++] = arr[j++];
            }
            cnt++;
            if (k == cnt)
                result = tmp[t-1];
        }

        // 왼쪽 배열의 남은 요소 추가
        while (i <= q) {
            tmp[t++] = arr[i++];
            cnt++;
            if (k == cnt)
                result = tmp[t-1];
        }

        // 오른쪽 배열의 남은 요소 추가
        while (j <= r) {
            tmp[t++] = arr[j++];
            cnt++;
            if (k == cnt)
                result = tmp[t-1];
        }

        // tmp 배열을 원래 배열에 복사
        for (i = p, t = 0; i <= r; i++, t++) {
            arr[i] = tmp[t];
        }
    }
}
