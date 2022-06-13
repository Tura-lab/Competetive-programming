class Solution {
    public int minOperations(int[] nums, int x) {
        int total = 0;
        int i=0;
        boolean found = false;
        int final_ans = nums.length;
        
        while(i<nums.length){
            if (total + nums[i] > x){
                i-=1;
                break;
            }
            else if (total + nums[i] == x){
                found = true;
                total += nums[i];
                final_ans = Math.min(final_ans, i+1);
                break;
            }
            total += nums[i];
            i+=1;
        }
        
        
        if (i==nums.length){
            return !found ? -1 : final_ans;
        } 
        
        // System.out.println(i + " " + final_ans);
        for (int j=nums.length-1; j>-1; j--){
            while (i>-1 && total + nums[j] > x){
                total -= nums[i]; 
                i-=1;
            }
            
            total += nums[j];
            if (total == x){
                found=true;
                final_ans = Math.min(final_ans, nums.length-j+i+1);
            }
            else if (total > x){
                return !found ? -1 : final_ans;
            }
            // System.out.println(total + " " + i + " " + j + " " + final_ans);
                        
        }
        return !found ? -1 : final_ans;
    }
}