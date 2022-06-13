class Solution {
    
    public static void permutations(int[] nums, int size, List<Integer> yet, List<List<Integer>> ans, Set<Integer> seen){
        if (yet.size() == nums.length){ 
            ans.add(new ArrayList<Integer>(yet)); 
        }
        for (int num: nums){
            if (!seen.contains(num)){
                // Choose 
                yet.add(num);
                seen.add(num);
                
                // Explore
                permutations(nums, size, yet, ans, seen);
                
                // Unchoose
                seen.remove(num);
                yet.remove(yet.size()-1);
            }
        }
    }
    
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        permutations(nums, 0, new ArrayList<Integer>(), ans, new HashSet<Integer>());
        
        return ans;
        
        
    }
}