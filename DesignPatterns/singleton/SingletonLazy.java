package singleton;

/**
 * 懒汉模式
 */
public class SingletonLazy {

    private static volatile SingletonLazy instance;

    private SingletonLazy() {
        if (instance != null) {
            // 防止反射攻击问出
            throw new RuntimeException();
        }
    }

    public static SingletonLazy getInstance() {
        if (instance == null) {
            // 线程安全
            synchronized (SingletonLazy.class) {
                // 并发情况下，可能多个线程阻塞在上面一行，某个线程完成创建后，避免重复创建，进行二次校验
                if (instance == null) {
                    instance = new SingletonLazy();
                }
            }
        }
        return instance;
    }
}
