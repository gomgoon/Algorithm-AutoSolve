import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int var;
        char[] arr;
        while (scanner.hasNextInt()) {
            var = scanner.nextInt();
            int length = 1;

            for (int i = 0; i < var; i++)
                length *= 3;

            arr = new char[length];

            for(int i = 0; i < length; i++) {
                arr[i] = '-';
            }

            kantoer(arr, 0, length);

            System.out.println(arr);
        }
    }

    public static void kantoer(char[] arr, int p, int q)
    {
        if (q - p < 3) {
            return;
        }
        
        int third = (q - p) / 3;

        for (int i = p + third; i < p + (third * 2); i++)
        {
            arr[i] = ' ';
        }

        kantoer(arr, p, p + third);
        kantoer(arr, p + (third * 2), p + (third * 3));
    }
}
