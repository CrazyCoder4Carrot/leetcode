class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def ipv4(ip):
            def validate(value):
                decimal = map(str, range(10))
                for char in value:
                    if char not in decimal:
                        return False
                return True
            ip_list = ip.split(".")
            for num in ip_list:
                if not validate(num):
                    return res_none
                if len(num.strip()) == 0:
                    return res_none
                if int(num) > 255:
                    return res_none
                if len(num[1:]) != 0 and int(num) == int(num[1:]):
                    return res_none
            return res_ipv4
        def ipv6(ip):
            def validate(value):
                hex = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D",
                       "E", "F", "a", "b", "c", "d", "e", "f"}
                for char in value:
                    if char not in hex:
                        return False
                return True
            ip_list = ip.split(":")
            if len(ip_list) != 8:
                return res_none
            for value in ip_list:
                if len(value.strip()) == 0:
                    return res_none
                if len(value) > 4:
                    return res_none
                if not validate(value):
                    return res_none
            return res_ipv6
        res_ipv4 = "IPv4"
        res_ipv6 = "IPv6"
        res_none = "Neither"
        if len(IP.split(".")) == 4:
            return ipv4(IP)
        else:
            return ipv6(IP)
