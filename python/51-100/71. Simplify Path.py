class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        path = filter(lambda x : x != "", path)
        res = []
        for val in path:
            if val != "." and val != "..":
                res.append(val)
            else:
                if val == ".":
                    continue
                if val == "..":
                    if res:
                        res.pop()
        return "/" + "/".join(res)