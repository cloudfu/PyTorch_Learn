import numpy as np
import matplotlib.pyplot as plt
from torch.utils.tensorboard import SummaryWriter


def f(x):
    return 3 * x ** 2 - 4 * x


def numerical_lim(f, x, h):
    result_1 = f(x + h)
    result_2 = f(x)
    return (f(x + h) - f(x)) / h


h = 0.1

for i in range(5):
    print(f'h={h:.5f}, numerical limit={numerical_lim(f, 1, h):.5f}')
    h *= 0.1

#
# writer = SummaryWriter(comment='_scalars', filename_suffix="12345678")
#
# for x in range(-10, 100, 1):
#     writer.add_scalar('X',  f(x), x)
#
# writer.close()
