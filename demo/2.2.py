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


import torch
import math

dtype = torch.float
device = torch.device("cpu")
# device = torch.device("cuda:0")  # Uncomment this to run on GPU

# Create Tensors to hold input and outputs.
# By default, requires_grad=False, which indicates that we do not need to
# compute gradients with respect to these Tensors during the backward pass.
x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
y = torch.sin(x)

# Create random Tensors for weights. For a third order polynomial, we need
# 4 weights: y = a + b x + c x^2 + d x^3
# Setting requires_grad=True indicates that we want to compute gradients with
# respect to these Tensors during the backward pass.
a = torch.randn((), device=device, dtype=dtype, requires_grad=True)
b = torch.randn((), device=device, dtype=dtype, requires_grad=True)
c = torch.randn((), device=device, dtype=dtype, requires_grad=True)
d = torch.randn((), device=device, dtype=dtype, requires_grad=True)

learning_rate = 1e-6
for t in range(2000):
    # Forward pass: compute predicted y using operations on Tensors.
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss using operations on Tensors.
    # Now loss is a Tensor of shape (1,)
    # loss.item() gets the scalar value held in the loss.
    loss = (y_pred - y).pow(2).sum()
    if t % 100 == 99:
        print(t, loss.item())

    # Use autograd to compute the backward pass. This call will compute the
    # gradient of loss with respect to all Tensors with requires_grad=True.
    # After this call a.grad, b.grad. c.grad and d.grad will be Tensors holding
    # the gradient of the loss with respect to a, b, c, d respectively.
    loss.backward()

    # Manually update weights using gradient descent. Wrap in torch.no_grad()
    # because weights have requires_grad=True, but we don't need to track this
    # in autograd.
    with torch.no_grad():
        a -= learning_rate * a.grad
        b -= learning_rate * b.grad
        c -= learning_rate * c.grad
        d -= learning_rate * d.grad

        # Manually zero the gradients after updating weights
        a.grad = None
        b.grad = None
        c.grad = None
        d.grad = None

print(f'Result: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')
