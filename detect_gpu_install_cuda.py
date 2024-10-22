import subprocess
import os

def detect_gpu():
    try:
        # nvidia-smi command for getting gpu model
        gpu_info = subprocess.check_output(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"], encoding="utf-8")
        gpu_model = gpu_info.strip().split("\n")[0]  # Get the first GPU model
        print(f"Detected GPU model: {gpu_model}")
        return gpu_model
    except Exception as e:
        print(f"Error detecting GPU: {e}")
        return None

# install CUDA and cuDNN via Conda based gpu
def install_cuda_cudnn(gpu_model):
    # Create a base command for Anaconda installation
    conda_install_base = ["conda", "install", "-y", "-n", "tensorflow_env"]

    # Map the GPU to appropriate CUDA and cuDNN versions
    if "A100" in gpu_model:
        print("Installing CUDA 11.4 and cuDNN 8.2")
        conda_install_base.extend(["cudatoolkit=11.4", "cudnn=8.2", "tensorflow-gpu"])
    elif "RTX 4090" in gpu_model or "RTX 4080" in gpu_model:
        print("Installing CUDA 11.8 and cuDNN 8.6")
        conda_install_base.extend(["cudatoolkit=11.8", "cudnn=8.6", "tensorflow-gpu"])
    elif "RTX 3090" in gpu_model or "RTX 3090 Ti" in gpu_model:
        print("Installing CUDA 11.4 and cuDNN 8.2")
        conda_install_base.extend(["cudatoolkit=11.4", "cudnn=8.2", "tensorflow-gpu"])
    elif "RTX 3060" in gpu_model:
        print("Installing CUDA 11.1 and cuDNN 8.0")
        conda_install_base.extend(["cudatoolkit=11.1", "cudnn=8.0", "tensorflow-gpu"])
    else:
        print("Installing default CUDA 10.1 and cuDNN 7.6")
        conda_install_base.extend(["cudatoolkit=10.1", "cudnn=7.6", "tensorflow-gpu"])

    subprocess.run(conda_install_base)
def main():
    gpu_model = detect_gpu()
    if gpu_model:
        install_cuda_cudnn(gpu_model)
    else:
        print("No compatible GPU detected. Exiting...")

if __name__ == "__main__":
    main()
