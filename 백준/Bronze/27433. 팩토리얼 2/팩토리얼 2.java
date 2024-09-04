import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();  // N 값 입력받기
        System.out.println(factorial(n));  // 팩토리얼 값 출력
    }

    // 팩토리얼 계산 함수 (재귀)
    public static long factorial(long n) {
        if (n == 0 || n == 1) {
            return 1;  // 0! 또는 1! = 1
        }
        return n * factorial(n - 1);  // 재귀 호출을 통한 팩토리얼 계산
    }
}
