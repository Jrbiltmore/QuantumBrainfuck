
# main.py
# UUID: 900100000018

import argparse
from src.quantum_brainfuck import QuantumBrainfuck

def parse_arguments():
    parser = argparse.ArgumentParser(description='Quantum Brainfuck Interpreter')
    parser.add_argument('code', type=str, help='Brainfuck code to execute')
    parser.add_argument('--qubits', type=int, default=5, help='Number of qubits for the quantum circuit')
    return parser.parse_args()

def main():
    args = parse_arguments()
    qb = QuantumBrainfuck(num_qubits=args.qubits)
    qb.run(args.code)

if __name__ == "__main__":
    main()
