"""Loads all the mesh data and saves it in a tidy table in feather form"""

import pandas as pd
import numpy as np

# Set the working directory as well as the names and 
# number of mesh files in each folder
root_folder = r"C:\Users\jamen\Google Drive\Everything\Results\P1 Model\OvenMeshIndy\\"
meshes = [["Mesh0",0,60,1],["Mesh1",0,60,1],["Mesh2",0,60,1],["Mesh3",0,60,1],
["Mesh4",0,60,1],["Mesh5",0,60,1],["Mesh6",0,60,1],["Mesh7",0,60,1],["Mesh8",0,60,1]] 
# name, first timestep, final timestep, timestep
areas = ["Food","Inlet","Outlet","Walls"] # prefix for each filename

meshdata_file = "OvenMeshIndi.xlsx"
meshdata= pd.read_excel(root_folder+meshdata_file)

alldata = []

for mesh in meshes:
    folder = root_folder + mesh[0]
    timesteps = np.arange(mesh[1],mesh[2],1)
    for timestep in timesteps:
        for area in areas:
            filename = folder+"\\"+area+str(timestep)+".csv"
            df = pd.read_csv(filename,header=3,error_bad_lines=False)
            df["time"] = timestep*mesh[3]-mesh[1]
            df["area"] = area
            df["mesh"] = mesh[0]
            alldata.append(df)
alldata = pd.concat(alldata)
column_names = {"X [ m ]":"x",
" Y [ m ]":"y",
" Z [ m ]":"z",
" Temperature [ K ]":"T",
" Wall Heat Flux [ W m^-2 ]":"flux",
" Wall Heat Transfer Coefficient [ W m^-2 K^-1 ]":"HTC",
" Velocity u [ m s^-1 ]":"u",
" Velocity v [ m s^-1 ]":"v",
" Velocity w [ m s^-1 ]":"w",
" Pressure [ Pa ]":"P"
}

#print(meshdata.columns)

alldata = alldata.rename(columns=column_names)
alldata = pd.merge(alldata, meshdata, on="mesh")

#print(alldata.columns)

alldata = alldata.reset_index()
alldata.to_feather(root_folder+"alldata.feather")



            


