// Binary Exponenetiation
// The rule:

// a^n = if(n = 0) = 1
// if(n is even) = (a^(n/2))^2
// if(n is odd) = a * (a^((n - 1)/2))^2

// Let's take 3^13
// take the exponent part:
// 13
// 13 in binary = 1101(base 2)
// 13 = 8 + 4 + 0 + 1
// 3^13 = 3^8 * 3^4 * 3^1
// 3^13 = 3^(8 + 4 + 1)

// lets try to code this:

#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false); cin.tie(NULL);
#define endl "\n"

int main() {
    fastio;
    long long base, exponent; cin >> base >> exponent;
    long long res = 1;
    while(exponent > 0){
        if(exponent & 1) res *= base; base *= base; exponent >>= 1;
    }
    cout << res << endl;
}
