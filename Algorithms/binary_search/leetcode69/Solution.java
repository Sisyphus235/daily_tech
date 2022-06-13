public class Solution {
    public int mySqrt(int x) {
        int left = 0;
        int right = x;
        int result = -1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            long target = mid * mid;
            if (target <= x) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return result;
    }
}
