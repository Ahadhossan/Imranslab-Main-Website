# #!/bin/bash
# set -e

# echo ">>> SYSTEM INFORMATION"
# echo "Hostname       : $(hostname)"
# echo "OS             : $(lsb_release -ds)"
# echo "Kernel         : $(uname -r)"
# echo "Architecture   : $(uname -m)"
# echo "CPU Cores      : $(nproc)"
# echo "Total RAM      : $(free -h | awk '/^Mem:/{print $2}')"
# echo "Disk Available : $(df -h / | awk 'NR==2 {print $4}')"
# echo "Swap Enabled   : $(swapon --summary | wc -l)"

# echo ">>> DISABLING SWAP"
# sudo swapoff -a
# sudo sed -i '/ swap / s/^/#/' /etc/fstab

# echo ">>> LOADING KERNEL MODULES"
# sudo modprobe overlay
# sudo modprobe br_netfilter
# sudo modprobe ip_tables
# sudo modprobe nf_conntrack

# cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
# overlay
# br_netfilter
# ip_tables
# nf_conntrack
# EOF

# echo ">>> CONFIGURING SYSCTL"
# cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
# net.bridge.bridge-nf-call-iptables  = 1
# net.bridge.bridge-nf-call-ip6tables = 1
# net.ipv4.ip_forward                 = 1
# EOF
# sudo sysctl --system

# echo ">>> MOUNTING /sys/fs/bpf"
# sudo mkdir -p /sys/fs/bpf
# sudo mount -t bpf bpffs /sys/fs/bpf || true
# grep -q bpffs /etc/fstab || echo "bpffs /sys/fs/bpf bpf defaults 0 0" | sudo tee -a /etc/fstab

# echo ">>> INSTALLING CONTAINERD"
# sudo apt-get update
# sudo apt-get install -y \
#     apt-transport-https \
#     ca-certificates \
#     curl \
#     gnupg \
#     lsb-release \
#     software-properties-common 

# sudo mkdir -p /etc/apt/keyrings
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
#   sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# echo \
#   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
#   https://download.docker.com/linux/ubuntu \
#   $(lsb_release -cs) stable" | \
#   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# sudo apt-get update
# sudo apt-get install -y containerd.io

# echo ">>> CONFIGURING CONTAINERD"
# sudo mkdir -p /etc/containerd
# containerd config default | sudo tee /etc/containerd/config.toml > /dev/null

# sudo sed -i 's|sandbox_image = ".*"|sandbox_image = "registry.k8s.io/pause:3.10"|' /etc/containerd/config.toml
# sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

# sudo systemctl restart containerd
# sudo systemctl enable containerd

# echo ">>> INSTALLING KUBERNETES COMPONENTS"
# curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | \
#   gpg --dearmor | sudo tee /etc/apt/keyrings/kubernetes-apt-keyring.gpg > /dev/null

# echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /" | \
#   sudo tee /etc/apt/sources.list.d/kubernetes.list > /dev/null

# sudo apt-get update
# sudo apt-get install -y \
#     kubelet \
#     kubeadm \
#     kubectl
# sudo apt-mark hold kubelet kubeadm kubectl
# sudo systemctl enable kubelet

# echo ""
# echo ">>> KUBERNETES WORKER NODE SETUP COMPLETE"
# echo "Run the following command to join the cluster (ask your admin):"
# echo "sudo kubeadm join <MASTER_IP>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>"



#!/bin/bash
set -e

echo ">>> SYSTEM INFORMATION"
echo "Hostname       : $(hostname)"
echo "OS             : $(lsb_release -ds)"
echo "Kernel         : $(uname -r)"
echo "Architecture   : $(uname -m)"
echo "CPU Cores      : $(nproc)"
echo "Total RAM      : $(free -h | awk '/^Mem:/{print $2}')"
echo "Disk Available : $(df -h / | awk 'NR==2 {print $4}')"
echo "Swap Enabled   : $(swapon --summary | wc -l)"

echo ">>> DISABLING SWAP"
sudo swapoff -a
sudo sed -i '/ swap / s/^/#/' /etc/fstab

echo ">>> LOADING KERNEL MODULES"
sudo modprobe overlay
sudo modprobe br_netfilter
sudo modprobe ip_tables
sudo modprobe nf_conntrack

cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
ip_tables
nf_conntrack
EOF

echo ">>> CONFIGURING SYSCTL"
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF
sudo sysctl --system

echo ">>> MOUNTING /sys/fs/bpf"
sudo mkdir -p /sys/fs/bpf
sudo mount -t bpf bpffs /sys/fs/bpf || true
grep -q bpffs /etc/fstab || echo "bpffs /sys/fs/bpf bpf defaults 0 0" | sudo tee -a /etc/fstab

echo ">>> INSTALLING CONTAINERD"
sudo apt-get update
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    software-properties-common 

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  gpg --dearmor --no-tty | sudo tee /etc/apt/keyrings/docker.gpg > /dev/null

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y containerd.io

echo ">>> CONFIGURING CONTAINERD"
sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml > /dev/null

sudo sed -i 's|sandbox_image = ".*"|sandbox_image = "registry.k8s.io/pause:3.10"|' /etc/containerd/config.toml
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

sudo systemctl restart containerd
sudo systemctl enable containerd

echo ">>> INSTALLING KUBERNETES COMPONENTS"
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | \
  gpg --dearmor --no-tty | sudo tee /etc/apt/keyrings/kubernetes-apt-keyring.gpg > /dev/null

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /" | \
  sudo tee /etc/apt/sources.list.d/kubernetes.list > /dev/null

sudo apt-get update
sudo apt-get install -y \
    kubelet \
    kubeadm \
    kubectl
sudo apt-mark hold kubelet kubeadm kubectl
sudo systemctl enable kubelet

echo ">>> ✅ KUBERNETES WORKER NODE SETUP COMPLETE"
