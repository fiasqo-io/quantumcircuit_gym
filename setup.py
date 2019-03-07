from setuptools import setup

setup(name='gym_quantcircuit',
      version='0.0.1',
      install_requires=['gym>=0.10.11',
                        'qutip>=4.3.1',
                        'qiskit>=0.7.2',
                        'numpy>=1.16.1',
                        'qiskit-aer>=0.1.1',
                        'qiskit-terra>=0.7.0',
                        'networkx>=2.2',
                        'matplotlib>=3.0.2',
                        'Cython>=0.29.4']
)