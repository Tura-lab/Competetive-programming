public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        
        int ans = 0;
        
        for (int i = 0; i<32; i++){
            int num = 0;
            
            if ((n & (1 << i)) != 0){
                num = 1;
            }
            ans |= (num << (31-i));
        }
        
        return ans;
    }
}