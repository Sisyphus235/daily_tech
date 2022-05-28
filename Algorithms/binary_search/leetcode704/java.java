package Algorithms.binary_search.leetcode704;

class Java {
    public int solutionOpen(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int middle = (left + right) / 2;
            if (target == nums[middle]) {
                return middle;
            } else if (nums[middle] > target) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        return -1;
    }

    public int solutionClose(int[] nums, int target) {
        int left = 0;
        int right = nums.length;
        while (left < right) {
            int middle = left + ((right - left) >> 1);
            if (target == nums[middle]) {
                return middle;
            } else if (nums[middle] > target) {
                right = middle;
            } else {
                left = middle + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {

    }
}