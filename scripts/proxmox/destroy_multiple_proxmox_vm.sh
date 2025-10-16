#!/bin/bash

# List of VM IDs to delete
VM_IDS=(397 398 399)

for VMID in "${VM_IDS[@]}"; do
  echo "Stopping VM $VMID..."
  qm stop "$VMID"

  echo "Destroying VM $VMID..."
  qm destroy "$VMID" --purge

  echo "VM $VMID deleted."
  echo "--------------------------"
done