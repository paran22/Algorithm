// 입력 : 첫번째 줄 : 총 기술 사용 횟수 N 
//       두번째 줄 : 공백없이 N 개의 기술

// 로직 :  연계 기술 : L -> R, S -> K   (사전 기술 없이 본 기술 사용 x )
//         연계 x  : 1~ 9 
//         -> 연계를 제대로 했거나, 연계없이 사용할수 있는 기술이 나오면 카운트 증가
//         -> 연계 기술은 사전 기술과 본 기술이 다 사용되야 하나의 기술로 간주하고 카운트 증가
//         -> 연계 꼬이면 거기서 멈춤 

// 출력 : 정상적으로 기술을 사용한 총 횟수


import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int repearNum = Integer.parseInt(br.readLine());
        String script = br.readLine();
        
        int skillCount = 0;
        //사전 기술 대기용 버퍼
        List<Character> buffers = new ArrayList<>();
        
        for (int i = 0; i < repearNum; i++) {
            char skill = script.charAt(i);
            
            // L , S 는 버퍼 추가 그냥 
            if (skill == 'L' || skill == 'S') {
                buffers.add(skill);
            } 
            // R K  는 버퍼 확인해서 사전 기술있는지 확인
            else if (skill == 'R' || skill == 'K') {
                // 버퍼 비어 있으면 확인 필요 없이 바로 종료
                if (buffers.isEmpty()) {
                    System.out.println(skillCount);
                    return;
                }

                // 연계기 확인
                boolean isClear = true;
                char requiredSkill = (skill == 'R') ? 'L' : (skill == 'K') ? 'S' : 0;

                for (int j = buffers.size() - 1; j >= 0; j--) {
                    char target = buffers.get(j);
                    if (target == requiredSkill) {
                        buffers.remove(j);
                        skillCount++;
                        isClear = false;
                        break;
                    }
                }

                // 연계기 못 찾았으면 종료
                if (isClear) {
                    System.out.println(skillCount);
                    return;
                }
            } 
            // 1 ~ 9는 그냥 카운트
            else {
                skillCount++;
            }
        }
        System.out.println(skillCount);
    }
}