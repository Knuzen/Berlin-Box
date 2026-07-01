# Software

## Operating System

The Berlin-Box was developed and tested using **Raspberry Pi OS Legacy (32-bit)**.

A desktop environment is not required. The system is intended to run as a lightweight, autonomous node on a Raspberry Pi Zero.

A clean installation of Raspberry Pi OS Legacy is recommended before starting the installation.

---

## Python Environment

The project runs inside a **Python virtual environment (venv)**.

Using a virtual environment keeps the operating system clean and separates the Berlin-Box software from other Python applications that may be installed on the Raspberry Pi.

---

## Required Python Packages

The following Python packages are required:

* Python 3
* pip
* venv
* RNS (Reticulum Network Stack)
* LXMF

Additional packages may be added in future versions if new functions are implemented.

---

## Reticulum Configuration

The Berlin-Box communicates through a RAK4631 running as an RNode.

The development and testing configuration was:

* Frequency: **869.475 MHz**
* Bandwidth: **125 kHz**
* Spreading Factor: **SF7**
* Coding Rate: **5**
* TX Power: **22 dBm**

These settings should match the configuration of the other Reticulum nodes used for testing.

---

## Berlin-Box Script

The main application is `berlin_box.py`.

Its primary functions are:

* initialize the Reticulum network
* register an LXMF delivery destination
* periodically announce its presence on the network
* receive incoming LXMF messages
* send simple reply messages for communication tests

The script was intentionally kept simple to make it easy to understand, modify and reproduce.

---

## System Services

For unattended operation the Berlin-Box is configured to start automatically during system boot.

The project uses Linux system services so that the node becomes operational without user interaction after power-up.

Depending on the installation, services such as `reticulum.service` and `berlin-box.service` are used.

---

## Notes

The focus of this project is reliability and reproducibility rather than software complexity.

Every function was tested on real hardware using Reticulum-compatible applications such as MeshChat and Sideband.

This document reflects the software environment that was actually used during development and serves as a reference for anyone who wants to rebuild the Berlin-Box.
