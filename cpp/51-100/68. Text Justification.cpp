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
				vector<int> slots(row.size(), 0);
				int blankcnt = maxWidth - length + (row.size() - 1);
				if (i == words.size()) {
					for (int k = 0; k < slots.size() && blankcnt > 0; k++, blankcnt--){
						slots[k]++;
					}
					slots[slots.size() - 1] += blankcnt;
				}
				else {
					while (blankcnt) {
						for (int k = 0; k < slots.size() - 1 && blankcnt > 0; k++, blankcnt--)
						{
							slots[k]++;
						}
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