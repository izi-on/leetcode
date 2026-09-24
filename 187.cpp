#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  uint32_t encoding(char nt) {
    if (nt == 'A') {
      return 0;
    } else if (nt == 'C') {
      return 1;
    } else if (nt == 'G') {
      return 2;
    } else if (nt == 'T') {
      return 3;
    }
    return -1;
  }

  char decoding(uint32_t num) {
    if (num == 0) {
      return 'A';
    } else if (num == 1) {
      return 'C';
    } else if (num == 2) {
      return 'G';
    } else if (num == 3) {
      return 'T';
    }
    return -1;
  }

  string decode(uint32_t encoding) {
    string res = "";
    uint32_t mask = 0xC0000;
    for (int i = 0; i < 10; i++) {
      char nt = decoding((encoding & mask) >> (2 * ((10 - i)-1)));
      res += nt;
      mask = mask >> 2;
    }
    return res;
  }

  uint32_t encode(string &seq) {
    uint32_t enc = 0;
    for (char c : seq) {
      enc = enc << 2;
      enc += encoding(c);
    }
    return enc;
  }

  vector<string> findRepeatedDnaSequences(string s) {
    unordered_map<uint32_t, uint32_t> count;
    if (s.length() < 10) return {};
    auto bruh = s.substr(0, 10);
    uint32_t cur = encode(bruh);
    count[cur] += 1;
    for (int i = 10; i < s.length(); i++) {
      cur = ((cur & 0x3FFFF) << 2) + encoding(s[i]);
      count[cur] += 1;
    }

    vector<string> ans;
    for (auto &[key, value] : count) {
      if (value > 1) {
        ans.push_back(decode(key));
      }
    }

    return ans;
  }
};
