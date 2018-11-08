from amuse.units import units
from amuse.datamodel import Particles

x = Particles(1)
x.mass = 3. | units.MSun
x.radius = 20. | units.RSun
