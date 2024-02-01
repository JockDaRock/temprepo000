apt update

apt install -y libvulkan1 libgl1 libglib2.0-0

# Install CUDA toolkit 11.8
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run

sh cuda_11.8.0_520.61.05_linux.run --silent --toolkit

# Install NVIDIA driver 530
add-apt-repository ppa:graphics-drivers/ppa

apt install -y nvidia-driver-515


# Open TCP port 43210 (optional)
# sudo ufw allow 43210

wget https://github.com/Juice-Labs/Juice-Labs/releases/latest/download/JuiceServer-linux.tar.gz

mkdir JuiceServer

cd JuiceServer

tar -xf ../JuiceServer-linux.tar.gz

#reboot