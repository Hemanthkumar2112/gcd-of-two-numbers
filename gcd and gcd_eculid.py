a = 98
b = 56
def gcd(x,y):
    if x==0:
        return y
    if y==0:
        return x
    if x>y:
        return gcd(x-y,y)
    return gcd(x,y-x)
  
  
  def gcd_eculid(x,y):
    if x==0:
        return y
    elif y==0:
        return x
    else:
        return gcd(y,x%y)
  gcd_eculid(a,b) ##14 more efficient
  gcd(a,b)    ####14
  
