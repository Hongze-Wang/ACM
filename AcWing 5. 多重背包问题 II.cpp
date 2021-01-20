// AcWing 5. 多重背包问题 II

// AcWing 4. 多重背包问题I 解法超时
// 1000 * 2000 * 2000 = 4,000,000,000 = 4e9
// #include <bits/stdc++.h>
// using namespace std;

// const int maxn = 2005;

// int main() {
//     int n, m;
//     int v, w, s;
//     int dp[maxn];
    
//     cin >> n >> m;
//     for(int i=0; i<n; i++) {
//         cin >> v >> w >> s;
//         for(int j=m; j>=v; j--) {
//             for(int k=1; k<=s && k*v<=j; k++) {
//                 dp[j] = max(dp[j], dp[j-k*v] + k*w);
//             }
//         }
//     }
//     cout << dp[m] << endl;
//     return 0;
// }

// 二进制拆分
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m;
    int v[1001], w[1001], s[1001];
    int dp[2001], a[24000], b[24000]; // 2^12 > 2000 最多能拆12个
    int total = 0;
    // memset(dp, 0, sizeof(dp));
    cin >> n >> m;
    for(int i=0; i<n; i++) {
        cin >> v[i] >> w[i] >> s[i];
    }
    // 二进制拆分
    for(int i=0; i<n; i++) {
        for(int j=1; j<s[i]; j<<=1) {
            a[total] = j * v[i];
            b[total++] = j * w[i];
            s[i] -= j;
        }
        if(s[i]) {
            a[total] = s[i] * v[i];
            b[total++] = s[i] * w[i];
        }
    }
    // 01背包解法
    for(int i=0; i<total; i++) {
        for(int j=m; j>=a[i]; j--) {
            dp[j] = max(dp[j], dp[j-a[i]] + b[i]);
        }
    }
    
    cout << dp[m] << endl;
    return 0;
}
