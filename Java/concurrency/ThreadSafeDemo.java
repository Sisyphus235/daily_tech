package Java.concurrency;


public class ThreadSafeDemo {
    public class MutablePoint {
        public int x, y;

        public MutablePoint() {
            x = 0;
            y = 0;
        }

        public MutablePoint(MutablePoint p) {
            this.x = p.x;
            this.y = p.y;
        }

        public MutablePoint(int x, int y) {
            this.x = x;
            thix.y = y;
        }
    }

    public class MonitorVehicleTracker {
        private final Map<String, MutablePoint> locations;

        public MonitorVehicleTracker(Map<String, MutablePoint> locations) {
            this.locations = deepCopy(locations);
        }

        public synchronized Map<String, MutablePoint> getLocations() {
            return deepCopy(locations);
        }

        public synchronized void setLocations(String id, int x, int y) throws IllegalAcccessException {
            MutablePoint location = locations.get(id);
            if (location == null) {
                throw new IllegalAccessException("Invalid Id " + id);
            }
            location.x = x;
            location.y = y;
        }

        public Map<String, MutablePoint> deepCopy(Map<String, MutablePoint> m) {
            Map<String, MutablePoint> result = new HashMap<String, MutablePoint>(m.size());
            for (String id : m.keySet()) {
                result.put(id, m.get(id));
            }
            return result;
        }
    }
}