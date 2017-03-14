class Solution {
public:
	void solveSudoku(vector<vector<char>>& board) {
		vector<vector<int>> positions;
		for (int i = 0; i < board.size(); i++)
		{
			for (int j = 0; j < board[0].size(); j++)
			{
				if (board[i][j] == '.')
				{
					std::vector<int> temp;
					temp.push_back(i);
					temp.push_back(j);
					positions.push_back(temp);
				}
			}
		}
		helper(board, positions, 0);
	}
	bool helper(vector<vector<char>>& board, vector<vector<int>> positions, int index)
	{
		if (index == positions.size())
		{
			return validate(board);
		}
		vector<int> temp = positions[index];
		for (int i = 0; i < 9; i++)
		{
			board[temp[0]][temp[1]] = '1' + i;
			if(!validate(board))
			{
			    board[temp[0]][temp[1]] = '.';
			}
			else{
			if(helper(board, positions, index+1))
			    return true;
			board[temp[0]][temp[1]] = '.';
			}
		}
		return false;
	}
    bool validate(vector<vector<char>>& board) {
        bool used1[9][9] = {false};
		bool used2[9][9] = {false};
		bool used3[9][9] = {false};
		for (int i = 0; i < board.size(); i++)
		{
			for (int j = 0; j < board[0].size(); j++)
			{
			    if(board[i][j] != '.')
			    {
				int num = board[i][j] - '1';
				int k = i / 3 * 3 + j / 3;
				if (used1[i][num] | used2[j][num] | used3[k][num])
					return false;
				else
					used1[i][num] = used2[j][num] = used3[k][num] = true;
			    }
			}
		}
		return true;
    }
};