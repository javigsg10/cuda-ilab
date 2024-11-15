# Executing a Instructlab Containerfile with Podman on a System with NVIDIA GPU

This implementation was made on a **VSI RHEL 9 system (architecture x86_64) with an NVIDIA L40 GPU**, and the `Containerfile` includes modifications based on the official [Instructlab repository](https://github.com/instructlab/instructlab).

## Prerequisites

1. **NVIDIA GPU**  
   Ensure your system is equipped with an NVIDIA GPU that is compatible with the workloads you intend to run.

2. **Linux System with GCC Compiler and Toolchain**  
   Use a supported version of Linux that includes a `gcc` compiler and the necessary toolchain.

3. **NVIDIA Driver**  
   Install the appropriate NVIDIA driver for your GPU. For more information, refer to the [NVIDIA driver downloads page](https://developer.nvidia.com/datacenter-driver-downloads).

## Installation Steps

### 1. Install NVIDIA Drivers
Follow the instructions on the [NVIDIA driver downloads page](https://developer.nvidia.com/datacenter-driver-downloads) to download and install the driver for your GPU. Verify the installation with:

```bash
nvidia-smi
```

### 2. **NVIDIA Container Toolkit**  
Install the NVIDIA Container Toolkit to enable integration of NVIDIA GPUs with container runtimes, including Podman.

```bash
dnf install nvidia-container-toolkit-base
```

### 3. **Podman with CDI Support**  
Podman is only supported for the **Container Device Interface (CDI)** specification. Generate CDI especifcation file.
   
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
List CDIs:

```bash
nvidia-ctk cdi list
```
    
### 4. Running ilab image with CDI
Once your image is built from `Containerfile` you can run:

```bash
podman run --rm --device nvidia.com/gpu=all -it <your-image-name>
```
