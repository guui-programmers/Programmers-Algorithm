class Solution {
    public int[] solution(long n) {
        int[] answer = new int[(n + "").length()];
        
        // int 배열에 하나씩 저장
        int index = 0;
        for(int i = ((n + "").length())-1; i >= 0; i--){
            answer[index++] = Integer.parseInt((n + "").substring(i,i+1));
        }
        int tmp = 0;
        return answer;
    }
}
