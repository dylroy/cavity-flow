"""

"""

from dataclasses import dataclass
from dataclasses import make_dataclass
from dataclasses import field
from typing import ClassVar

import numpy as np
import xarray as xr

__version__ = '0.1'
__author__ = 'Dylan J Roy-Leo'

ufunc_x = lambda x: x*0
ufunc_y = lambda y: y*0
wfunc_x = lambda x: x*0
wfunc_y = lambda y: y*0
pfunc_x = lambda x: x*0
pfunc_y = lambda y: y*0

coords = {'xdim':np.linspace(0.0,domain_size,Nx),'ydim':np.linspace(0.0,domain_size,Nx),'tdim':np.arange(0.0,Ndt,dt)}
uxarr, wxarr, pxarr = create_arrays(coords, ics, bcs)

@dataclass
class Config():
    """
    The `Config` class is the main interface between
    the user of this simulation and the simulation
    itself.
    """
    default_init: ClassVar[function] = lambda x: x*0
    default_bounds: ClassVar[float] = 0.

    model_type: dict[str, int | str]
    initial_conditions: dict[str, function | np.ndarray]
    boundary_conditions: tuple[tuple[float]]
    forcings: np.ndarray | None
    Kviscosity: float
    density: float
    poisson_iterations: int
    CFL_condition: float
    Nx: float
    dt: float
    Ndt: float
    
    def __post_init__(self) -> None:
        self.cxarr = xr.DataArray(np.zeros_like(uxarr.data[:,:,:]),
                                  dims=list([key for key in coords.keys()]),
                                  coords=coords)
        self.vxarr = xr.DataArray(np.zeros_like(uxarr.data[:,:,:]),
                                  dims=list([key for key in coords.keys()]),
                                  coords=coords)
        return
    
    def edit_coordinates(self, coords) -> None:

        
Config()

class Simulate(Config):
    """
    
    """
