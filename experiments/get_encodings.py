## Testing Points
from MORALS.systems.utils import get_system
from MORALS.models import *
from MORALS.dynamics_utils import DynamicsUtils
from MORALS.data_utils import DynamicsDataset
import dytop.Grid as Grid
import argparse

import dytop.CMGDB_util as CMGDB_util
import dytop.RoA as RoA
import dytop.dyn_tools as dyn_tools

import numpy as np
import os

from MORALS.systems.pendulum import *

config_path = "/nas/home/ashwinb/robotic_manipulation/MORALS/experiments/config/pendulum/pendulum_lqr_2.txt"

with open(config_path) as f:
        config = eval(f.read())

dyn_utils = DynamicsUtils(config)
model  = Pendulum()

x =   [
    [3.141592653589793116e+00, -2.026833970057930756e-01],
    [3.033315696041743337e+00, -1.699719010038497347e+00],
    [2.798006635045007684e+00, -2.481733916260282058e+00],
    [2.513515208610996865e+00, -2.598135192393367099e+00],
    [2.242830096693554154e+00, -2.259310459568842244e+00],
    [2.022421360550808345e+00, -1.715972349882604053e+00],
    [1.864090387530081383e+00, -1.152521163105182156e+00],
    [1.764401431193744596e+00, -6.604953724673090498e-01],
    [1.713689215792630227e+00, -2.657990369996300895e-01],
    [1.701368290017099882e+00, 3.680054337364013078e-02],
    [1.718040016506884982e+00, 2.613624072646679175e-01],
    [1.755832285204816046e+00, 4.206087936045390663e-01],
    [1.808055386909066309e+00, 5.231049942833724264e-01],
    [1.868764344320622772e+00, 5.740112551498010030e-01],
    [1.932492923569682608e+00, 5.772311924264345029e-01],
    [1.994240344264270215e+00, 5.376967681430174784e-01],
    [2.049678298327838988e+00, 4.629546522977070477e-01],
    [2.095471001324491489e+00, 3.635462844177295150e-01],
    [2.129567020867119798e+00, 2.521029968412323852e-01],
    [2.151338297621787188e+00, 1.415420196064899605e-01],
    [2.161502448804932364e+00, 4.304590756474013791e-02]
]
x = np.array(x)

transformed_points =  model.transform(x)
sb = 16
dim_latent_space = config['low_dims']
lower_bounds = [-1]*dim_latent_space
upper_bounds = [1]*dim_latent_space
print("Bounds for encoded space", lower_bounds, upper_bounds)

grid = Grid.Grid(lower_bounds, upper_bounds, sb)

latent_space_sample = dyn_utils.encode(transformed_points, normalize=False)
print(latent_space_sample)


# x = np.array([[-0.376,-0.142]])

# decoded = dyn_utils.decode(x)

# print(model.reverse_transform(decoded))
