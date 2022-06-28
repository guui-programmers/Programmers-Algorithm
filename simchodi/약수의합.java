import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        int n_yaksu = n;
        
        while(n_yaksu > 0){
            if (n % n_yaksu == 0){
                answer += n_yaksu;
            }
            n_yaksu--;
        }
        return answer;
    }
}
