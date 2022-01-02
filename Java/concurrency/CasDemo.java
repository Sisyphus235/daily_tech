package Java.concurrency;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class CasDemo {
    private AtomicInteger atomicI = new AtomicInteger(0);
    private int i = 0;

    private void safeCount() {
        for (;;) {
            int i = atomicI.get();
            boolean result = atomicI.compareAndSet(i, ++i);
            if (result) {
                break;
            }
        }
    }

    private void unsafeCount() {
        i++;
    }

    public static void main(String[] args) {
        final CasDemo casDemo = new CasDemo();
        List<Thread> threadList = new ArrayList<Thread>(600);
        long start = System.currentTimeMillis();
        for (int j = 0; j < 100; j++) {
            Thread t = new Thread(new Runnable() {
                @Override
                public void run() {
                    for (int i = 0; i < 10000; i++) {
                        casDemo.unsafeCount();
                        casDemo.safeCount();
                    }
                }
            });
            threadList.add(t);
        }
        for (Thread t : threadList) {
            t.start();
        }
        for (Thread t : threadList) {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println(casDemo.i);
        System.out.println(casDemo.atomicI.get());
        System.out.println(System.currentTimeMillis() - start);
    }
}