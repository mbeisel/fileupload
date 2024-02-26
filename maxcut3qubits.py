from qiskit.circuit.quantumcircuit import QuantumCircuit
qc = QuantumCircuit.from_qasm_str("OPENQASM 2.0;\ninclude \"qelib1.inc\";\nqreg q[3];\ncreg meas[3];\nh q[0];\nh q[1];\nrzz(1.0) q[0],q[1];\nh q[2];\nrzz(1.0) q[0],q[2];\nrx(2.0) q[0];\nrzz(1.0) q[1],q[2];\nrx(2.0) q[1];\nrx(2.0) q[2];\nbarrier q[0],q[1],q[2];\nmeasure q[0] -> meas[0];\nmeasure q[1] -> meas[1];\nmeasure q[2] -> meas[2];\n")
