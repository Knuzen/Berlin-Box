# Installation

This document describes the software installation used during the development of the Berlin-Box.

The installation is intentionally divided into small steps so that every stage can be verified before continuing.

---

## Create Python Virtual Environment

The Berlin-Box runs inside a dedicated Python virtual environment (venv).

Using a virtual environment keeps the operating system clean and allows all required Python packages to be installed independently from the system installation.

---

## Install Reticulum

Install the Reticulum Network Stack (RNS).

Reticulum provides the networking layer that allows the Berlin-Box to communicate with other compatible nodes over LoRa using an RNode.

After installation, verify that Reticulum starts correctly before continuing.

---

## Install LXMF

Install the LXMF package.

LXMF is the messaging layer used by the Berlin-Box to receive and send messages across the Reticulum network.

After installation, verify that the package is available inside the virtual environment.

---

## Copy berlin_box.py

Copy the `berlin_box.py` script to the Raspberry Pi.

This script contains the application logic of the Berlin-Box and is the only project-specific software required to operate the node.

---

## Create systemd Service

Create a Linux `systemd` service for the Berlin-Box.

Using a service allows the software to run automatically in the background and makes administration easier.

---

## Enable Automatic Startup

Enable the service so that the Berlin-Box starts automatically whenever the Raspberry Pi boots.

This allows the node to operate unattended after a power failure or restart.

---

## Test the Installation

Before closing the installation, verify that:

* the RAK4631 is detected correctly
* Reticulum starts without errors
* the Berlin-Box service is running
* the node announces itself on the network
* LXMF messages can be received
* reply messages are sent successfully

Successful communication with MeshChat or Sideband confirms that the installation is complete.

---

## Notes

This installation reflects the environment used during the development of the Berlin-Box.

Individual Raspberry Pi models, operating system versions or future releases of Reticulum and LXMF may require minor adjustments.
