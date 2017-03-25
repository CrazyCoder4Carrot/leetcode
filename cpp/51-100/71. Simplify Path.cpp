class Solution {
public:
	string simplifyPath(string path)
	{
		vector<string> directory;
		string res = "", temp;
		stringstream ss(path);
		while(getline(ss, temp, '/')){
			if(temp == "." || temp == "")
				continue;
			if(temp == ".." && !directory.empty())
				directory.pop_back();
			if(temp != "..")
				directory.push_back(temp);
		}
		for(int i = 0 ; i < directory.size(); i++)
			res += "/" + directory[i];
		return res.empty()? "/":res;
	}
};