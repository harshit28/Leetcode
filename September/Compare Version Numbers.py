class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arrv1,arrv2= version1.split('.'),version2.split('.')
        i=0
        if len(arrv1) < len(arrv2):
            toadd = len(arrv2) - len(arrv1)
            arrv1 = arrv1 + [0] * toadd
        elif len(arrv1) > len(arrv2):
            toadd = len(arrv1) - len(arrv2)
            arrv2 = arrv2 + [0] * toadd
            
        while i < len(arrv1):
            if int(arrv1[i]) > int(arrv2[i]):
                return 1
            elif int(arrv1[i]) < int(arrv2[i]):
                return -1
            i+=1
        return 0
