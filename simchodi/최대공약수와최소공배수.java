import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;

class Solution {
    public ArrayList makeYaksu(int n){
        ArrayList yaksu = new ArrayList();
        int count = 0;
        
        while(true){
            if(n % 2 == 0 && n != 2){
                yaksu.add(2);
                count++;
                n = n/2;
            }else if(n % 3 == 0 && n != 3){
                yaksu.add(3);
                count++;
                n = n/3;
            }else if(n % 5 == 0 && n != 5){
                yaksu.add(5);
                count++;
                n = n/5;
            }else if(n % 7 == 0 && n != 7){
                yaksu.add(7);
                count++;
                n = n/7;
            }else{
                if(count == 0){
                    yaksu.add(1);
                    yaksu.add(n);
                    break;
                }
                if(n == 1){
                    break;
                }
                yaksu.add(n);
                break;
            }
            
        }
        return yaksu;
    }//makeYaksu
    
    public HashMap countYaksu(HashSet yaksu_set, ArrayList yaksu){
        HashMap yaksu_map = new HashMap();
        for(int i = 0; i < yaksu.size(); i++){
            if(yaksu_set.contains(yaksu.get(i))){ //set에 있는 값인데

