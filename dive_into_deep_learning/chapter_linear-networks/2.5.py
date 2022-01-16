import torch

x = torch.arange(4.0, requires_grad=True)
print(x)
y = 2 * torch.dot(x, x)
print(y)
y.backward()
print(x.grad)
