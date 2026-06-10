#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n;
    if(n == 0){
        cout << 0;
    }

    int count = 0;
    
    while(n != 0){
        if(n % 2 == 0){
            n /= 2;
        } else {
            n -= 1;
        }

        count++;
    }

    cout << count;
}