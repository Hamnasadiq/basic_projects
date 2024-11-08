#  user_input=int(input())
#  for x in range (1,11):
#      print(f"{user_input} x {x} = {user_input*x}")
# for x in range (1,101):
#     if x%3==0 and x%5==0: 
#         print("FizzBuzz")
#     elif x%5==0:
#         print("Buzz")
#     elif x%3==0:
#         print("FizzBuzz")  
#     else:
#         print(x)  
# user_input=str(input(
# reversed_string=user_input[::-1]
# print(reversed_string)
# def reversed_str(r):
#     return r[::-1]
# user_input=str(input())
# reversed_str=reversed_str(user_input)
# print(reversed_str)
#def vowel(v):
   # return v.count("a") +v.count("e") +v.count("i") +v.count("o") +v.count("u")


# user_input=str(input()).lower()
# vowel_count=vowel(user_input)
# print(vowel_count)
  
# name=str(input("name:"))
# second_name=str(input("second_name:"))
# edu=str(input("edu:"))
# roll_no=int(input("roll_no: "))
# tu=(1,name ,2, edu,3, roll_no)
# li=list(tu)
# li[1]=second_name
# tup=tuple(li)
# print(tup)
user_input=int(input("enter no"))
li=[32,12,44,6,56,32,78]
max_num = []
for _ in range(user_input):
    max_val = max(li)       
    max_num.append(max_val)  
    li.remove(max_val)       
print(f"{user_input} maximum values are", max_num)