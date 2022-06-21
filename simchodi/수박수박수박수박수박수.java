class Solution {
    public String solution(int n) {
        String answer = "";
        int index = 0;
        
        while(index < n){
            String imsi = (index % 2 == 0) ? "수" : "박";
            answer += imsi;
            index ++;
        }
        return answer;
    }
}
