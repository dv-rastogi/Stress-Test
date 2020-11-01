# include "bits/stdc++.h"
 
using namespace std;
 
#define endl "\n"
typedef long long int ll;
#define f first
#define s second
 
#define SEND_HELP ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
inline void setPrecision(int n){cout.precision(n);}
 
//DEBUG
#define BR cerr<<endl
#define dbg(x) cerr<<(#x)<<": "<<x<<endl
#define dbgV(x) cerr<<(#x)<<": "; for(auto it: x) cerr<<it<<" "; cerr<<endl;
#define dbgS(x) cerr<<(#x)<<": "; for(auto it: x) cerr<<it<<" "; cerr<<endl;
#define dbgM(x) cerr<<(#x)<<": "; for(auto it: x) cerr<<"["<<it.f<<", "<<it.s<<"] "; cerr<<endl;
#define dbg2D(x) cerr<<(#x)<<": \n"; for(auto y: x) { for(auto it: y) cerr<<it<<" "; cerr<<endl; } cerr<<endl;
#define dbgA(x, n) cerr<<(#x)<<": "; for(int i=0;i<n;++i) cerr<<x[i]<<" "; cerr<<endl;
#define dbgVP(x) cerr<<(#x)<<": "; for(auto it: x) cerr<<"["<<it.f<<", "<<it.s<<"] "; cerr<<endl;
 
ll INF = 1e10;
int MOD = 1e9+7;

int w, n;
vector<ll> x;

void solve(int ntc) {

	x.clear();
	cin >> w >> n;
	x.resize(w);
	for(int i = 0; i < w; ++ i)
		cin >> x[i];
	sort(x.begin(), x.end());

	ll moves = 1e18;
	for(auto choose : x) {
		ll here = 0;
		for(auto it : x) {
			if (it < choose) {
				here += min(choose - it, n - choose + it);
			}
			else {
				here += min(it - choose, n - it + choose);
			}
		}		
		moves = min(moves, here);	
	}

	cout << "Case #" << ntc << ": " << moves << endl;
}

int main() { 
	#ifndef ONLINE_JUDGE
        freopen("inputf.in", "r", stdin);
    #endif
    SEND_HELP

    int tt;
    cin >> tt;
    for(int ntc = 1; ntc <= tt; ++ ntc) {
    	solve(ntc);
    }

    return 0;
}

/*

*/