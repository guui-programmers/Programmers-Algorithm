class Solution {
    public String solution(String phone_number) {
        String answer = "";
        String starChar = phone_number.substring(phone_number.length()-4,phone_number.length()); //뒷4자리 문자열 추출
        System.out.println(starChar);
        for(int i=0;i<phone_number.length()-4;i++){
            answer+="*";
        }
        return answer+starChar;
    }
}