
Gym Environment for Quantum Circuit Synthesis (using qiskit and qutip)
***************************************************************************

A custom gym environment for the generation of optimal quantum circuits which perform a given computational task, 
using IBMQ's Qiskit library for Python. Options include:


#. Defining size of the circuit in terms of number of qubits
#. Choosing whether to use unitary matrices or statevectors
#. Choosing a set of gates to use, predefined or custom
#. Choosing the physical connectivity of the qubits, predefined or custom
#. Choosing initial goal states or unitaries

A step in the environment is defined as applying one single gate from the defined gate group to a specific qubit, 
with all possible combinations of gate/qubit pairs (or triplets in case of a two qubit gate) being generated based on the defined connectivity.

The reward is sparse, and inversely proportional to the amount of gates needed to get to the goal - incentivising smaller circuits. 
Experimentation with custom reward functions is encouraged.

Qiskit Integration
-------------------

Qiskit is central to this environment, providing the QuantumCircuit class that allows the sequential application of gates 
to construct a circuit representation of a unitary process. This facilitates the simulation of a given circuit using the Aer backend 
in order to obtain the resultant quantum state. The library also provides a tool to visualise the current circuit using standard literature conventions.

Installation
------------

First clone/download the repo. Then (preferably in a fresh virtual environment):

.. code-block::

   cd quantumcircuit-gym
   conda install -c conda-forge qutip
   while read requirement; do conda install --yes $requirement; done < conda_reqs.txt
   pip install -r requirements.txt
   pip install -e .

In progress: better installation automation

Example use
-----------

Most methods displayed in `tutorial notebook <https://github.com/MaxKelsen/quantumcircuit_gym/blob/master/gym-quantcircuit-tutorial.ipynb>`_.
