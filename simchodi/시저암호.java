class Solution {
    public String solution(String s, int n) {
        String answer = "";
        char[] tmp = s.toCharArray(); 
        for (char t : tmp){
            if(t == ' '){ //공백
                answer += " ";
                continue;
            }else if((int)t >= 65 && (int)t <= 90){   //대문자
                if((int)t + n > 90){
                    answer += Character.toString(((int)t + n) - 26);
                    continue;
                }
            }else if((int)t >= 97 && (int)t <= 122){  //소문자
                if((int)t + n > 122){
                    answer += Character.toString(((int)t + n) - 26);
                    continue;
                }
            }
            answer += Character.toString((int)t+n);
        }
        return answer;
    }
}
