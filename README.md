# scalargrad

A small scalar-valued autograd engine with a minimal neural network library on top.


## Install

```bash
pip install -e .
```

## Usage

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

See `demo.ipynb` for training a binary classifier on the moons dataset.

## Tests

Tests compare gradients against PyTorch, so install `torch` and `pytest`, then:

```bash
python -m pytest
```

