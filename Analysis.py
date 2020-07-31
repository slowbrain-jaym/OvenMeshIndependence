import pandas as pd
import numpy as np

root_folder = r"C:\Users\jamen\Google Drive\Everything\Results\P1 Model\OvenMeshIndy\\"
meshes = [["Mesh1",0,60]] # name, first timestep, final timestep
areas = ["Food","Inlet","Outlet","Walls"] # prefix for each filename

alldata = pd.read_feather(root_folder+"alldata.feather")

timestep_means = {}
for timestep in np.arange(0,60,1):
    timestep_means['flux'] = np.mean(alldata[alldata["timestep"]==timestep]['flux'])
    timestep_means['HTC'] = np.mean(alldata[alldata["timestep"]==timestep]['HTC'])
    timestep_means['P'] = np.mean(alldata[alldata["timestep"]==timestep]['P'])
    timestep_means['T'] = np.mean(alldata[alldata["timestep"]==timestep]['T'])

