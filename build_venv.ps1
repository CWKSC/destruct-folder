python -m venv venv
.\venv\Scripts\activate

python -m pip install --upgrade pip

pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
pip3 install numpy
pip3 install opencv-contrib-python
pip3 install tqdm

pip3 install black
pip3 install pytest
pip3 install build twine

pip3 install -e .

python -m build

pause
deactivate
