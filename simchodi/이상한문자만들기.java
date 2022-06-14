class Solution {
    public String solution(String s) {
        String answer = "";
        s = s.toLowerCase();
        
        char[] s_char = s.toCharArray();
        int index = 0;
        int inner_index = 0;
        while(index < s_char.length){
            if(s_char[index] == ' '){
                inner_index = -1;
            }
            if(inner_index % 2 == 0){
                s_char[index] = Character.toUpperCase(s_char[index]);
            }
            answer += s_char[index];
            index++;
            inner_index++;
        }
        
        return answer;
    }
}
