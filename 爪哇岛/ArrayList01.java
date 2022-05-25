package xuexijava.caishuzi;

import java.util.ArrayList;

public class ArrayList01 {
    public static void main(String[] args){
        ArrayList<String> list = new ArrayList<>();
        System.out.println(list);
        //像集合中添加数据
        boolean success= list.add("哈哈哈");
        System.out.println(list);
        //查看添加动作是否成功
        System.out.println(success);

        list.add("哈哈哈");
        list.add("啊啊啊");
        list.add("黑猫警长");
        list.add("大耳贼");

        System.out.println(list);
        //返回对应位置的数据
        String name = list.get(2);
        System.out.println(name);
        //删除对应位置的数据
        String remo = list.remove(3);
        //查看删除的数据
        System.out.println(remo);
        //查看集合的长度
        int size = list.size();
        System.out.println(size);
    }
}
