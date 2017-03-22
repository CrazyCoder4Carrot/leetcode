class Solution {
public:
	vector<string> fullJustify(vector<string>& words, int maxWidth) {
		int i = 0;
		vector<string> res;
		while (i < words.size()) {
			vector<string> row;
			string rowstr = "";
			int length = -1;
			for (; i < words.size() && length <= maxWidth; i++)
			{
				row.push_back(words[i]);
				length += words[i].size() + 1;
			}
			while (length > maxWidth)
			{
				row.pop_back();
				length = length - words[i - 1].size() - 1;
				i--;
			}
			if (row.size() == 1)
			{
				string slotstr(maxWidth - row[0].size(), ' ');
				rowstr = row[0] + slotstr;
			}
			else
			{
				vector<int> slots(row.size(), blankcnt / (row.size() - 1));
				int blankcnt = maxWidth - length + (row.size() - 1);
				if (i == words.size()) {
					for(int k = 0; k < slots.size() - 1; k++)
						slots[k] = 1;
					slots[slots.size() - 1] += blankcnt  - (row.size() - 1);
				}
				else {
					slots[slots.size() - 1] = 0;
					int rem = blankcnt % (row.size() - 1);
					for (int k = 0; k < slots.size() && rem > 0; k++, rem--)
					{
						slots[k]++;
					}
				}
				for (int k = 0; k < row.size(); k++) {
					string slotstr(slots[k], ' ');
					rowstr = rowstr + row[k] + slotstr;
				}

			}
			res.push_back(rowstr);
		}
		return res;
	}
};