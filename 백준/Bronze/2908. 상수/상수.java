import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int var, var2;
        String st_var, st_var2;
        Scanner scanner = new Scanner(System.in);

        var = scanner.nextInt();
        var2 = scanner.nextInt();

        st_var = String.valueOf(var);
        st_var2 = String.valueOf(var2);

        StringBuilder sb_var = new StringBuilder(st_var);
        StringBuilder sb_var2 = new StringBuilder(st_var2);

        sb_var.reverse();
        sb_var2.reverse();

        var = Integer.parseInt(sb_var.toString());
        var2 = Integer.parseInt(sb_var2.toString());

        if (var>var2)
            System.out.println(var);
        else
            System.out.println(var2);
    }
}