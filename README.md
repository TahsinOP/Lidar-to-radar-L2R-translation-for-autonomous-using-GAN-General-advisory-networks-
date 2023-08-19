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


