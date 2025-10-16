# #!/bin/bash
# set -e

# ROLE="$1" # "master" or "worker"

# if [[ -z "$ROLE" || ("$ROLE" != "master" && "$ROLE" != "worker") ]]; then
#   echo "Usage: $0 [master|worker]"
#   exit 1
# fi

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

# sudo tee /etc/modules-load.d/k8s.conf <<EOF
# overlay
# br_netfilter
# EOF

# sudo tee /etc/sysctl.d/k8s.conf <<EOF
# net.bridge.bridge-nf-call-iptables  = 1
# net.bridge.bridge-nf-call-ip6tables = 1
# net.ipv4.ip_forward                 = 1
# EOF

# sudo sysctl --system

# echo ">>> INSTALLING CONTAINERD"
# sudo apt-get update
# sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release software-properties-common

# sudo mkdir -p /etc/apt/keyrings
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
#   sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# echo \
#   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
#   $(lsb_release -cs) stable" | \
#   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# sudo apt-get update
# sudo apt-get install -y containerd.io

# echo ">>> CONFIGURING CONTAINERD"
# sudo mkdir -p /etc/containerd
# containerd config default | sudo tee /etc/containerd/config.toml > /dev/null
# sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
# sudo systemctl restart containerd
# sudo systemctl enable containerd

# echo ">>> ADDING KUBERNETES APT REPO"
# sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key
# echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /" | \
#   sudo tee /etc/apt/sources.list.d/kubernetes.list

# sudo apt-get update
# sudo apt-get install -y kubelet kubeadm kubectl
# sudo apt-mark hold kubelet kubeadm kubectl

# echo ">>> ENABLEING KUBELET"
# sudo systemctl enable kubelet

# if [[ "$ROLE" == "master" ]]; then
#   echo ">>> READY FOR MASTER INITIALIZATION"
#   echo "Run the following to initialize your master node:"
#   echo ""
#   echo "  sudo kubeadm init --pod-network-cidr=192.168.0.0/16"
#   echo ""
#   echo "After that:"
#   echo "  mkdir -p \$HOME/.kube"
#   echo "  sudo cp -i /etc/kubernetes/admin.conf \$HOME/.kube/config"
#   echo "  sudo chown \$(id -u):\$(id -g) \$HOME/.kube/config"
#   echo ""
#   echo "Then install a CNI plugin, e.g., Calico:"
#   echo "  kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.0/manifests/calico.yaml"

# else
#   echo ">>> WORKER NODE SETUP COMPLETE"
#   echo "Ask your admin for the join command and run it like:"
#   echo ""
#   echo "  sudo kubeadm join <MASTER_IP>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>"
# fi


# #!/bin/bash
# set -e

# ROLE="$1"  # Expected: "master" or "worker"

# if [[ -z "$ROLE" || ("$ROLE" != "master" && "$ROLE" != "worker") ]]; then
#   echo "Usage: $0 [master|worker]"
#   exit 1
# fi

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

# cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
# overlay
# br_netfilter
# EOF

# cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
# net.bridge.bridge-nf-call-iptables  = 1
# net.bridge.bridge-nf-call-ip6tables = 1
# net.ipv4.ip_forward                 = 1
# EOF

# sudo sysctl --system

# echo ">>> INSTALLING CONTAINERD"
# sudo apt-get update
# sudo apt-get install -y \
#     apt-transport-https \
#     ca-certificates \
#     curl \
#     gnupg \
#     lsb-release \
#     software-properties-common 

# # Docker repo
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
# sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
# sudo systemctl restart containerd
# sudo systemctl enable containerd

# echo ">>> ADDING KUBERNETES APT REPO"
# sudo mkdir -p /etc/apt/keyrings
# curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | \
#   gpg --dearmor | sudo tee /etc/apt/keyrings/kubernetes-apt-keyring.gpg > /dev/null

# echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /" | \
#   sudo tee /etc/apt/sources.list.d/kubernetes.list > /dev/null

# sudo apt-get update
# sudo apt-get install -y \
#     kubelet \
#     kubeadm \
#     kubectl
# sudo apt-mark hold \
#     kubelet \
#     kubeadm \
#     kubectl
# echo ">>> ENABLING KUBELET"
# sudo systemctl enable kubelet

# if [[ "$ROLE" == "master" ]]; then
#   echo ">>> INITIALIZATION INSTRUCTIONS"
#   echo ""
#   echo "Run the following command to initialize your master node:"
#   echo ""
#   echo "  sudo kubeadm init --pod-network-cidr=192.168.0.0/16"
#   echo ""
#   echo "Then configure kubectl for your user:"
#   echo ""
#   echo "  mkdir -p \$HOME/.kube"
#   echo "  sudo cp -i /etc/kubernetes/admin.conf \$HOME/.kube/config"
#   echo "  sudo chown \$(id -u):\$(id -g) \$HOME/.kube/config"
#   echo ""
#   echo "Install the Calico CNI plugin:"
#   echo ""
#   echo "  kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.0/manifests/calico.yaml"
# else
#   echo ">>> WORKER NODE SETUP COMPLETE"
#   echo "To join this worker to the cluster, run the join command shown on the master node after kubeadm init."
# fi


#!/bin/bash
set -e

ROLE="$1"  # Expected: "master" or "worker"

if [[ -z "$ROLE" || ("$ROLE" != "master" && "$ROLE" != "worker") ]]; then
  echo "Usage: $0 [master|worker]"
  exit 1
fi

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
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

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

# Fix for the kubeadm pause image warning
sudo sed -i 's|sandbox_image = ".*"|sandbox_image = "registry.k8s.io/pause:3.10"|' /etc/containerd/config.toml
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

sudo systemctl restart containerd
sudo systemctl enable containerd

echo ">>> INSTALLING KUBERNETES COMPONENTS"
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | \
  gpg --dearmor | sudo tee /etc/apt/keyrings/kubernetes-apt-keyring.gpg > /dev/null

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /" | \
  sudo tee /etc/apt/sources.list.d/kubernetes.list > /dev/null

sudo apt-get update
sudo apt-get install -y \
    kubelet \
    kubeadm \
    kubectl
sudo apt-mark hold \
    kubelet \
    kubeadm \
    kubectl
sudo systemctl enable kubelet

if [[ "$ROLE" == "master" ]]; then
  echo ""
  echo ">>> KUBERNETES MASTER NODE SETUP READY"
  echo ""
  echo "Run this command to initialize the master node:"
  echo "--------------------------------------------------"
  echo "sudo kubeadm init --pod-network-cidr=192.168.0.0/16 #done"
  echo "--------------------------------------------------"
  echo ""
  echo "Then run the following to configure kubectl:"
  echo "mkdir -p \$HOME/.kube"
  echo "sudo cp -i /etc/kubernetes/admin.conf \$HOME/.kube/config"
  echo "sudo chown \$(id -u):\$(id -g) \$HOME/.kube/config"
  echo ""
  echo "Finally, install the Calico CNI plugin:"
  echo "kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.30.0/manifests/calico.yaml"
  echo ""
else
  echo ""
  echo ">>> KUBERNETES WORKER NODE SETUP COMPLETE"
  echo ""
  echo "Ask the admin for the join command and run:"
  echo "sudo kubeadm join <MASTER_IP>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>"
fi