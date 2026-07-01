
# Troubleshooting

This document collects problems that were encountered during the development of the Berlin-Box together with their solutions.

It is based on real experience rather than theoretical examples.

---

## The RAK4631 is not detected

### Symptom

The Berlin-Box starts, but no radio interface is available.

### Possible Cause

The USB cable does not provide a data connection or the RAK4631 is connected incorrectly.

### Solution

Verify the USB connection and check whether the RAK4631 appears as a serial device.

---

## The Berlin-Box service does not start

### Symptom

The `berlin-box.service` fails immediately after startup.

### Possible Cause

The Python virtual environment is not activated correctly, the script path is incorrect, or a required package is missing.

### Solution

Check the service configuration and inspect the system log using `journalctl`.

---

## The node is running but no Announce is visible

### Symptom

The service is active, but MeshChat or Sideband cannot see the Berlin-Box.

### Possible Cause

The radio parameters do not match the other nodes or the antenna is missing.

### Solution

Verify frequency, bandwidth, spreading factor, coding rate and TX power on every participating node.

---

## Messages are received but no reply is sent

### Symptom

Incoming LXMF messages arrive, but no response is generated.

### Possible Cause

The LXMF callback is not registered correctly or the application is not processing incoming messages.

### Solution

Verify the Berlin-Box log output and confirm that the callback is active.

---

## Development Notes

Several of these issues were encountered during the development of the Berlin-Box.

For that reason, this document will continue to grow as new experiences are made. Every solved problem can help future builders save time.
