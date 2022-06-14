class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        if (arr.length == 1){
            answer = new int[1];
            answer[0] = -1;
        }else{
            // 작은 수 찾는
            answer = new int[arr.length-1];
            int min = arr[0];
            for (int i = 0; i < arr.length; i++) {
                for (int j = i+1; j < arr.length; j++) {
                    if (min > arr[j]){
                        min = arr[j];
                    }
                }
            }
            int index = 0;
            for (int i:arr){
                if(i != min){
                    answer[index] = i;
                    index++;
                }
            }
        }
        return answer;
    }
}
