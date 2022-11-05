# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:05:27 2022

@author: eliza
"""
import pandas as pd
from datetime import datetime
root='C:/Users/eliza/Desktop/Python_Scripts/'
def traject(year):
    
    fp_krtp=root+"input_data/{}_FGM_KRTP_1M.TAB".format(year)

    df=pd.read_csv(fp_krtp, header=None,delim_whitespace=True)
    df = df.rename(columns={0: 'Time_isot',1:'B_r(nT)',2:'B_theta(nT)',3:'B_phi(nT)',
                            4:'B_total(nT)',5:'Range(R_s)',6:'Latitude',7: "East_Longitude",
                            8:'Local_Time',9:'NPTS'})
    func_tstmp_todoy = lambda x: ((x -datetime(int(datetime.strftime(x,'%Y')),1,1)).total_seconds()/86400) +1
    time_dt = df['Time_isot'].apply(lambda x: datetime.fromisoformat(x))
    doy_frac=list(map(func_tstmp_todoy, time_dt))
    fp_ksm="C:/Users/eliza/Desktop/git_folder/ML_For_SKR_Code/input_data/{}_FGM_KSM_1M.TAB".format(year)
    df_ksm=pd.read_csv(fp_ksm, header=None,delim_whitespace=True)
    df_ksm = df_ksm.rename(columns={0: 'Time_isot',1:'B_x(nT)',2:'B_y(nT)',3:'B_z(nT)',
                            4:'B_total(nT)',5:'X(R_s)',6:'Y(R_s)',7: "Z(R_s)",
                            8:'Local_Time',9:'NPTS'})

    df_final =pd.DataFrame({'datetime_ut': time_dt, 'bphi_krtp':df['B_phi(nT)'],
                                    'br_krtp':df['B_r(nT)'],
                                    'btheta_krtp':df['B_theta(nT)'],
                                    'btotal':df['B_total(nT)'],
                                    'doyfrac':doy_frac,
                                    'lat':df['Latitude'],
                                    'localtime':df['Local_Time'],
                                    'range':df['Range(R_s)'],
                                    'xpos_ksm':df_ksm['X(R_s)'],
                                    'ypos_ksm':df_ksm['Y(R_s)'],
                                    'zpos_ksm':df_ksm['Z(R_s)']})
    return df_final
for year in range(2004,2018, 1):
    #Dataframe with trajectory information.
    #columns are: 'datetime_ut','bphi_krtp' 'br_krtp' 'btheta_krtp' 'btotal' 'doyfrac'
     # 'lat' 'localtime'  'range' 'xpos_ksm' 'ypos_ksm' 'zpos_ksm'
    traj_df = traject(year)  
    
    fp = root+'output_data/trajectory{}.csv'.format(year)
    traj_df.to_csv(fp, index=False)