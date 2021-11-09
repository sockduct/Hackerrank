/* Enter your macros here */

#define toStr(x) #x
#define INF 1000000000
#define foreach(a, b) for (auto b; b < a.size(); ++b)
#define io(x) cin >> x
#define FUNCTION(a, b) void a(int& x, int y) { if (!(x b y)) x = y; }

// #include <iostream>
// #include <vector>
using namespace std;

#if !defined toStr || !defined io || !defined FUNCTION || !defined INF
#error Missing preprocessor definitions
#endif 

FUNCTION(minimum, <)
FUNCTION(maximum, >)

int main(){
	int n; cin >> n;
	vector<int> v(n);
	foreach(v, i) {
		io(v)[i];
	}
	int mn = INF;
	int mx = -INF;
	foreach(v, i) {
		minimum(mn, v[i]);
		maximum(mx, v[i]);
	}
	int ans = mx - mn;
	cout << toStr(Result =) <<' '<< ans;

	return 0;
}

