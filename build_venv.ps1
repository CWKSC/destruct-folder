python -m venv venv
.\venv\Scripts\activate

python -m pip install --upgrade pip

# pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
# pip install numpy
# pip install opencv-contrib-python

pip install tqdm
pip install black
pip install pytest
pip install build twine

pip install -e .

python -m build

pause
deactivate
