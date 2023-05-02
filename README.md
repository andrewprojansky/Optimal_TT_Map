# Optimal_TT_Map

Code for generating optimal ternary tree fermion-to-qubit encodings. Once an encoding is generated, it generates the map from the encoding to an
encoding equivalent to the Jordan Wigner encoding (JW) by mapping them to a set of stabiliers and destabilizers, and finding the clifford that 
transforms them back into the stabilizer for the all zero state.
Once it has this clifford, it checks if it maps the all zero state to an entangled state. If not, it generates the local unitaries to take the 
vacuum state of the encoding to the all zero state. 
