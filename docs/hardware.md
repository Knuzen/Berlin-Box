
# Hardware

## Overview

The Berlin-Box is built from inexpensive and widely available components. The goal was to create a compact, low-power Reticulum/LXMF node that can operate unattended for long periods while remaining easy to reproduce.

---

## Raspberry Pi Zero

The Raspberry Pi Zero is used as the main computer running Raspberry Pi OS, Reticulum and the Berlin-Box software.

Although its computing power is modest, it is fully sufficient for operating a small autonomous Reticulum node.

---

## Waveshare UPS HAT (C)

A Waveshare UPS HAT (C) is mounted on the Raspberry Pi Zero.

Besides providing battery backup, an important practical advantage became apparent during development:

The Raspberry Pi can still be programmed through the **micro-USB port of the Waveshare UPS HAT**, even while the RAK4631 occupies the Raspberry Pi's own USB data connection.

This makes software development and maintenance much easier and avoids repeatedly disconnecting the radio hardware.

---

## RAK4631 RNode

The radio interface is a RAK4631 configured as an RNode.

It provides the LoRa connection to the Reticulum network and is connected to the Raspberry Pi via USB.

The development system was configured for the European 869.475 MHz band using standard Reticulum parameters.

---

## USB Connection

A suitable USB connection between the Raspberry Pi Zero and the RAK4631 is required.

Depending on the hardware used, a dedicated USB adapter cable may be necessary.

Before powering the system for the first time, verify that both power and USB data connections are correct.

---

## Antenna

Always connect a suitable antenna to the RAK4631 before transmitting.

Operating LoRa hardware without an antenna is not recommended.

---

## Power Supply

During development the Berlin-Box was powered either through the Waveshare UPS HAT or from a USB power source connected to the HAT.

This allows normal software maintenance while keeping the complete hardware assembly connected.

---

## Mechanical Assembly

No special enclosure was required during development.

The prototype was intentionally kept simple to allow easy access for testing, measuring and modifying the hardware.

Future builders are encouraged to adapt the mechanical design to their own requirements.

---

## Notes

The hardware described here reflects the configuration that was successfully tested during development.

Other compatible Raspberry Pi models or Reticulum-compatible RNodes may also work, but they have not been the primary focus of this project.

The screenshots included in this repository document the successful operation of this hardware configuration with MeshChat and Sideband.
