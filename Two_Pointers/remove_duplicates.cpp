#include<bits/stdc++.h>
using namespace std;

int removeDuplicates(vector<int>& arr){
    sort(arr.begin(), arr.end());

    int slow = 0;
    for(int fast = 1; fast < arr.size(); fast++){
        if(arr[slow] != arr[fast]){
            slow++;
            arr[slow] = arr[fast];
        }
    }

    for(int i = 0; i <= slow; i++){
        cout << arr[i] << " ";
    }
}

int main(){
    int n; cin >> n;
    vector<int> arr(n);

    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    removeDuplicates(arr);
}

