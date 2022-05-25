package xuexijava.caishuzi;

import java.util.Random;

public class Bulls01 {
    public static void main(String[] args) {
        Bulls bulls = new Bulls();
        Random random = new Random();
        System.out.println("猜数字");
        System.out.println("请输入一个0-10之间的数字");
        int s = random.nextInt(11);
        bulls.setNum(s);
        bulls.Show();
    }
}
