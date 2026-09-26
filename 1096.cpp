#include <functional>
#include <set>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  vector<string> braceExpansionII(string expression) {
    int cursor = 0;

    function<int(int pos)> operation = [&expression](int pos) -> int {
      if (pos >= expression.length()) {
        return 0;
      } else if (expression[pos] == ',') {
        return 1;
      } else {
        return 2;
      }
    };

    function<set<string>(set<string> a, set<string> b, int op)> apply_operation = [&expression](set<string> a, set<string> b, int op) -> set<string> {
      if (op == 1) {
        set<string> words(a.begin(), a.end());
        words.insert(b.begin(), b.end());
        return words;
      } else {
        set<string> new_words;
        for (auto word : a) {
          for (auto word2: b) {
            new_words.insert(word + word2);
          }
        }
        return new_words;
      }
    };

    function<tuple<set<string>, int>(int start)> helper = [&helper, &expression, &operation, &apply_operation](int start) -> tuple<set<string>, int> {
      if (start >= expression.length()) {
        return {{""}, start};
      }

      set<string> res;
      int ptr = start;
      set<string> cur_comma_res = {""};
      while (ptr < expression.length()) {
        switch (expression[ptr]) {
          case '{': {
            auto [res, resume] = helper(ptr+1);
            ptr = resume;
            cur_comma_res = apply_operation(cur_comma_res, res, 2);
            break;
          }
          case '}': {
            res = apply_operation(res, cur_comma_res, 1);
            return {res, ptr};
          }
          case ',': {
            res = apply_operation(res, cur_comma_res, 1);
            cur_comma_res = {""};
            break;
          }
          default: {
            auto new_word = {string(1, expression[ptr])};
            cur_comma_res = apply_operation(cur_comma_res, new_word, 2);
          }
        }
        ptr++;
      }
      res = apply_operation(res, cur_comma_res, 1);
      return {res, ptr};
    };

    auto [res, ptr] = helper(0);
    return vector<string>(res.begin(), res.end());
  }
};
