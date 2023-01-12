# in python when we want to control a version for any particular project then
# we will use virtual environment
# to create a virtual env python -m venu myenv once you execute this myenu folder will be create
# to active this virtual env myenv\scripts\activate.bat or activate.ps1 if u are doing in powercell
# after that what ever you want to install you can install which will be only for this virtual env
# to deactivate the virtual env just u write deactivate
# if you want to know how many package is installed in your project then write pip freeze
# to write all the package version in any document write pip freeze >requirenment.txt
# to import all the requirenment.txt package for your project write pip install -r requirenment.txt

import math as m
print(f"{m.sqrt(4444):.2f}")