import numpy as np
import linear
import relu
import batchnorm

np.random.seed(42)

fc = linear.Linear(in_features=4, out_features=3)
bn = batchnorm.BatchNorm1d(num_features=3)
relu = relu.ReLU()

x = np.random.randn(5, 4)
print("Input:\n", x)

out_fc = fc.forward(x)
out_bn = bn.forward(out_fc, training=True)
out_relu = relu.forward(out_bn)

print("\nForward Output:\n", out_relu)

dout = np.random.randn(*out_relu.shape)

drelu = relu.backward(dout)
dbn = bn.backward(drelu)
dfc = fc.backward(dbn)

print("\nBackward grad wrt input:\n", dfc)

fc.step(lr=0.01)
bn.step(lr=0.01)

print("\nUpdated weights and gamma/beta:")
print("W:\n", fc.W)
print("gamma:\n", bn.gamma)
print("beta:\n", bn.beta)
