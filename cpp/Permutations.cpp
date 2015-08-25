#include <vector>
#include <iostream>

using namespace std;

vector<vector<int> > permute(vector<int>& nums);
void dfs(vector<vector<int> > &ret, vector<int> &num,int cur);

int main()
{
	int n[] = {1,2,3};
	vector<int> v(n,n+3);
	vector<vector<int> > ans = permute(v);

	for(int i=0; i<ans.size(); i++)
	{
		for(int j=0; j<ans.at(0).size(); j++)
			cout << ans.at(i).at(j);
		cout << endl;
	}


	return 0;
}

vector<vector<int> > permute(vector<int> &nums)
{
	vector<vector<int> > ret;
	dfs(ret, nums, 0);
	return ret;
}

//dfs:Depth-First-Search深度优先遍历
void dfs(vector<vector<int> > &ret, vector<int> &num,int cur)
{
	if(num.size() == cur)
	{
		ret.push_back(num);
	}
	else
	{
		for(int i = cur; i<num.size(); i++)
		{
			swap(num[cur], num[i]);
			dfs(ret, num, cur+1);
			swap(num[cur],num[i]);
		}
	}
}

