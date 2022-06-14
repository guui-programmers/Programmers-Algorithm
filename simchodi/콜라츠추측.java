class Solution {
    public int solution(int num) {
        int count = 0;
        long num2 = (long)num;
        while (num2 != 1){
            if (count==499){
                break;
            }
            if (num2 % 2 ==0){
                num2 = num2/2;
            }else{
                num2 = (num2 * 3) + 1;
            }
            count++;
        }
        return count==499?-1:count;
    }

}
