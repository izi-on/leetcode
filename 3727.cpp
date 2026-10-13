#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
      sort(nums.begin(), nums.end(), [](const auto& a, const auto& b) {return abs(a) < abs(b);});
      long long ans = 0l;
      for (int i = 0; i < nums.size() / 2; i++) {
        ans += (long long) nums[nums.size() - i - 1] * (long long) nums[nums.size() - i - 1];
        ans -= (long long) nums[i] * (long long) nums[i];
      }
      if (nums.size() % 2 == 1) ans += (long long) nums[nums.size()/2] * (long long) nums[nums.size()/2];
      return ans;
    }
};
