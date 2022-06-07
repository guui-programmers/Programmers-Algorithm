import java.util.*;

class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        for(int i=1;i<n+1;i++){
            answer[i-1]=(long)x*i;
        }
        
        /* 뭔가 에러가 있어서 다시 짠 코드 ↓ */
//         ArrayList<Long> arrayAnswer = new ArrayList<Long>();
//         for(int i=1;i<n+1;i++){
//             arrayAnswer.add((long)x*i);
//         }
        
//         int index = 0;
//         for(int i=0;i<arrayAnswer.size();i++){
//             answer[i] = arrayAnswer.get(i);
//         }
        
        return answer;
    }
}