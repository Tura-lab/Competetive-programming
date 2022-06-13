class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int j = 0;
        int i = 0;
        int total = 0;
        boolean found = false;
        int ans=0;
        
        while (j<nums.length && total + nums[j] < target){
            total += nums[j];
            j+=1;
        }
        if (j<nums.length){
            found=true;
        }
        
        while (j<nums.length){
            total -= nums[i];
            i+=1;
            total += nums[j];
            
            while (total >= target){
                found = true;
                total -= nums[i];
                i+=1;
            }
            
            j+=1;
        }
        
        
    return !found ? 0 : j-i+1;  
    }
}