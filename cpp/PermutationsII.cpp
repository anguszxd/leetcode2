#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<vector<int> > permute(vector<int>& nums);
void dfs(vector<vector<int> > &ret, vector<int> &num,int cur);
vector<vector<int> > permuteUnique(vector<int>& nums);

int main()
{
	int n[] = {1,2,1};
	vector<int> v(n,n+3);
	vector<vector<int> > ans = permuteUnique(v);

	for(int i=0; i<ans.size(); i++)
	{
		for(int j=0; j<ans.at(0).size(); j++)
			cout << ans.at(i).at(j);
		cout << endl;
	}
	cout << ans.size() << endl;

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
		vector<int> used;
		vector<int>::iterator it;
		for(int i = cur; i<num.size(); i++)
		{
			it = find(used.begin(),used.end(),num.at(i));
			bool exist= it!=used.end() ? false:true;
			if(exist)
			{
				used.push_back(num.at(i));
				swap(num[cur], num[i]);
				dfs(ret, num, cur+1);
				swap(num[cur],num[i]);
			}

		}
	}
}

vector<vector<int> > permuteUnique(vector<int>& nums) {
	vector<vector<int> > ret;
        // case with nums.size() <= 1 is also handled properly
	//这个过程类似于找字典序
	//全体元素排序（从小到大）
    sort(nums.begin(), nums.end());
    ret.push_back(nums); // first permutation
    int i, j;
    while(1){
            // 找到最后一个升序
        for (i=nums.size()-1; i>0; i--){
       	    if (nums[i-1] < nums[i]){
                break;
            }
        }
       	if (i==0){ // next permutation would be the first one again. it means we have got all permutations, ready to return
            break;
        }
            // find nums[j] > nums[i-1], j >= i
        for (j=nums.size()-1; j>=i; j--){
            if (nums[j] > nums[i-1]){
                break;
            }
        }
            // swap
        swap(nums[j], nums[i-1]);
            // sort
        sort(nums.begin()+i, nums.end());
            // now nums is a new permutation
        ret.push_back(nums);
    }
    return ret;
}

