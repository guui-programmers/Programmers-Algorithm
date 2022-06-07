class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int all_length = arr1.length;
        int one_length = arr1[0].length;
        // [3][2] {{1,2},{2,3},{3,4}}
        int[][] answer = new int[all_length][one_length];
        for(int i=0;i<all_length;i++){
            for(int j=0;j<one_length;j++){
                answer[i][j]=arr1[i][j]+arr2[i][j];
            }
        }
        return answer;
    }
}