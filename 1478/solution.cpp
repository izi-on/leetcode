#include <algorithm>
#include <cassert>
#include <functional>
#include <limits>
#include <map>
#include <string>
#include <utility>
#include <vector>
using namespace std;

using ll = long long;
using ld = long double;
using ull = unsigned long long;

using pii = pair<int,int>;
using pll = pair<ll,ll>;
using vi = vector<int>;
using vl = vector<ll>;
using vd = vector<double>;
using vld = vector<ld>;
using vs = vector<string>;

#define sz(x) (int)(x).size()
#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define rep(i,a,b) for (int i = (a); i < (b); ++i)
#define per(i,a,b) for (int i = (b) - 1; i >= (a); --i)
#define pb push_back
#define eb emplace_back
#define fi first
#define se second

class Solution {
public:
    int minDistance(vector<int>& houses, int k) {
      int n = houses.size();
      sort(houses.begin(), houses.end());
      vector<ll> psum(n+1, 0);
      for (int i = 0; i < n; i++) {
        psum[i+1] = psum[i] + houses[i];
      }


      map<pair<ll, ll>, ll> memo;

      auto bin_search = [&](ll target, ll left, ll right) {
        ll ans = left;
        while (left <= right) {
          ll mid = (left + right) / 2;
          if (houses[mid] <= target) {
            left = mid + 1;
            ans = mid;
          } else {
            right = mid - 1;
          }
        }
        return ans;
      };

      function<ll(ll i, ll k)> helper;
      helper = [&](ll i, ll k) {
        if (k == 0) {
          return psum[n] - psum[i] - houses[i-1]*(n - i);
        }

        if (i >= n) {
          return (ll) numeric_limits<int>::max();
        }

        if (memo.count({i, k}) > 0) {
          return memo[{i,k}];
        }

        ll best_placement = numeric_limits<int>::max();
        for (ll j = i; j < n; j++) {
          ll midpoint = (houses[i-1] + houses[j]) / 2;
          ll split_idx = bin_search(midpoint, i-1, j);
          ll cost = (psum[split_idx + 1] - psum[i] - (split_idx - i + 1) * houses[i-1])
                   + (houses[j] * (j - split_idx - 1) - (psum[j] - psum[split_idx + 1]));
          // cout << "_____" << endl;
          // cout << (psum[split_idx + 1] - psum[i] - (split_idx - i + 1) * houses[i-1]) << " " << houses[j] * (j - split_idx - 1) - (psum[j] - psum[split_idx + 1]) << endl;
          // cout << "for " << "(" << i-1 << "," << houses[i-1] << ") (" << j << "," << houses[j] << "): " << cost << ", split idx: " << split_idx << endl;
          // cout << "i: " << i << endl;
          // cout << "_____" << endl;
          best_placement = min(best_placement, cost + helper(j+1, k-1));
        }
        memo[{i,k}] = best_placement;
        return best_placement;
      };

      ll ans = numeric_limits<int>::max();
      for (ll i = 0; i < n; i++) {
        ll cost = i*houses[i] - psum[i];
        ans = min(ans, cost + helper(i+1, k-1));
      }
      return ans;
    }
};
