# Dependencies
Install
 - Python
 ## Download the models MobileNet-SSD

  -  [deploy.prototxt](https://github.com/chuanqi305/MobileNet-SSD/blob/master/deploy.prototxt)
  - [mobilenet_iter_73000.caffemodel](https://github.com/chuanqi305/MobileNet-SSD/blob/master/mobilenet_iter_73000.caffemodel)


# Create virtual environment

create a python virtual environment with the name of "science2024"

```bash
python -m venv <virtual_env_name>
```

## Activate the virtual environment

in order to activate it execute the following command, under the path of where the environment was created

```bash
<virtual_env_name>\Scripts\activate.bat
```

# Initialize project 

create a a new file with the name requirements.txt

```txt
opencv-python-headless
pytesseract
flask
numpy
Pillow
```

in order to execute the requierements execute the following command

```bash
pip install -r requirements.txt
```

