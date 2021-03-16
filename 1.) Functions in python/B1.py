#what will be the output of the following code:
def interest(p,t=2,r=0.10):
    return(p*r*t)


print(interest(6100,1))
print(interest(5000,r=0.05))
print(interest(5000,3,0.12))
print(interest(t=4,p=5000))

# OUPTUT:

# 610.0
# 500.0
# 1800.0
# 2000.0
