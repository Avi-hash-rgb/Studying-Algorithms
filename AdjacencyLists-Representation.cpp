#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

int32_t main() {
    // int n; cin >> n; 
    // vector<vector<int>> adj(n + 1);

    // storing items in an adjacency list.

    // Hardcoded version
    // adj[1].push_back(2);
    // adj[2].push_back(3); 
    // adj[2].push_back(4);
    // adj[3].push_back(4);
    // adj[4].push_back(5);

    // Manual Input Version:-
    int n, m;
    cout << "No of vertices (n) and edges (m): "; cin >> n >> m;

    vector<vector<int>> adj(n + 1);
    cout << "Enter " << m << " lines of edges (u v): " << endl;

    for(int i = 0; i < m; i++){
        int u, v; cin >> u >> v;
        adj[u].push_back(v); // Directed edge u -> v.
    }

    cout << endl << "<----- Adjacency List ----->" << endl;
    for(int i = 1; i <= n; i++){
        cout << i << " -> ";
        for(int neighbour: adj[i]) cout << neighbour << " ";
        cout << endl;
    }
}