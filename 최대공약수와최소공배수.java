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
                if(!yaksu_map.containsKey(yaksu.get(i))){   //map에 아직 안넣었으면
                    yaksu_map.put(yaksu.get(i),1);
                }else if(yaksu_map.containsKey(yaksu.get(i))){   //map에 있으면 안넣었으면
                    int plus = Integer.parseInt(yaksu_map.get(yaksu.get(i))+"");
                    yaksu_map.put(yaksu.get(i),plus+1);
                }
            }
        }
        return yaksu_map;
    }
    
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        
        ArrayList n_yaksu = makeYaksu(n);
        ArrayList n_yaksu_same = makeYaksu(n);
        ArrayList m_yaksu = makeYaksu(m);
        
        HashSet n_yaksu_set = new HashSet();
        HashSet m_yaksu_set = new HashSet();
        n_yaksu_set.addAll(n_yaksu);
        m_yaksu_set.addAll(m_yaksu);
        
        HashMap n_yaksu_map = countYaksu(n_yaksu_set, n_yaksu);
        HashMap m_yaksu_map = countYaksu(m_yaksu_set, m_yaksu);
        
        //교집합(최대공약수) > 없으면 1리턴
        n_yaksu_same.retainAll(m_yaksu);
        if(n_yaksu_same.size() == 0){
            answer[0] = 1;
        }else{
            int multi = 1;
            for(int i = 0; i < n_yaksu_same.size(); i++){
                multi = Integer.parseInt(n_yaksu_same.get(i) + "") * multi;
            }
            answer[0] = multi;
        }
        
        //차집합(최소공배수)
        n_yaksu.removeAll(n_yaksu_same);
        m_yaksu.removeAll(n_yaksu_same);
        n_yaksu.addAll(m_yaksu);
        n_yaksu.addAll(n_yaksu_same);
        
        int multi = 1;
        for(int i = 0; i < n_yaksu.size(); i++){
            multi = Integer.parseInt(n_yaksu.get(i) + "") * multi;
        }
        answer[1] = multi;
        
        
        return answer;
    }
}
