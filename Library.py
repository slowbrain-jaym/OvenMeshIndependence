import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import scipy.stats as stats
idx = pd.IndexSlice
pyo.init_notebook_mode()


def outlet_sorting(df, meshes):
    #food coordinates:

    for mesh in meshes:
        df = df.sort_index(axis=1)
        print(mesh)
        df.loc[:,idx[mesh,'row']] = np.NaN
        df.loc[:,idx[mesh,'col']] = 'null'
        df = df.sort_index(axis=1)

        df.loc[df.loc[: , idx[mesh,'x']]<0.24 , idx[mesh,'col']] = 0
        df.loc[df.loc[: , idx[mesh,'x']]>=0.24 , idx[mesh,'col']] = 1
        df = df.sort_values([(mesh,'z')], ascending=True)
        df.loc[df.loc[: , idx[mesh,'col']]==0 , idx[mesh,'row']] = \
        np.where(df.loc[df.loc[: , idx[mesh,'col']]==0 , idx[mesh,'z']].diff(1)>0.01,1,0)
        df.loc[df.loc[: , idx[mesh,'col']]==0 , idx[mesh,'row']] = \
        df.loc[df.loc[: , idx[mesh,'col']]==0 , idx[mesh,'row']].cumsum()

        df.loc[df.loc[: , idx[mesh,'col']]==1 , idx[mesh,'row']] = \
        np.where(df.loc[df.loc[: , idx[mesh,'col']]==1 , idx[mesh,'z']].diff(1)>0.01,1,0)
        df.loc[df.loc[: , idx[mesh,'col']]== 1, idx[mesh,'row']] = \
        df.loc[df.loc[: , idx[mesh,'col']]==1 , idx[mesh,'row']].cumsum()


        df = df.sort_index(axis=1)
    
    for mesh in meshes:
        df.loc[:,idx[mesh,'vT']] = df.loc[:,idx[mesh,'T']] * -df.loc[:,idx[mesh,'v']]
    
    means=pd.DataFrame()
    means['T'] = df.loc[:,idx[:,'T']].mean(axis=1)
    means['HTC'] = df.loc[:,idx[:,'HTC']].mean(axis=1)
    means['Flux'] = df.loc[:,idx[:,'Flux']].mean(axis=1)
    means['u'] = df.loc[:,idx[:,'u']].mean(axis=1)
    means['v'] = df.loc[:,idx[:,'v']].mean(axis=1)
    means['w'] = df.loc[:,idx[:,'w']].mean(axis=1)
    means['P'] = df.loc[:,idx[:,'P']].mean(axis=1)
    means['vT'] = df.loc[:,idx[:,'vT']].mean(axis=1)
    
    means.columns = pd.MultiIndex.from_arrays([['Mean']*8, ['T','HTC','Flux','u','v','w','P','vT']])
    df = df.join(means)
       
    df = df.sort_index(axis=1)
    
    return df

def inlet_heater_sorting(df): 
    df = df.sort_index(axis=1)
    means=pd.DataFrame()
    means['T'] = df.loc[:,idx[:,'T']].mean(axis=1)
    means['HTC'] = df.loc[:,idx[:,'HTC']].mean(axis=1)
    means['Flux'] = df.loc[:,idx[:,'Flux']].mean(axis=1)
    means['u'] = df.loc[:,idx[:,'u']].mean(axis=1)
    means['v'] = df.loc[:,idx[:,'v']].mean(axis=1)
    means['w'] = df.loc[:,idx[:,'w']].mean(axis=1)
    means['P'] = df.loc[:,idx[:,'P']].mean(axis=1)
    
    means.columns = pd.MultiIndex.from_arrays([['Mean']*7, ['T','HTC','Flux','u','v','w','P']])
    df = df.join(means)
    
    df = df.sort_index(axis=1)
    
    return df

