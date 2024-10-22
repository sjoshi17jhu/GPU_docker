# Use a Windows base image with NVIDIA GPU support
FROM mcr.microsoft.com/windows:20H2

# Download and install Anaconda if not done
RUN powershell -Command `
    Invoke-WebRequest -Uri https://repo.anaconda.com/archive/Anaconda3-2023.07-Windows-x86_64.exe -OutFile Anaconda3.exe; `
    Start-Process .\Anaconda3.exe -ArgumentList '/S /D=C:\Anaconda3' -NoNewWindow -Wait; `
    Remove-Item .\Anaconda3.exe

# hancle anaconda system environment
ENV PATH="C:\\Anaconda3;C:\\Anaconda3\\Scripts;C:\\Anaconda3\\condabin:$PATH"

#  detect GPU
RUN powershell -Command `
    Invoke-WebRequest -Uri https://developer.download.nvidia.com/compute/cuda/repos/wsl2/x86_64/cuda-wsl2.repo -OutFile cuda-wsl2.repo

# detect gpu
COPY detect_gpu_install_cuda.py C:\\detect_gpu_install_cuda.py

ENTRYPOINT ["python", "C:\\detect_gpu_install_cuda.py"]
