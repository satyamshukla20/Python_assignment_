#task1-Slicing
#Get element from second position to fifth position from list - [1, 2, 3, 4, 5, 6]

# def solve1(arr1):
#     return arr1[2:6]

# arr1=[i for i in input().split()]
# print(solve1(arr1))

#-------------------------------------------------------------------------------------------

#task2-Condition
#Check if string palindrome or not “ab”, “abc”, “aba”

# def solve2(arr2):
#     ans=[]
#     for i in arr2:
#         if(i==i[::-1]):
#             ans.append(True)
#         else:
#             ans.append(False)
#     return(ans)

# brr2=[i for i in input().split()]
# ans=solve2(brr2)
# for i in range(len(ans)):
#     if i<len(ans)-1:
#         print(ans[i],end=',')
#     else:
#         print(ans[i])

# #-----------------------------------------------------------------------------------------------

# #task3-Loop
# #Check if string contains repeated characters “aab”, “abc”, “def”

 
# def solve3(arr3):
#     ans=[]
#     for i in arr3:
#         elements={}
#         for char in i:
#             if elements.get(char,None) != None :
#                 elements[char] +=1
#             else: 
#                 elements[char] =1
        
#         for k,v in elements.items():
#             flag=False
#             if v>1:
#                 ans.append(True)
#                 flag=True
#                 break
#         if flag==False:
#             ans.append(False)
#     return ans

# arr3 = [i for i in input().split()]
# print(solve3(arr3))

# #--------------------------------------------------------------------------------------------------

# #task4-Function
# #Convert all the above to function which can work on variadic number of arguments


#1.)
# def solve4(*args):
#     return args[2:6]

# print(solve4(2,5,7,7,8,9))

#/////////////////////////////////////////////////////////////////////

#2.)

# def solve5(*args):
#     ans=[]
#     for i in args:
#         if(i==i[::-1]):
#             ans.append(True)
#         else:
#             ans.append(False)
#     return(ans)


# ans=solve5("abc","acf","asa")
# for i in range(len(ans)):
#     if i<len(ans)-1:
#         print(ans[i],end=',')
#     else:
#         print(ans[i])

#////////////////////////////////////////////////////////////////////////

#3.)

# def solve6(*args):
#     ans=[]
#     for i in args:
#         elements={}
#         for char in i:
#             if elements.get(char,None) != None :
#                 elements[char] +=1
#             else: 
#                 elements[char] =1
        
#         for k,v in elements.items():
#             flag=False
#             if v>1:
#                 ans.append(False)
#                 flag=True
#                 break
#         if flag==False:
#             ans.append(True)
#     return ans

# print(solve6("as11","awa","asdfg"))










