def s_ou_n(varetas):
   for k in range(1, len(varetas)-1):
        if varetas[k] + varetas[k-1] > varetas[k+1]:
           return "S"
   return "N"       
            
varetas = sorted(map(int, input().split()))
print(s_ou_n(varetas))