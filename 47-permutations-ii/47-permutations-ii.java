class Solution {
    
    public static int count(int[] nums, int n){
        int count = 0;
        for (int num: nums){
            if (n==num){
                count+=1;
            }
        }
        
        return count;
    }
    
    public static void perms(Set<Integer> nums, List<Integer> yet, HashMap<Integer,Integer> seen, HashMap<Integer,Integer> counts, List<List<Integer>> ans, int total){
        if (total == yet.size() ){
            ans.add(new ArrayList<Integer>(yet));
            return;
        }
        for (int num: nums){
            // System.out.println(counts.get(num));
            // System.out.println(!seen.containsKey(num));
            if(!seen.containsKey(num) || seen.get(num)<counts.get(num)){
                //CHOOSE
                if (!seen.containsKey(num)){
                    seen.put(num, 1);
                }
                else{
                    seen.put(num, seen.get(num)+1);
                }
                yet.add(num);
                
                //EXPLORE
                perms(nums, yet, seen, counts, ans, total);
                
                //UNCHOOSE
                yet.remove(yet.size()-1);
                seen.put(num, seen.get(num)-1);
            }
        }
        
    }
    
    public List<List<Integer>> permuteUnique(int[] nums) {
        
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        HashMap<Integer,Integer> counts = new HashMap<Integer,Integer>();
        
        for (int num:nums){
            if (counts.containsKey(num)){
                continue;
            }
            counts.put(num, count(nums, num));
        }
        
        Set<Integer> numss = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        
        
        perms(numss, new ArrayList<Integer>(), new HashMap<Integer,Integer>(), counts, ans, nums.length); 
        
        return ans;
        
    }
}