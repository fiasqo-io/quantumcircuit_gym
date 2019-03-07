# Gym Environment for Quantum Circuit Synthesis (using qiskit and qutip)

A custom gym environment for creating quantum circuits using IBMQ's qiskit library for python. Options include:

1. Defining size of the circuit in terms of number of qubits
2. Choosing whether to use unitary matrices or statevectors
3. Choosing a set of gates to use, predefined or custom
4. Choosing the physical connectivity of the qubits, predefined or custom
5. Choosing initial goal states or unitaries

A step in the environment is defined as applying one single gate from the defined gate group to a specific qubit, with all possible combinations of gate/qubit pairs (or triplets in case of a two qubit gate) being generated based on the defined connectivity.

The reward is sparse, and inversely proportional to the amount of gates needed to get to the goal - incentivising smaller circuits. Alternatives are currently being investigated.

## Installation

First clone/download the repo. Then (preferably in a fresh virtual environment):

```
cd quantumcircuit-gym
conda install -c conda-forge qutip
while read requirement; do conda install --yes $requirement; done < conda_reqs.txt
pip install -r requirements.txt
pip install -e .
```
In progress: better installation automation

## Example use
Most methods displayed in [tutorial notebook](gym-quantcircuit-tutorial.ipynb).
