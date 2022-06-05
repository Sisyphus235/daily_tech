package Algorithms.binary_search.leetcode704;

import java.util.ArrayList;
import java.util.Arrays;

class Solution {
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

    public static void testCases() {
        ArrayList<ArrayList> testCases = new ArrayList<>();
        ArrayList testCase1 = new ArrayList<>();
        testCase1.add(new int[] { -1, 0, 3, 5, 9, 12 });
        testCase1.add(9);
        testCase1.add(4);
        testCases.add(testCase1);
        testCase1.add(new int[] { -1, 0, 3, 5, 9, 12 });
        testCase1.add(9);
        testCase1.add(4);
        ArrayList testCase2 = new ArrayList<>();
        testCases.add(testCase2);
        testCase2.add(new int[] { -1, 0, 3, 5, 9, 12 });
        testCase2.add(2);
        testCase2.add(-1);
        testCases.add(testCase2);
        ArrayList testCase3 = new ArrayList<>();
        testCases.add(testCase3);
        testCase3.add(new int[] {});
        testCase3.add(2);
        testCase3.add(-1);
        testCases.add(testCase3);
        ArrayList testCase4 = new ArrayList<>();
        testCases.add(testCase4);
        testCase4.add(new int[] { 1 });
        testCase4.add(1);
        testCase4.add(0);
        testCases.add(testCase4);
        ArrayList testCase5 = new ArrayList<>();
        testCases.add(testCase4);
        testCase5.add(new int[] { 1 });
        testCase5.add(0);
        testCase5.add(-1);
        testCases.add(testCase5);

        for (ArrayList testCase : testCases) {
            int[] nums = (int[]) testCase.get(0);
            int target = (int) testCase.get(1);
            int expected = (int) testCase.get(2);
            Solution solution = new Solution();
            int actualOpen = solution.solutionOpen(nums, target);
            if (actualOpen != expected) {
                System.out.println("Test failed: " + testCase);
                System.out.println("Expected: " + expected);
                System.out.println("Actual: " + actualOpen);
            }
            int actualClose = solution.solutionClose(nums, target);
            if (actualOpen != expected) {
                System.out.println("Test failed: " + testCase);
                System.out.println("Expected: " + expected);
                System.out.println("Actual: " + actualClose);
            }
        }
    }

    public static void main(String[] args) {
        testCases();
    }
}