#  Lidar to radar translation for autonomous vehicles using GAN (Generative adverserial networks )
# Project Introduction

In this project, our objective is to understand how to customize an onboard LiDAR model according to the specifications of a desired RADAR field of view, resolution, and range. Additionally, we aim to employ a density-based clustering algorithm to generate RADAR-like output within an open-source graphical engine, specifically Unreal Engine (UE).

## Key Points

1. **Lack of RADAR Sensor Modeling in Open-Source Simulators**
   
   A survey of available open-source simulators has highlighted the minimal attention given to modeling RADAR (Radio Detection and Ranging) sensors.

2. **RADAR Models in Private vs. Open-Source Simulators**
   
   While high-fidelity RADAR models are accessible within private simulation tools like MATLAB's automated driving toolbox, there is a noticeable absence of such models in open-source simulators like AirSim. This gap necessitates the development of realistic automobile RADAR sensor models.

3. **Contrasting LiDAR and RADAR Characteristics**
   
   LiDAR systems are more vulnerable to adverse weather conditions such as rain and dust. On the other hand, RADAR relies on frequency modulated continuous wave (FMCW) technology, making it immune to these weather conditions. However, RADAR's performance is influenced by a different set of environmental variables, such as temperature.

4. **LiDAR Emulating RADAR**
   
   The outcome of our project involves the successful creation of a LiDAR sensor model that is capable of replicating RADAR detection capabilities. Additionally, we have ensured that the LiDAR model possesses a suitable operational range.


## Differences between RADAR and LIDAR

1. **LIDAR Characteristics**

   LIDAR technology is capable of detecting small objects with short wavelengths. It excels at creating highly accurate 3D monochromatic images of objects. However, there are certain disadvantages associated with LIDAR:

   - **Limited Visibility in Low Light Conditions:** LIDAR's effectiveness diminishes in dark or overcast weather conditions, making its usage less optimal under such circumstances.
   - **Operational Height Range:** LIDAR operates effectively within the range of 500 to 2000 meters.
   - **Costly Technology:** LIDAR is considered a high-priced technology, which can be a limiting factor in certain applications.

2. **RADAR Characteristics**

   RADAR is capable of functioning in overcast weather and during the night. It has a long operating distance. However, RADAR has its own set of drawbacks:

   - **Limitation in Detecting Small Objects:** RADAR struggles to detect smaller objects at shorter wavelengths.
   - **Lack of Precise Imaging:** Due to its longer wavelength, RADAR cannot provide a precise image of an object to the user.








