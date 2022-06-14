import java.lang.Math;

class Solution {
    public long solution(long n) {
        long answer = 0;
        double sq = Math.sqrt(n);
        if(Math.round(sq) == Math.sqrt(n)){
            return (long)Math.pow((sq+1),2);
        }
        return -1;
    }
}
