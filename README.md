<h1 align="center"><img style="width: 30px; margin-right: 1em" src="/readme_assets/logo.png"></img> TinSpire</h1>

A collection of custom Python/TI-Basic libraries for the TI-Nspire CX II Family made for recreational computing and mathematics
## 🗒️ Note
These libraries have only been tested on a factory TI-Nspire CX II CAS with the latest firmware.
All other firmware and hardware has not been proven to work, but most likely will.
<h2><img style="width: 30px; margin-right: 1em" src="./readme_assets/python.png"> Python Libraries</h2>

### CustomMath
An extended math library designed to replace certain functions and data structures from `numpy` and other commonly used math libraries.
**Current Submodules**
- Matrix - Barebones matrix math implementation
### threedee
A collection of libraries for 3D rendering.
**Current Submodules**
- Camera - Camera class used in `threedee.Point3D` for projection
- Point3D - A class for creating, representing, and manipulating 3D points
<h2><img style="width: 30px; margin-right: 1em" src="./readme_assets/ti.png"> TI-BASIC</h2>

No TI-Basic programs are currently being developed for TinSpire, but keep an eye out!
## Installation
1) Copy the contents of the `tns` directory to your calculator (please refer to [Transfering Files](#transfering-files) for help).
2) To install each module, navigate to each document and:
    1) Navigate to the python file with the same name as the module
    
    <div align="center"><img style="width: 90%; margin: 10px" src="./readme_assets/screenshots/03-12-2025 Image002.jpg"></div>
    
    2) Press the "menu" key and go to `Actions` > `Install as Python module` and hit "enter".
    
    <div align="center"><img style="width: 90%; margin: 10px" src="./readme_assets/screenshots/03-12-2025 Image003.jpg"></div>
    
    3) Confirm replacing the document; this is OK
    
    <div align="center"><img style="width: 90%; margin: 10px" src="./readme_assets/screenshots/03-12-2025 Image004.jpg"><img style="width: 90%; margin: 10px" src="./readme_assets/screenshots/03-12-2025 Image005.jpg"></div>

3) To confiirm the modules have been installed succesfully, TinSpire's modules should show up in the `More Modules` sub-menu when editing a Python file.
## Transfering Files
To transfer the `.tns` document files to your calculator, use one of the following software:
- [Ti-Nspire^TM^ CX II Connect](https://nspireconnect.ti.com/)