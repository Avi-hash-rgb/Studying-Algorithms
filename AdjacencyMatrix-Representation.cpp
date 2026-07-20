#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

int32_t main() {
    int n, m; cin >> n >> m;
    // where adj[n][n] tells us adj[a][b]
    vector<vector<int>> adj(n + 1, vector<int>(n + 1, 0));
    // Initialize an (n + 1) x (n + 1) matrix
    cout << "Enter " << m << " lines of edges (u v): " << endl;
    for(int i = 0; i < m; i++){
        int u, v; cin >> u >> v;
        adj[u][v] = 1;
    }
    cout << endl;
    cout << "<----- Adjacency Matrix ----->"; 
    cout << endl;

    cout << "  ";
    for(int j = 1; j <= n; j++) cout << j << ' ';
    cout << endl;
    for(int i = 1; i <= n; i++){
        cout << i << " ";
        for(int j = 1; j <= n; j++) cout << adj[i][j] << " ";
        cout << endl;
    }
}