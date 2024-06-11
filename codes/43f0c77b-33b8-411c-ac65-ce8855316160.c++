#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>
#include <cstring>

int n, m;

int a[700];

int main()
{
	scanf("%d", &n);

	int b;
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &b);
		a[b]++;
	}

	int ans = 0;
	for (int i = 1; i < 660; ++i)
		if (a[i] > 0) ++ans;

	printf("%d\n", ans);

	return 0;
}