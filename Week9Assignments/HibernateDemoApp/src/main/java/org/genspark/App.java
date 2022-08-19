package org.genspark;

import org.genspark.Entity.Employee;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import org.hibernate.query.Query;

import java.util.List;

public class App
{
    public static void main( String[] args )
    {
        System.out.println("Welcome to DB");
        Configuration cfg = new Configuration();
        cfg.configure("hibernate.cfg.xml");
        SessionFactory factory = cfg.buildSessionFactory();

        Session session = factory.openSession();

        Transaction tx = session.beginTransaction();

        Query q = session.createQuery("update Employee set name=:n where id=:i");
        q.setParameter("n", "Udit Kumar");
        q.setParameter("i", 1);
        int status = q.executeUpdate();
        System.out.println(status);
    }
}
