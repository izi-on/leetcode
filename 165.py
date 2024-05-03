class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        sv1 = version1.split(".")
        sv2 = version2.split(".")
        if len(sv1) < len(sv2):
            sv1.extend(["0"] * (len(sv2) - len(sv1)))
        if len(sv2) < len(sv1):
            sv2.extend(["0"] * (len(sv1) - len(sv2)))
        for i in range(len(sv1)):
            n1 = int(sv1[i])
            n2 = int(sv2[i])
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
        return 0
