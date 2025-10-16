for i in {101..110}; do
  qm create $i --name vm-$i --memory 2048 --net0 virtio,bridge=vmbr0 --bootdisk scsi0 --scsihw virtio-scsi-pci
  qm set $i --scsi0 local-lvm:10
  qm set $i --cdrom local:iso/ubuntu-22.04.iso
  qm set $i --boot order=scsi0;ide2
  qm start $i
done
