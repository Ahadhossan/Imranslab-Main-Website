🔹 Step 1: Disable Swap
```bash
```
```
🔹 Step 2: Install Container Runtime (Containerd)
```bash
sudo apt update && sudo apt install -y containerd
```
# Configure containerd
sudo mkdir -p /etc/containerd
sudo containerd config default | sudo tee /etc/containerd/config.toml

# Restart and enable
sudo systemctl restart containerd
sudo systemctl enable containerd
```
🔹 Step 3: Set Kernel Parameters
```bash
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

# Sysctl settings
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
net.bridge.bridge-nf-call-ip6tables = 1
EOF

sudo sysctl --system
```
🔹 Step 4: Install Kubernetes Packages (kubeadm, kubelet, kubectl)
```bash
sudo apt update && sudo apt install -y apt-transport-https ca-certificates curl

sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg

echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] \
https://apt.kubernetes.io/ kubernetes-xenial main" | \
sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt update
sudo apt install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```
🔹 Step 5: Initialize Kubernetes Cluster (Master Node)
```bash
sudo kubeadm init --pod-network-cidr=192.168.0.0/16
```

You can specify a different CIDR based on the network plugin (see Calico/Flannel below).

Save the kubeadm join command printed at the end.


🔹 Step 6: Set Up kubeconfig for Admin User
```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```
🔹 Step 7: Install a CNI Plugin (Flannel, Calico, etc.)
Option 1: Flannel
```bash
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```
Option 2: Calico (more powerful, network policy support)
```bash
kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.25.0/manifests/calico.yaml
```
🔹 Step 8: Verify Cluster is Running
```bash
kubectl get nodes
kubectl get pods -A
```

### Get the join command from the k8s-master
```bash
kubeadm token create --print-join-command
```