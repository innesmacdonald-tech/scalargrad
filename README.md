# scalargrad

I use ScalarGrad to explore how automatic differentiation works under the hood.
It is a small scalar-valued autograd engine with a minimal neural-network library,
inspired by Andrej Karpathy's [micrograd](https://github.com/karpathy/micrograd).

## Installation

```bash
pip install -e .
```

To run the notebook demo, install its additional dependencies:

```bash
pip install numpy matplotlib scikit-learn jupyter
```

## Quick start

```python
from scalargrad.engine import Value

a = Value(3.0)
b = Value(2.0)
c = (a * b + b**3).relu()
c.backward()
print(a.grad, b.grad)  # 2.0 15.0
```

```python
from scalargrad.nn import MLP

model = MLP(2, [16, 16, 1])
```

The [demo notebook](demo.ipynb) walks through training a binary classifier on
the moons dataset with this engine.

## Running the tests

The tests compare gradients against PyTorch. Install the test dependencies and
run the suite with:

```bash
pip install torch pytest
python -m pytest
```
