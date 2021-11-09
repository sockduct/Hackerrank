#line 1 "preproc-test1.cpp"










using namespace std;



#line 16 "preproc-test1.cpp"

void minimum(int& x, int y) { if (!(x < y)) x = y; }
void maximum(int& x, int y) { if (!(x > y)) x = y; }

int main(){
	int n; cin >> n;
	vector<int> v(n);
	for (auto i; i < v.size(); ++i) {
		cin >> v[i];
	}
	int mn = 1000000000;
	int mx = -1000000000;
	for (auto i; i < v.size(); ++i) {
		minimum(mn, v[i]);
		maximum(mx, v[i]);
	}
	int ans = mx - mn;
	cout << "Result =" <<' '<< ans;

	return 0;
}

