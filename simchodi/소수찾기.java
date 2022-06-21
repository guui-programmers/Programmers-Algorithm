class Solution {
    public int solution(int n) {
        int answer = 0;
        
        while(n > 2){
            int count = 0;
            for(int i = 2; i * i <= n; i++){
                if(n % i == 0 && n != i){ 
                    count++;
                    break;
                }
            }
            if(count == 0){
                answer += 1;
            }
            n--;
        }
        return answer+1;
    }
}
