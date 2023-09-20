import java.util.*;
public class Main {
    public static void main(String[] args) {
        int[] nums = {1,2,3};
        List<List<Integer>> subsets = findSubsets(nums);

        // Print all subsets
        int maxi = Integer.MIN_VALUE;
        for (List<Integer> subset : subsets) {
            if(subset.size()!=0){
            int sum=0;
            for (int num : subset) {
                sum=0;
                for(int i=0;i<subset.size();i++){
                    sum += 1*subset.get(i);
                }
                maxi = Math.max(maxi,Math.abs(sum));
            }
            System.out.println(subset+" "+sum);
        }
        }
        System.out.println("Maximum: "+maxi);
    }

    public static List<List<Integer>> findSubsets(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        generateSubsets(nums, 0, new ArrayList<>(), subsets);
        return subsets;
    }

    private static void generateSubsets(int[] nums, int index, List<Integer> current, List<List<Integer>> subsets) {
        if (index == nums.length) {
            // Add the current subset to the list of subsets
            subsets.add(new ArrayList<>(current));
            return;
        }

        // Include the current element in the subset
        current.add(nums[index]);
        generateSubsets(nums, index + 1, current, subsets);

        // Exclude the current element from the subset
        current.remove(current.size() - 1);
        generateSubsets(nums, index + 1, current, subsets);
    }
}
