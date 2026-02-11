# RIGOL DP800 Python Control API

This API contains scripts for validating RIGOL USB connection. To use the repository, first clone it and install the required dependencies:

```
pip install -r requirements.txt
```
---
## Project Goals

- Programmatically control a **DP800 Series Power Supply**
- 
- Charge connected battery via constant current, voltage, and power settings
- Implement voltage and current protection limits
- Control beeping and error limits
- Run on a **Raspberry Pi** over USB

## Hardware Overview

- **Programmable Electronic Power Supply:** RIGOL DP800 Series PS
- **Interface:** USB or RS-232  
- **Controller:** Raspberry Pi / Standard OS

## Software Overview

- **Language:** Python
- **Primary Library:** [`pyvisa`](https://pypi.org/project/PyVISA/)

The `pyvisa` package provides a high-level Python interface for RIGOL SCPI communication, allowing control of:
- Voltage/current commands
- PS Protection limits
- PS enable/disable
- Voltage, current, and power measurements

Using this library avoids implementing low-level SCPI commands from scratch.

---

# Simulated Charging and Programmable Outputs

Pre-test Notes:
DO NOT, in any circumstance, set the RIGOL output to "OFF". If this happens, the Programmable PS will short the positive and negative leads, 
creating a shor circuit on the battery. Constantly monitor PS status when charging batteries and use a diode or current limiter to prevent shorts.

To charge a connected battery pack, connect the positive RIGOL PS lead to the positive terminal on the battery, following with the respective negative leads. 

Please use 'lsusb' on linux to extract the specific RIGOL DP800 USB ID

ID should look like this: 'USB0::6833::3601::DP8D202700178::0::INSTR'

Update ID with 'nano /Examples/example2.py' and execute:

```
sudo python3 -m /Examples/example2.py
```

(USB ID and network communication may need to be enabled via the RIGOL DP800 GUI)

# Chemistry-specific Charge Cycles

Coming soon...

# Verifying Inhibits

Coming soon...

# Verifying Thread Functionality

Coming soon...