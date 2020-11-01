# include "bits/stdc++.h"
 
using namespace std;
 
#define endl "\n"
typedef long long int ll;
#define f first
#define s second
 
#define SEND_HELP ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
 
// DEBUG
void __print(int x) { cerr << x; }
void __print(ll x) { cerr << x; }
void __print(double x) { cerr << x; }
void __print(char x) { cerr << '\'' << x << '\''; }
void __print(const string& x) { cerr << '\"' << x << '\"'; }
void __print(const char* x) { cerr << '\"' << x << '\"'; }
void __print(bool x) { cerr << (x ? "true" : "false"); }
 
template<typename T, typename V>
void __print(const pair<T, V>& x) { cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}'; }
template<typename T>
void __print(const T& x) { int _ = 0; cerr << '{'; for (auto& i : x) cerr << (_++ ? "," : ""), __print(i); cerr << "}"; }
void _print() { cerr << "]\n"; }
template <typename T, typename... V>
void _print(T t, V... v) { __print(t); if (sizeof...(v)) cerr << ", "; _print(v...); }
#ifndef ONLINE_JUDGE
    #define dbg(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
    #define dbg(x...)
#endif
 
ll INF = 2e17;
ll MOD = 1e9+7;

int w, n;
vector<ll> x;

void solve(int ntc) {
	x.clear();
	cin >> w >> n;
	x.resize(w);
	for(int i = 0; i < w; ++ i)
		cin >> x[i];
	sort(x.begin(), x.end());

	vector<ll> pre(1);
	for(auto it : x) {
		pre.push_back(pre.back() + it);
	}


	ll moves = 1e18;
	// better to land at one of the x?
	for(int at = 0; at < w; ++ at) {

		ll choose = x[at];
		// i will settle at this
		// binary search left for finding the position till it's better to turn anti
		int lo = 0;
		int hi = at - 1;
		int lpos = -1;
		while(lo <= hi) {
			int mid = (lo + hi) >> 1;
			ll clok = (choose - x[mid]);
			ll anti = (n - choose + x[mid]);
			if(anti < clok) {
				lpos = mid;
				lo = mid + 1;
			}
			else {
				hi = mid - 1;
			}
		}
		// binary search right for the same reason, till better to turn clok
		lo = at + 1;
		hi = w - 1;
		int rpos = -1;
		while(lo <= hi) {
			int mid = (lo + hi) >> 1;
			ll anti = (x[mid] - choose);
			ll clok = (n - x[mid] + choose);
			if(clok < anti) {
				rpos = mid;
				hi = mid - 1;
			}
			else {
				lo = mid + 1;
			}
		}

		ll here = 0;

		// calc left
		if((at >= 1) && lpos != -1) {
			ll antisuml = pre[lpos + 1];
			// all will move to 1 first and then to choose
			ll antinl = lpos + 1;
			ll antiml = antisuml + antinl * (n - choose);
			here += antiml;
		}
		// lpos + 1 ---> at - 1
		if(at >= 1 && (lpos + 1) <= (at - 1)) {
			ll cloksuml = pre[at] - pre[lpos + 1];
			ll cloknl = (at - 1) - (lpos + 1) + 1;
			ll clokml = cloknl * (choose) - cloksuml;
			here += clokml;
		}

		// calc right
		if((at < w - 1) && rpos != -1) {
			// rpos --> w - 1
			ll cloksumr = pre[w] - pre[rpos];
			ll cloknr = (w - 1) - (rpos) + 1;
			ll clokmr = cloknr * (n + choose) - cloksumr;
			here += clokmr;
 		}
		if(rpos == -1)
			rpos = w;
		if((at < w - 1) && ((rpos - 1) >= (at + 1))) {
			// at + 1 ---> rpos - 1
			ll antisumr = pre[rpos] - pre[at + 1];
			ll antinr = (rpos - 1) - (at + 1) + 1;
			ll antimr = antisumr - antinr * (choose);
			here += antimr;
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
