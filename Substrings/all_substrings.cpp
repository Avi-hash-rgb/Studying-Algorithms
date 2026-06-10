#include<bits/stdc++.h>
using namespace std;

int main(){
    string s; cin >> s;
    for(int i = 0; i < s.size(); i++){
        for(int j = 1; j <= s.size() - i; j++){
            cout << s.substr(i, j) << endl;
        }
    }
}

// Most common substring operations in CP
// int demonstrations(){
    // string s = "competitive";
    // if(s.find("pet") != string::npos) cout << "Found";
// }

// s.substr(i, len) is not O(1), it takes O(len), where len is the length of the string.


// Golden mindset for string problems

// When solving substring problems, think in:

// start index
// end index
// length
// frequency
// window