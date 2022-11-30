
#import math,os, numpy as np

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

avg(-5.5, -3.5, 0.5, 0.5)
avg(-5.5, -12.5, 0.5, 0.5)
avg(-19.5, -12.5, 0.5, 0.5)
avg(-19.5, -26.5, 0.5, 0.5)
avg(-26.5, -26.5, 0.5, 0.5)
avg(-26.5, -26.5, 0.5, 0.5)
avg(-17.5, -26.5, 0.5, 0.5)