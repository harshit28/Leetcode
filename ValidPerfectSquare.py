  l,r=1,num
        while(l<=r):
            mid=r+(l-r)//2
            if mid*mid == num:
                return True
            elif mid * mid > num:
                r=mid-1
            else:
                l=mid+1
        return False        
