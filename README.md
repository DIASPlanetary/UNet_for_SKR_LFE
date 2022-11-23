[![DOI](https://zenodo.org/badge/562262047.svg)](https://zenodo.org/badge/latestdoi/562262047)
# UNet_for_SKR_LFE
Full code for the preparation of training and test set, as well as implementation of U-Net for semantic segmentation of Low Frequency Extensions of Saturn Kilometric Radiation.

## Download the code and store according to: <br>
- Folder <br> 
    - UNET_for_SKR_LFE 
        - 0_prepare_data.py
        - 1_prepare_data.py
        - 2_prepare_data.py
        - 3_prepare_data.py
        - 4_prepare_data.py
        - 5_prepare_data.py
        - UNET.ipynb
    - input_data
      - SKR_2004_CJ.sav
      - ...
      - SKR_2017_001-258_CJ.sav 
      - 2004_FGM_KRTP_1M.TAB
      - ...
      - 2017_FGM_KRTP_1M.TAB
      - 2004_FGM_KSM_1M.TAB
      - ...
      - 2004_FGM_KSM_1M.TAB
    - output_data
      - ML_lfes.json
    - ML_Dataset
        - flux_images
        - pol_images
        - mask_images
## Description of files
Need to run prepare data files in order and change variable `root` to path to Folder at the top of each script.
### 0_prepare_data.py 
Compile trajectory data from given files and store as single .csv file for each year in output_data folder.
### 1_prepare_data.py
Separate data with LFEs fully labelled and extract empty intervals (without LFE) into 5 hour chunks. Save .csv file of start and end times of both LFEs and non-LFEs along with class label to output_data.
### 2_prepare_data.py 
Plot and save spectrogram images and corresponding binary mask for each labelled instance of LFE/Non-LFE.
### 3_prepare_data.py 
Perform data augmentation and plot and save spectrogram images and corresponding binary mask.
### 4_prepare_data.py 
Save .csv file with start and end times of LFEs, Non-LFEs and augmented data along with corresponding latitude median and standard deviation and local time median and standard deviation over each interval.
### 5_prepare_data.py 
Separate data into train and test, and save images, masks and labels to folders corresponding to index of each image.
### UNET.ipynb
Implementation of modified U-NET.
