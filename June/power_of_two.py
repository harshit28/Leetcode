       if n==1:
            return True
        if n == 0:
            return False
        while(n!=1):
            if n%2:
                return False
            n/=2
        return True  
