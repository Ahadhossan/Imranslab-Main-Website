# Example: Create VM with ID 101
qm create 101 --name ubuntu-vm-1 --memory 2048 --net0 virtio,bridge=vmbr0 --bootdisk scsi0 --scsihw virtio-scsi-pci

# Add disk (10GB on local-lvm)
qm set 101 --scsi0 local-lvm:10

# Attach ISO for installation
qm set 101 --cdrom local:iso/ubuntu-22.04.iso

# Set boot order
qm set 101 --boot order=scsi0;ide2

# Start the VM
qm start 101