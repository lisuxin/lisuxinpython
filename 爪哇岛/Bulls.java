package xuexijava.caishuzi;

import java.util.Scanner;

public class Bulls {
    Scanner scanner = new Scanner(System.in);

    private int num;//随机数

    public Bulls() {
    }

    public Bulls(int num) {
        this.num = num;
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public int Show() {
        while (true) {
            int nul =scanner.nextInt();
            if (nul < num) {
                System.out.println("小");
            } else if (nul > num) {
                System.out.println("大");
            } else {
                System.out.println("对");
                break;
            }
        }
        return 1;
    }
}
