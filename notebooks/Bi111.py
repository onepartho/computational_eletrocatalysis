from ase import Atom, Atoms
from ase.visualize import view



# Define geometry of slab + BF4:
slab = Atoms([Atom('Bi', (0.0000, 0.0000, -1.590)),
              Atom('Bi', (2.2700, 1.3105,  0.000)),
              Atom('Bi', (2.2700, 3.9315, -1.590)),
              Atom('Bi', (0.0000, 5.2420,  0.000))],
              cell=((4.54,0,0), (0,7.8635,0), (0,0,1)),pbc=True)
slab.center(axis=2, vacuum=10)

view(slab)

