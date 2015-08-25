#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int main(){
	int data[] = {1,2,3,4};
	vector<int> v(data, data+4);
	int seacher[] = {2,2,3,4,5,1};
	vector<int> v_search(seacher, seacher+6);
	
	vector<int>::iterator it;
	for(int i = 0; i<v_search.size(); i++){
		it = find(v.begin(),v.end(),v_search.at(i));
		bool mark = it!=v.end() ? true:false;
		if(mark)
			cout << "element " << v_search.at(i) <<" is in V" << endl;
		else
			cout << "element " << v_search.at(i) <<" is not in V" << endl;
	}


	return 0;
}
