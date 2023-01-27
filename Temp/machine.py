
import math,os, numpy as np, pandas

# import tensorflow as tf

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# def sigmoid(x):
#   return 1 / (1 + math.exp(-x))

# def relu(x):
#     return np.maximum(0,x)
# z1=sigmoid(0.7)
# z2=sigmoid(0.6)

# z3=sigmoid(1+z1-z2)
# z4=sigmoid(0.7+0.5*z1+z2)

# z5=sigmoid(0.5-0.8*z3+0.9*z4)
# z6=sigmoid(-0.1+0.3*z3+0.4*z4)

# z7=sigmoid(1+0.1*z5-0.2*z6)
# z8=sigmoid(-0.2+1.3*z5-0.4*z6)

# # z1=relu(0.7)
# # z2=relu(0.6)

# # z3=relu(1+z1-z2)
# # z4=relu(0.7+0.5*z1+z2)

# # z5=relu(0.5-0.8*z3+0.9*z4)
# # z6=relu(-0.1+0.3*z3+0.4*z4)

# # z7=relu(1+0.1*z5-0.2*z6)
# # z8=relu(-0.2+1.3*z5-0.4*z6)

# print(z1,z2)
# print(z3,z4)
# print(z5,z6)
# print(z7,z8)

def avg(a,b,c,d):
    print((a+b+c+d)/4)
'''
avg(-5.5, -3.5, 0.5, 0.5)
avg(-5.5, -12.5, 0.5, 0.5)
avg(-19.5, -12.5, 0.5, 0.5)
avg(-19.5, -26.5, 0.5, 0.5)
avg(-26.5, -26.5, 0.5, 0.5)
avg(-26.5, -26.5, 0.5, 0.5)
avg(-17.5, -26.5, 0.5, 0.5)
'''

def softmax(a):
    c = np.max(a) # 최댓값을 빼주자
    exp_a = np.exp(a-c) 
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
'''
print(softmax([0.4,2.0,0.001,0.32]))


y_pred = np.array([0.001, 0.9, 0.001, 0.098])
y_real = np.array([0, 0, 0, 1])

print(-np.log2(0.098))


import numpy as np
from sklearn import metrics

y_pred = np.array([0.001, 0.9, 0.001, 0.098])
y_real = np.array([0, 0, 0, 1])

# 평균제곱오차
print(metrics.mean_squared_error(y_pred, y_real))
print(((0.001-0)**2 + (0.9-0)**2 + (0.001-0)**2 + (0.098-1)**2)/4)


y_pred = np.array([0.001, 0.9, 0.001, 0.098])
y_real = np.array([0, 0, 0, 1])

# 교차 엔트로피
def cross_entropy_error(y,t):
        # 로그 함수는 x = 0 에서 무한대로 발산하는 함수이기 때문에 x = 0 이 들어가서는 안된다.
        # 따라서, 매우 작은 값을 넣어 - 무한대가 나오는 것을 방지한다.
    delta = 1e-7
    return -np.sum(np.log(y+delta) * t)

print(cross_entropy_error(y_pred, y_real))
print(-(np.log(0.001+1e-7)*0 + np.log(0.9+1e-7)*0 + np.log(0.001+1e-7)*0 + np.log(0.098+1e-7)*1))
'''

A = [[8,2],[2,11]]

det = A[0][0]*A[1][1]-A[0][1]*A[1][0]

iA =  [[0,0],[0,0]]
iA[0][0] =  A[1][1] / det
iA[0][1] = -A[0][1] / det
iA[1][0] = -A[1][0] / det
iA[1][1] =  A[0][0] / det

print(iA)

def cal(a,b):
    result = 2.4*a -27.6*b
    return result

data = pandas.DataFrame({'a':[121,140,120,131,101],
                        'b':[1.72,1.62,1.7,1.8,1.78],
                        'c':[69,63.2,59,82,73.5]})
from sklearn.preprocessing import StandardScaler

print(data.mean(axis='rows'))
print(data.std(axis='rows')) 
'''
a    122.600  14.570518 => -0.11  1.194 -0.178 0.577 -1.482
b      1.724  0.071274
c     69.340  8.976525
'''
scaler = StandardScaler()
df_std = scaler.fit_transform(data)

data2 = pandas.DataFrame(df_std, columns = ['x1_std', 'x2_std','x3_std'])
print(data2)


print(np.std([121,140,120,131,101]))

mean = sum([121,140,120,131,101])/5
vsum = 0
for val in [121,140,120,131,101]:
    vsum = vsum + (val - mean)**2
variance = vsum / 5
print(math.sqrt(variance))

print(2.04 - 0.2* 0.16)
print(1.36 - 0.2* 0.72)
print(1 - 0.2* 0)