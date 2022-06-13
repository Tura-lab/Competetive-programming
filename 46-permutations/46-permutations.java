class Solution {
    
    public static void permutations(int[] nums, int size, List<Integer> yet, List<List<Integer>> ans){
        if (yet.size() == nums.length){ 
            ans.add(new ArrayList<Integer>(yet)); 
        }
        
        for (int num: nums){
            if (!yet.contains(num)){
                yet.add(num);
                permutations(nums, size, yet, ans);
                yet.remove(yet.size()-1);
            }
        }
    }
    
    
    public List<List<Integer>> permute(int[] nums) {
        
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        
        permutations(nums, 0, new ArrayList<Integer>(), ans);
        
        return ans;
        
        
    }
}