import random
random_no=random.sample(range(1,101) ,10)
string=" ".join(map(str,random_no))
print(string)