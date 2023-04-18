image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
# the output should be

# (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5




















# solution(image) = [[5, 4], 
#                   [4, 4]]
# c = []
# for x in range(0,len(image)-2):
#     b = []    
#     for y in range(0,len(image)-2):

#         a = []
#         for i in range(0+y,3+y):
#             for j in range(0+x,3+x):
#                 a.append(image[i][j])
#         b.append(sum(a)//9)
#     c.append(b)
# print(c)