
import java.util.*;
import java.io.*;

public class BackJoon_5052 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            Trie trie = new Trie();
            boolean check = true;

            int N = Integer.parseInt(br.readLine());
            List<String> list = new ArrayList<>();
            for (int n = 0; n < N; n++) { // 처음에는 넣고
                String val = br.readLine();
                trie.insert(val, 0);
                list.add(val);
            }
            for (int i = 0; i < list.size(); i++) { // 다시 돌려보면서 확인
                if (!trie.Find(list.get(i), 0)) {
                    check = false;
                }
            }
            if (check) {
                System.out.println("YES");
            } else {
                System.out.println("NO");

            }
        }
    }

    static class Trie {
        // boolean end; // 어차피 다시 돌려보면서 확인할거기에 end는 굳이 필요X
        boolean pass;
        Trie[] childs;

        Trie() {
            // end = false;
            pass = false;
            childs = new Trie[10];
        }

        public void insert(String str, int idx) {
            if (idx == str.length()) {
                // end = true;
                return;
            }
            int cur = str.charAt(idx) - '0';
            if (childs[cur] == null) {
                childs[cur] = new Trie();

            }
            pass = true;

            childs[cur].insert(str, idx + 1);
        }

        public boolean Find(String str, int idx) {
            if (idx == str.length()) { // 현재 문자열 끝까지 왔는데 뒤에 자식 노드가 더 있으면
                // 다른 번호의 접두어로 된다는 뜻이기에
                if (pass)
                    return false;
                else
                    return true;
            }
            int cur = str.charAt(idx) - '0';
            return childs[cur].Find(str, idx + 1);

        }
    }

}
