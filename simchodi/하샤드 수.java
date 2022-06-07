class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        String xString = x+""; // x를 String으로 바꿔서 
        int sum = 0;           // 한자리씩 덧셈해서 sum에 저장예정
        for(int i=0;i<xString.length();i++){
            sum += (int)Character.getNumericValue(xString.charAt(i));
            // char -> int로 형변환 하면 아스키코드 값이 나와서
            // 숫자의미 그대로의 int로 변환
        }
        System.out.println(sum);
        if(x%sum!=0){
            answer = false;
        }
        return answer;
    }
}