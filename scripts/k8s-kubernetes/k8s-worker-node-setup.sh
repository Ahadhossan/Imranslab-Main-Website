#!/bin/bash

# List of worker IPs
AGENT_IPS=(
  "192.168.2.181"
  "192.168.2.7"
  "192.168.2.223"
  "192.168.2.140"
  "192.168.2.18"
  "192.168.2.71"
  "192.168.2.240"
  "192.168.2.194"
)  # Replace with your actual agent IPs

# SSH user
SSH_USER="k8s-agent"  # or whatever user you're using

# The kubeadm join command (copy from master output)
JOIN_COMMAND="kubeadm join 192.168.2.11:6443 --token 1gduob.s35ho0cxawsvne1j \
--discovery-token-ca-cert-hash sha256:18ded8fc9a2fd39e04691608338f069d06f6790129ef8aaf7898e0d02e8096a2"

# Loop over each agent and execute setup + join
for ip in "${AGENT_IPS[@]}"; do
  echo "=== Connecting to $ip ==="
  
  ssh "${SSH_USER}@${ip}" <<EOF
sudo apt update && sudo apt install -y kubeadm kubelet kubectl
sudo swapoff -a
sudo sed -i '/ swap / s/^/#/' /etc/fstab
sudo systemctl enable kubelet && sudo systemctl start kubelet
sudo ${JOIN_COMMAND}
EOF

  echo "=== Finished setup on $ip ==="
done


#!/bin/bash

# List of worker node IPs
AGENT_IPS=(
  "192.168.2.101"
  "192.168.2.102"
)

# SSH username
SSH_USER="ubuntu"  # Change this to your SSH user

# Loop through each agent and run the setup
for ip in "${AGENT_IPS[@]}"; do
  echo ">>> Connecting to $ip"

  # Copy the setup script
  scp setup.sh "$SSH_USER@$ip:/tmp/setup.sh"

  # Run the script with 'worker' argument
  ssh "$SSH_USER@$ip" "sudo bash /tmp/setup.sh worker"

  echo ">>> Done with $ip"
done






#!/bin/bash

# List of worker node IPs
AGENT_IPS=(
  "192.168.2.181"
  "192.168.2.7"
  "192.168.2.223"
  "192.168.2.140"
  "192.168.2.18"
  "192.168.2.71"
  "192.168.2.240"
  "192.168.2.194"
)

# SSH username
SSH_USER="k8s-agent"
SETUP_SCRIPT="worker-setup-k8s.sh"  # Path to your setup script

# The kubeadm join command (copy from master output)
JOIN_COMMAND="kubeadm join 192.168.2.11:6443 --token 1gduob.s35ho0cxawsvne1j \
--discovery-token-ca-cert-hash sha256:18ded8fc9a2fd39e04691608338f069d06f6790129ef8aaf7898e0d02e8096a2"


# SSH options to skip host key checking and known_hosts prompt
SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"


echo ">>> Configuring passwordless sudo for user: $SSH_USER"

for ip in "${AGENT_IPS[@]}"; do
  ssh $SSH_OPTS "$SSH_USER@$ip" "echo '$SSH_USER ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/$SSH_USER >/dev/null && sudo chmod 440 /etc/sudoers.d/$SSH_USER"
done

echo ">>> Passwordless sudo configured on all agents"


# Loop through each worker and execute setup
for ip in "${AGENT_IPS[@]}"; do
  echo ">>> Executing setup on $ip"

  # Run setup.sh remotely (without argument now)
  ssh $SSH_OPTS "$SSH_USER@$ip" 'sudo bash' < "$SETUP_SCRIPT"

  # Execute join command
  ssh $SSH_OPTS "$SSH_USER@$ip" "sudo $JOIN_COMMAND"

  echo ">>> Done with $ip"
done






#!/bin/bash

AGENT_IPS=(
  "192.168.2.181"
  "192.168.2.7"
  "192.168.2.223"
  "192.168.2.140"
  "192.168.2.18"
  "192.168.2.71"
  "192.168.2.240"
  "192.168.2.194"
)

SSH_USER="k8s-agent"
SETUP_SCRIPT="worker-setup-k8s.sh"

JOIN_COMMAND="kubeadm join 192.168.2.11:6443 --token 1gduob.s35ho0cxawsvne1j \
--discovery-token-ca-cert-hash sha256:18ded8fc9a2fd39e04691608338f069d06f6790129ef8aaf7898e0d02e8096a2"

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"

echo ">>> Configuring passwordless sudo for user: $SSH_USER"
for ip in "${AGENT_IPS[@]}"; do
  ssh $SSH_OPTS "$SSH_USER@$ip" "echo '$SSH_USER ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/$SSH_USER >/dev/null && sudo chmod 440 /etc/sudoers.d/$SSH_USER"
done

echo ">>> Passwordless sudo configured on all agents"

# Loop through each worker and execute setup
i=1
for ip in "${AGENT_IPS[@]}"; do
  echo ">>> Executing setup on $ip"

  UNIQUE_HOSTNAME="k8s-worker-$i"

  ssh $SSH_OPTS "$SSH_USER@$ip" "
    sudo hostnamectl set-hostname $UNIQUE_HOSTNAME &&
    echo '127.0.0.1 $UNIQUE_HOSTNAME' | sudo tee -a /etc/hosts
  "

  ssh $SSH_OPTS "$SSH_USER@$ip" 'sudo bash' < "$SETUP_SCRIPT"

  ssh $SSH_OPTS "$SSH_USER@$ip" "
    sudo kubeadm reset -f &&
    sudo rm -rf /etc/cni/net.d /var/lib/cni/ /etc/kubernetes /var/lib/kubelet/* &&
    sudo systemctl restart kubelet
  "


  ssh $SSH_OPTS "$SSH_USER@$ip" "sudo $JOIN_COMMAND"

  echo ">>> $UNIQUE_HOSTNAME joined successfully"
  ((i++))
done









#!/bin/bash
set -e

# === Configuration ===
AGENT_IPS=(
  "192.168.2.181"
  "192.168.2.7"
  "192.168.2.223"
  "192.168.2.140"
  "192.168.2.18"
  "192.168.2.71"
  "192.168.2.240"
  "192.168.2.194"
)

SSH_USER="k8s-agent"
SETUP_SCRIPT="worker-setup-k8s.sh"
REMOTE_SCRIPT_PATH="/tmp/worker-setup-k8s.sh"

JOIN_COMMAND="kubeadm join 192.168.2.11:6443 --token 1gduob.s35ho0cxawsvne1j \
--discovery-token-ca-cert-hash sha256:18ded8fc9a2fd39e04691608338f069d06f6790129ef8aaf7898e0d02e8096a2"

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"

# === Step 1: Ensure passwordless sudo ===
echo ">>> Setting up passwordless sudo..."
for ip in "${AGENT_IPS[@]}"; do
  ssh $SSH_OPTS "$SSH_USER@$ip" \
    "echo '$SSH_USER ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/$SSH_USER >/dev/null && sudo chmod 440 /etc/sudoers.d/$SSH_USER"
done

# === Step 2: Loop through each agent and configure ===
i=1
for ip in "${AGENT_IPS[@]}"; do
  echo -e "\n>>> [$ip] Starting setup..."

  UNIQUE_HOSTNAME="k8s-worker-$i"

  echo ">>> [$ip] Setting hostname to $UNIQUE_HOSTNAME"
  ssh $SSH_OPTS "$SSH_USER@$ip" "
    sudo hostnamectl set-hostname $UNIQUE_HOSTNAME &&
    echo '127.0.0.1 $UNIQUE_HOSTNAME' | sudo tee -a /etc/hosts
  "

  echo ">>> [$ip] Uploading setup script..."
  scp $SSH_OPTS "$SETUP_SCRIPT" "$SSH_USER@$ip:$REMOTE_SCRIPT_PATH"

  echo ">>> [$ip] Cleaning old cluster data..."
  ssh $SSH_OPTS "$SSH_USER@$ip" "
    sudo kubeadm reset -f &&
    sudo rm -rf /etc/cni/net.d /var/lib/cni/ /etc/kubernetes /var/lib/kubelet/* &&
    sudo systemctl restart kubelet
  "

  echo ">>> [$ip] Running setup script..."
  ssh $SSH_OPTS "$SSH_USER@$ip" "sudo bash $REMOTE_SCRIPT_PATH"

  echo ">>> [$ip] Joining cluster..."
  ssh $SSH_OPTS "$SSH_USER@$ip" "sudo $JOIN_COMMAND"

  echo ">>> [$ip] $UNIQUE_HOSTNAME joined successfully"
  ((i++))
done

echo -e "\n>>> ✅ All worker nodes have been configured and joined."












#!/bin/bash
set -e

# === Configuration ===
AGENT_IPS=(
  "192.168.2.181"
  "192.168.2.7"
  "192.168.2.223"
  "192.168.2.140"
  "192.168.2.18"
  "192.168.2.71"
  "192.168.2.240"
  "192.168.2.194"
)

SSH_USER="k8s-agent"
SETUP_SCRIPT="worker-setup-k8s.sh"
REMOTE_SCRIPT_PATH="/tmp/worker-setup-k8s.sh"

JOIN_COMMAND="kubeadm join 192.168.2.11:6443 --token 1gduob.s35ho0cxawsvne1j \
--discovery-token-ca-cert-hash sha256:18ded8fc9a2fd39e04691608338f069d06f6790129ef8aaf7898e0d02e8096a2"

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"

# === Step 1: Passwordless sudo ===
echo ">>> Setting up passwordless sudo..."
for ip in "${AGENT_IPS[@]}"; do
  ssh $SSH_OPTS "$SSH_USER@$ip" \
    "echo '$SSH_USER ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/$SSH_USER >/dev/null && sudo chmod 440 /etc/sudoers.d/$SSH_USER"
done

# === Step 2: Setup each worker ===
i=1
for ip in "${AGENT_IPS[@]}"; do
  echo -e "\n>>> [$ip] Starting setup..."
  UNIQUE_HOSTNAME="k8s-worker-$i"

  echo ">>> [$ip] Setting hostname to $UNIQUE_HOSTNAME"
  ssh $SSH_OPTS "$SSH_USER@$ip" "
    sudo hostnamectl set-hostname $UNIQUE_HOSTNAME &&
    grep -q '$UNIQUE_HOSTNAME' /etc/hosts || echo '127.0.0.1 $UNIQUE_HOSTNAME' | sudo tee -a /etc/hosts
  "

  echo ">>> [$ip] Uploading setup script..."
  scp $SSH_OPTS "$SETUP_SCRIPT" "$SSH_USER@$ip:$REMOTE_SCRIPT_PATH"

  echo ">>> [$ip] Resetting any previous Kubernetes config..."
  ssh $SSH_OPTS "$SSH_USER@$ip" "
    sudo kubeadm reset -f &&
    sudo systemctl stop kubelet &&
    sudo systemctl stop containerd || true &&
    sudo rm -rf /etc/cni/net.d /var/lib/cni/ /etc/kubernetes /var/lib/kubelet/* /etc/containerd/config.toml &&
    sudo systemctl daemon-reexec &&
    sudo systemctl restart containerd
  "

  echo ">>> [$ip] Running base setup..."
  ssh $SSH_OPTS "$SSH_USER@$ip" "sudo bash $REMOTE_SCRIPT_PATH"

  echo ">>> [$ip] Joining cluster..."
  ssh $SSH_OPTS "$SSH_USER@$ip" "sudo $JOIN_COMMAND"

  echo ">>> [$ip] $UNIQUE_HOSTNAME joined successfully"
  ((i++))
done

echo -e "\n✅ All worker nodes have been configured and joined."
