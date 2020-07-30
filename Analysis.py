import pandas as pd
import numpy as np

root_folder = r"C:\Users\jamen\Google Drive\Everything\Results\P1 Model\OvenMeshIndy\\"
meshes = [["Mesh1",0,60]] # name, first timestep, final timestep
areas = ["Food","Inlet","Outlet","Walls"] # prefix for each filename

alldata = pd.read_csv(root_folder+"alldata.csv")

means = []
for timestep in np.arange(0,60,1):
    mean = np.mean(alldata[alldata["timestep"]==timestep]['flux'])
    means.append(mean)