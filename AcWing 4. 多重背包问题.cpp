// AcWing 4.多重背包问题 标准解法

#include <bits/stdc++.h>

const int maxn = 10005;

using namespace std;

int main() {
    int n, m;
    int v, w, s;
    int dp[maxn];
    cin >> n >> m;
    for(int i=0; i<n; i++) {
        cin >> v >> w >> s;
        for(int j=m; j>=v; j--) {
            for(int k=1; k<=s && k*v<=j; k++) {
                dp[j] = max(dp[j], dp[j-v*k]+w*k);
            }
        }
    }
    cout << dp[m] << endl;
    return 0;
} 
