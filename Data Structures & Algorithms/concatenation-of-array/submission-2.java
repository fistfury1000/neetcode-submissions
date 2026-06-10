class Solution {
    public int[] getConcatenation(int[] nums) {
        int poop [] = new int[2*nums.length];
        for(int i =0; i<nums.length; i++){
            poop[i] = nums[i];
            poop[i+(nums.length)]=nums[i];
        }
        return poop;
    }
}