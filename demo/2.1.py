import torch


# x = torch.arange(12, dtype=torch.float32).reshape(3, 4)
# y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
# x1 = torch.cat((x,y),dim=0)
# y1 = torch.cat((x,y),dim=1)
# print(torch.cat((x,y),dim=0),torch.cat((x,y),dim=1))
#
# reult = x == y
# print(reult)

# a = torch.arange(3).reshape(1,3)
# b = torch.arange(3).reshape(3,1)
# print(a + b)
import torch
X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
Z = torch.zeros_like(Y)
print('id(Z):', id(Z))
Z[:] = X + Y
print(Z)
print('id(Z):', id(Z))


# a1 = torch.tensor([[1,2,3]])
# b1 = torch.tensor([[4],[5],[6]])
# print (a1 + b1)
