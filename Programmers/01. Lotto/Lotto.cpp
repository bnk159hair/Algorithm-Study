#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int num_of_win = 0, num_of_zero = 0;
    for (int i = 0; i < lottos.size(); i++) {
        for (int j = 0; j < win_nums.size(); j++) {
            if (lottos[i] != 0 && lottos[i] == win_nums[j]) {
                num_of_win++;
            }
        }
        if (lottos[i] == 0)
            num_of_zero++;
    }
    int num_of_win_new = num_of_win + num_of_zero;
    if (num_of_win_new > 7)
        num_of_win_new = 6;


    if (num_of_win_new >= 2)
        answer.push_back(7 - num_of_win_new);
    else
        answer.push_back(6);

    if (num_of_win >= 2)
        answer.push_back(7 - num_of_win);
    else
        answer.push_back(6);
    return answer;
}