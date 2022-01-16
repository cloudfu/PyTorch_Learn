import random
import torch
import matplotlib.pyplot as plt
import numpy as np


# # matmul sample
# a = torch.arange(0,6).reshape(2, 3)
# print(a)
# b = torch.arange(0,6).reshape(3, 2)
# print(b)
# print(torch.matmul(a, b))


# def element_by_element():
#     x = torch.tensor([1, 2, 3])
#     y = torch.tensor([4, 5, 6])
#
#     return x * y, torch.mul(x, y)
#
# print(element_by_element())


def vec_matrix():
    x = torch.tensor([1, 2, 3])
    y = torch.tensor([
        [7, 8],
        [9, 10],
        [11, 12]
    ])
    print(x)
    print(y)
    return torch.matmul(x, y)
print(vec_matrix())


def matrix_vec():
    x = torch.tensor([
        [1, 2, 3],
        [4, 5, 6]
    ])
    print(x)
    y = torch.tensor(
        [7, 8, 9]
    )
    print(y)
    return torch.matmul(x, y)

print(matrix_vec())


# def matrix_multiple():
#     x = torch.tensor([
#         [1, 2, 3],
#         [4, 5, 6]
#     ])
#     y = torch.tensor([
#         [7, 8],
#         [9, 10],
#         [11, 12]
#     ])
#
#     return torch.matmul(x, y)
# print(matrix_multiple())

#
# a = np.array([[1,2],[3,4]])
# print(a)
# b = np.array([[11,12],[13,14]])
# print(b)
# # [[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
# print(np.dot(a,b))

# 3.2.1. 生成数据集
def synthetic_data(w, b, num_examples):  # @save
    """生成y=Xw+b+噪声"""
    # normal 必须入参 size，标志生成向量的维度
    # torch.normal(0, 1, (num_examples, len(w)))(num_examples, len(w))为正态分布的数据维度，这里维度是(1000, 2)

    # len只给出向量得 第一维度长度
    # width = len(torch.tensor([[1, 2], [2, 3], [2, 3]]))
    # 输出 X = 1000,2 size

    #   torch.normal(0, 1, (1000,2))
    X = torch.normal(0, 1, (num_examples, len(w)))

    # y和一维数据相乘降维[1000]
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))


true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = synthetic_data(true_w, true_b, 1000)

plt.scatter(features[:, (1)].detach().numpy(), labels.detach().numpy(), 1)
plt.show()


# 3.2.2. 读取数据集
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    # 这些样本是随机读取的，没有特定的顺序
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(indices[i: min(i + batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]


batch_size = 10

for X, y in data_iter(batch_size, features, labels):
    print("X:", X, '\n', "Y:", y)
    break

# 3.2.3. 初始化模型参数
w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)


def linreg(X, w, b):  # @save
    """线性回归模型"""
    return torch.matmul(X, w) + b


def squared_loss(y_hat, y):  # @save
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2


def sgd(params, lr, batch_size):  # @save
    """小批量随机梯度下降"""
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()


lr = 0.03
num_epochs = 3
net = linreg
loss = squared_loss

for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y)  # X和y的小批量损失
        # 因为l形状是(batch_size,1)，而不是一个标量。l中的所有元素被加到一起，
        # 并以此计算关于[w,b]的梯度
        l.sum().backward()
        sgd([w, b], lr, batch_size)  # 使用参数的梯度更新参数
    with torch.no_grad():
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')

print(f'w的估计误差: {true_w - w.reshape(true_w.shape)}')
print(f'b的估计误差: {true_b - b}')
