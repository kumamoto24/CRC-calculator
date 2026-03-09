# CRC Calculator🧮

## Background
CRC, or Cyclic Redundancy Check, is a widely used method for detecting errors in digital data transmission or storage.  
It works by treating the data as a binary number, dividing it by a predefined generator polynomial, and producing a remainder called the CRC checksum. This checksum can be used to verify whether the data has been transmitted or stored correctly.  

The purpose of this project is to provide a simple CRC calculator to verify manually calculated CRC results.  
This calculator is also designed to facilitate learning and understanding for the **UWA CITS3002** unit.  
It includes a core calculation module (`CRC_calculator.py`) and a graphical user interface (`crc_gui.py`) for easier input and visualization.

## Project Structure
- `CRC_calculator.py` : Core CRC calculation function  
- `crc_gui.py` : GUI calling `crc_calculator.py`  
- `README.md` : Project description  
- `LICENSE` : License information

## Usage
1. Make sure Python (>=3.7) is installed  
2. Run the GUI from the command line:

```bash
python crc_gui.py
```
3. In the GUI panel:  
   - Enter binary data (e.g., `1101011`)  
   - Enter generator polynomial (e.g., `1011`)  
   - Click **Compute CRC** → The CRC remainder will be displayed

## Feedback & Contribution
Feedback, suggestions, or improvements are welcome via GitHub issues or pull requests.
