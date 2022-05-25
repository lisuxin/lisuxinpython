package xuexijava.caishuzi;

import java.util.ArrayList;

public class Student01 {
    public static void main(String[] args) {
        ArrayList<Student> list = new ArrayList<>();
        Student stu = new Student("哈哈",20);
        Student sta = new Student("嘿嘿",21);
        Student stb = new Student("丫丫",22);
        Student stc = new Student("呀呀",23);
//        //set是重新赋值
//        stu.setName("哈哈");
//        Student a = stu.getName();
//        list.add(a);
//        stu.setAge(20);
//        stu.setName("嘿嘿");
//        stu.setAge(21);
//        stu.setName("丫丫");
//        stu.setAge(22);
        list.add(stu);
        list.add(sta);
        list.add(stb);
        list.add(stc);

        for (int i = 0; i < list.size(); i++) {
            Student a = list.get(i);
            System.out.println(a.getName()+a.getAge());
        }
    }
}
