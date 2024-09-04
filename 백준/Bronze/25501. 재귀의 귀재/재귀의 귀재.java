import java.util.Scanner;

public class Main {
    public static int cnt = 0;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String string;
        int n = scanner.nextInt();
        scanner.nextLine();
        for(int i = 0; i < n; i++)
        {
            cnt = 0;
            string = scanner.nextLine();
            System.out.printf("%d %d\n", isPalindrome(string), cnt);
        }
    }

    public static int recursion(String s, int l, int r){
        cnt += 1;
        if (l >= r)
            return 1;
        else if (s.charAt(l) != s.charAt(r))
            return 0;
        else
            return recursion(s, l+1, r-1);
    }

    public static int isPalindrome(String s){
        return recursion(s, 0, s.length() - 1);
    }
}
