"""Loads all the mesh data and saves it in a tidy table in csv form"""

import pandas as pd
import numpy as np


root_folder = r"C:\Users\jamen\Google Drive\Everything\Results\P1 Model\OvenMeshIndy\\"
meshes = [["Mesh1",0,60]]
areas = ["Food","Inlet","Outlet","Walls"]

alldata = []

for mesh in meshes:
    folder = root_folder + mesh[0]
    timesteps = np.arange(mesh[1],mesh[2],1)
    for timestep in timesteps:
        for area in areas:
            filename = folder+"\\"+area+str(timestep)+".csv"
            df = pd.read_csv(filename,header=3,error_bad_lines=False)
            df["timestep"] = timestep
            df["area"] = area
            df["mesh"] = mesh[0]
            alldata.append(df)
alldata = pd.concat(alldata)
column_names = {"X [ m ]":"x",
" Y [ m ]":"y",
" Z [ m ]":"z",
" Wall Heat Flux [ W m^-2 ]":"flux",
" Wall Heat Transfer Coefficient [ W m^-2 K^-1 ]":"HTC",
" Velocity u [ m s^-1 ]":"u",
" Velocity v [ m s^-1 ]":"v",
" Velocity w [ m s^-1 ]":"w",
" Pressure [ Pa ]":"P"
}
alldata = alldata.rename(columns=column_names)
alldata.to_csv(root_folder+"alldata.csv")



            


