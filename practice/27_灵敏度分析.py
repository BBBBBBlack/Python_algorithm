from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import numpy as np

# Define the model inputs
problem = {
    'num_vars': 3,
    'names': ['x1', 'x2', 'x3'],
    'bounds': [[-3.14159265359, 3.14159265359],
               [-3.14159265359, 3.14159265359],
               [-3.14159265359, 3.14159265359]]
}

# Generate samples
# 采样，生成N*(2D+2)个样本（D为problem中参数个数），每个参数的值在[-3.14159265359, 3.14159265359]之间
param_values = saltelli.sample(problem, N=1024)

# Run model (example)
# 计算每个样本的输出值
Y = Ishigami.evaluate(param_values)

# Perform analysis
# 计算灵敏度指数
Si = sobol.analyze(problem, Y, print_to_console=True)
