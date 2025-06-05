#Matrix Addition and Multiplication

# a=[[1,1,1],[1,2,2],[3,3,3]]
# b=[[1,1,1],[1,2,2],[3,3,3]]
# def mat_add(a,b):
#     temp=a
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             temp[i][j] = a[i][j]+b[i][j]
#     return temp
# print(mat_add(a,b))


###########################################

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

def mat_mul(A,B,test=[]):
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(0)
        test.append(row)

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                test[i][j] += A[i][k] * B[k][j]
    return test
print(mat_mul(A,B))




############################################
