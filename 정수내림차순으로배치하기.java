class Solution {
    public long solution(long n) {
        String answer = "";
        int[] num_list = new int[(n + "").length()];
        
        // int 배열에 하나씩 저장
        for(int i = 0; i < (n + "").length(); i++){
            num_list[i] = Integer.parseInt((n + "").substring(i,i+1));
        }
        
        // sort
        int tmp = 0;
        for(int i = 0; i < num_list.length-1; i++){
            for(int j = i+1; j < num_list.length; j++){
                if(num_list[i] < num_list[j]){
                    tmp = num_list[i];
                    num_list[i] = num_list[j];
                    num_list[j] = tmp;
                }
            }
        }
        
        //answer에 붙이기
        for(int i = 0; i < num_list.length; i++){
            answer += num_list[i];
        }
        
        return Long.parseLong(answer);
    }
}
