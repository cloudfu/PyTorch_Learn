import torch
import matplotlib.pyplot as plt

lr = 0.001
see = 20000

# torch.rand(size) size可以为int，也可以为一个数组指定输出维度
# torch.rand(4)
# 0.9193
# 0.3347
# 0.3232
# 0.7715
# torch.rand([1, 50])
# [[0,1,2,3,4,5....50]]
x = torch.rand([1, 50])
y = 3 * x + 0.8

w = torch.rand([1, 1], requires_grad=True, dtype=torch.float32)
b = torch.rand(1, requires_grad=True, dtype=torch.float32)
loss = []

plt.ion()

for i in range(see):
    # 进行函数预测 y = 3 * x + 0.8
    y_pred = torch.matmul(w, x) + b

    cur_loss = torch.matmul(y - y_pred, (y - y_pred).T)
    loss.append(cur_loss.item())
    if i != 0:  # 将梯度清零，初始时参数的梯度为None所以先计算一次后才有梯度
       w.grad.data.zero_()
       b.grad.data.zero_()

    cur_loss.backward()
    w.data = w.data - lr * w.grad
    b.data = b.data - lr * b.grad

    if i % 200 == 0:
        print("w, b, loss", w.item(), b.item(), cur_loss.item())
        plt.cla()
        plt.scatter(x.numpy()[0], y.numpy()[0])
        y_predict = torch.matmul(w, x) + b
        plt.plot(x.numpy()[0], y_predict.detach().numpy()[0])
        plt.pause(1)

plt.ioff()
plt.show()