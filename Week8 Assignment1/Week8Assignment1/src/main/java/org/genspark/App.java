package org.genspark;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App
{
    public static void main(String[] args)
    {
        //Should print out the details of the student that the bean creates
        ApplicationContext contextAdd = new AnnotationConfigApplicationContext(AppConfig.class);
        Address add = (Address) contextAdd.getBean(Address.class);
        System.out.println(add);

        ApplicationContext contextStu = new ClassPathXmlApplicationContext("Spring.xml");
        Student stu = (Student) contextStu.getBean("Student");
        System.out.println(stu);

        ApplicationContext contextPho = new AnnotationConfigApplicationContext(AppConfig.class);
        Phone pho = (Phone) contextPho.getBean(Phone.class);
        System.out.println(pho);
    }
}
