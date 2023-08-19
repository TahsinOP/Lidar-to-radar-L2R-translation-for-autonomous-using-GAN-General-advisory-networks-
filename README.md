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

# LIDAR to RADAR Translation

1. We introduce the "L2R Generative Adversarial Network," a conditional model designed to convert LiDAR data into RADAR data.

2. The GAN facilitates image-to-image conditional translation, resulting in three distinct representations of RADAR data:
   - Raw Polar RADAR Spectrum
   - RADAR Spectrum in Cartesian Coordinates
   - 3D RADAR Point Clouds and 2D RADAR Pins

3. The original RADAR data is initially in the form of a 2D array, which is not directly accessible to users. This challenge is addressed by employing Digital Signal Processing (DSP) algorithms like Fast Fourier Transform (FFT) and Multiple Signal Classification (MUSIC) to derive polar RADAR data.

4. Moving forward, we implement a baseline utilizing pix2pix and pix2pixHD methodologies to generate high-resolution RADAR data/spectrum from the LiDAR point cloud. This approach leverages a GAN framework for image-to-image translation, accompanied by loss functions.

5. Our research concludes that the L2R GAN neural network model holds significant promise in producing RADAR images. The model employs global generators for large regions and local generators for small regions. Furthermore, it can be employed to generate RADAR data for critical scenarios, such as pedestrian collision warnings.

# Prerequisites

Before proceeding with the sensor fusion using synthetic radar and vision data simulation, ensure you have the following prerequisites in place:

1. **MATLAB Installation:**
   You should have MATLAB installed on your system. If you don't have MATLAB, you can obtain it from the official MathWorks website.

2. **Sensor Fusion Toolbox:**
   Ensure that you have access to the Sensor Fusion Toolbox within MATLAB. This toolbox provides essential functionality for working with sensor data fusion and related applications.

3. **Autonomous Driving Toolbox:**
   The Autonomous Driving Toolbox is another crucial component needed for this simulation. It offers specialized tools for developing perception, sensor fusion, and control algorithms in the context of autonomous systems.

## Getting the Toolboxes

If you already have MATLAB installed, you can acquire the Sensor Fusion Toolbox and Autonomous Driving Toolbox through the MATLAB Add-Ons menu or MathWorks website.

## Verify Installation

To verify that you have the necessary toolboxes installed, open MATLAB and execute the following commands in the Command Window:

```matlab
% Check for Sensor Fusion Toolbox
sensorFusionToolboxInstalled = license('test', 'Sensor_Fusion_Toolbox');

% Check for Autonomous Driving Toolbox
autonomousDrivingToolboxInstalled = license('test', 'Automated_Driving_Toolbox');

disp(['Sensor Fusion Toolbox Installed: ', num2str(sensorFusionToolboxInstalled)]);
disp(['Autonomous Driving Toolbox Installed: ', num2str(autonomousDrivingToolboxInstalled)]);

```
# Simulation Using MATLAB

To demonstrate the principles of sensor fusion and autonomous driving , we will use MATLAB to run a simulation that showcases the fusion of synthetic radar and vision data. The simulation will illustrate how the combined information from these sensors can provide a more comprehensive perception of the surroundings

## 1. Sensor Fusion Using Synthetic Radar and Vision Data

In this section, we delve into the concept of sensor fusion, where synthetic radar and vision data are combined for enhanced perception and understanding of the environment. This integration of data from multiple sensors can lead to improved accuracy and reliability in various applications.

![simulation](https://in.mathworks.com/help/examples/driving/win64/SensorFusionUsingSyntheticDataExample_01.png)



Please use the following MATLAB command to initiate the simulation:

```matlab
openExample('driving/SensorFusionUsingSyntheticDataExample)

```

## 2. Track-Level Fusion of Radar and Lidar Data

This example demonstrates how to generate an object-level track list from measurements obtained from both a radar and a lidar sensor. Additionally, it showcases the fusion of these measurements using a track-level fusion scheme. The radar measurements are processed using an extended object tracker, while the lidar measurements are handled using a joint probabilistic data association (JPDA) tracker.

![Workflow](https://in.mathworks.com/help/examples/shared_driving_fusion_lidar/win64/xxRadarLidarTrackFusionWorkflow.png)

Below is the MATLAB code example that showcases the track-level fusion of radar and lidar data. Make sure you have the required toolboxes installed and configured before running the code.

```matlab
openExample('shared_driving_fusion_lidar/RadarAndLidarTrackFusionExample')
```
# Future Implementations 

The python code using the L2R Generative Adverserial Networks ( GAN ) will be implemented in Unreal Engine for a proper 3-D graphic simulation of Autonomous driving with fusion of LIDAR and RADAR data

