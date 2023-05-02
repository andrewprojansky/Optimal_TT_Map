#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Examples.py
---------------------------------------------------------------------
Test functions and examples of use of Op_TT_Ent.py

by Andrew Projansky
Last Edited 5/2/23

"""
from Op_TT_Ent import *
from qiskit.quantum_info import Clifford
import itertools 
from tqdm import tqdm
#%%
'''
Make a random tree of size n. If the clifford entangles the vacuum state, 
prints so. If not, generates list of local transformations that take the 
product state of the encoding back to the vacuum state for JW
'''
n = 3
Msi = Gen_Tree(n)
Ms = [t for t in Msi]
del Ms[np.random.randint(0,2*n+1)]
s_dict, Ms = Stab_Destab(n, Ms)
U = Clifford(Clifford.from_dict(s_dict).to_circuit().reverse_bits()).to_matrix()
vac = np.zeros(2**n); vac[0] = 1
psi = U @ vac
mps = make_mps_like(psi, n)
flat_list = []
for sublist in mps:
    for val in sublist:
        flat_list.append(val)
if len(flat_list) > 2*n:
    print('Entangled')
else:
    ulist = np.zeros((n, 2, 2), dtype='complex')
    for i in range(len(mps)):
        p = mps[i]
        p = p / LA.norm(p)
        rho_s = np.outer(p, np.conj(p))
        d, u = LA.eig(rho_s)
        ulist[i,:,:] = u
print(ulist)
#%%
'''
An ordered clique such that deleting any element (while keeping ordering) 
produces a set of majoranas that has non entangled vacuum state
'''
Ms = ['XIX', 'XIY', 'XIZ', 'YII', 'ZXI', 'ZYI', 'ZZI']
v = 0
del Ms[v]
s_dict, Ms = Stab_Destab(n, Ms)
U = Clifford(Clifford.from_dict(s_dict).to_circuit().reverse_bits()).to_matrix()
vac = np.zeros(2**n); vac[0] = 1
psi = U @ vac
mps = make_mps_like(psi, n)
ulist = np.zeros((n, 2, 2), dtype='complex')
for i in range(len(mps)):
    p = mps[i]
    p = p / LA.norm(p)
    rho_s = np.outer(p, np.conj(p))
    d, u = LA.eig(rho_s)
    ulist[i,:,:] = u
#print(ulist)
#%%
'''
Checks all orderings of a set of 6 majoranas to see if and how many 
orderings produce non entangled vacuum states
'''
n = 3
pcount = 0
perms = list(itertools.permutations( ['XXI', 'XYI', 'XZI', 'YIY', 'YIZ', 'ZII']))
for plist in perms:
    s_dict, Ms = Stab_Destab(3, plist)
    U = Clifford(Clifford.from_dict(s_dict).to_circuit().reverse_bits()).to_matrix()
    vac = np.zeros(2**n); vac[0] = 1
    psi = U @ vac
    mps = make_mps_like(psi, n)
    flat_list = []
    for sublist in mps:
        for val in sublist:
            flat_list.append(val)
    if len(flat_list) == 2*n:
        pcount += 1
        print(plist)