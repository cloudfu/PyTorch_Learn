import os
import pandas as pd

# os.makedirs(os.path.join('..', 'data'), exist_ok=True)
# data_file = os.path.join('..', 'data', 'house_tiny.csv')
# with open(data_file, 'w') as f:
#     f.write('NumRooms,Alley,Price\n')  # 列名
#     f.write('NA,Pave,127500\n')  # 每行表示一个数据样本
#     f.write('2,NA,106000\n')
#     f.write('4,NA,178100\n')
#     f.write('NA,NA,140000\n')
# data = pd.read_csv(data_file)
# print(data)

# 2.3
# import torch
#
# a = torch.arange(5,dtype=torch.float32)
# b = torch.ones(6,dtype=torch.float32)
# print(torch.dot(a,b))

# print(a)
# a_sum = a.sum(axis=1,keepdims=True)
# print(a_sum)
# print(a.mean())
# print(a.sum()/a.numel())
# # print(a_sum.shape)
#
# a = torch.randn(1, 3)
# torch.mean(a)

# 2.3.7  点积
# 点积只能针对一维数据模型
# import torch
# a = torch.arange(6,dtype=torch.float32)
# b = torch.ones(6,dtype=torch.float32)
# print(a)
# print(b)
# print(torch.dot(a,b))

# 2.3.8 矩阵-向量积
# 使用向量b和张量a，第二维度相乘并累加，保留张量a 第一维度
# import torch
# a = torch.arange(8,dtype=torch.float32).reshape(2,2,4)
# print(a)
# b = torch.arange(4,dtype=torch.float32)
# print(b)
# print(torch.mv(a, b))

# 范式
# import torch
# u = torch.tensor([6.0,8.0])
# print(torch.norm(u))

# import numpy as np
# from IPython import display
# from d2l import torch as d2l

#
# def f(x):
#     return 3 * x ** 2 - 4 * x


from tensorboard import version
print(version.VERSION)