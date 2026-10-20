import pytest

from scalargrad.nn import Neuron


def test_neuron_rejects_wrong_number_of_inputs():
    neuron = Neuron(2)

    with pytest.raises(ValueError, match="expected 2 inputs, received 1"):
        neuron([1.0])
