qm importdisk 2000 ubuntu-cloudinit.qcow2 local-lvm

qm set 1000 --serial0 socket --vga serial0

### inside the vm to ... #####
sudo apt install qemu-guest-agent -y

cloud image link
https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img

### start multiple vms together ###

for vmid in 400 401 402 403 404; do qm stop $vmid; done
for vmid in 400 401 402 403 404; do qm start $vmid; done

for vmid in 402 403 404; do qm start $vmid; done

for vmid in 405 406 407; do qm start $vmid; done

vzdump 122 --fleecing 0 --storage Local_Dir_For_VMs_Backup --node pokemon --compress zstd --all 0 --mode snapshot

vzdump 122 --fleecing 0 --storage Local_Dir_For_VMs_Backup --compress zstd --node pokemon --mode snapshot --all 0