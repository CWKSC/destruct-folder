from typing import List
from destructfolder import IContentFolder
from abc import abstractmethod
from pathlib import Path
from copy import deepcopy
from typing import List

from tqdm import tqdm
import numpy as np

class NpLoadTxtFolder(IContentFolder):
    def getContents(self, paths: list[Path]):
        result = {}
        if len(paths) > 0:
            if self.show_progress:
                print(f"Loading NpLoadTxtFolder contents ({self.name}) ...")
            for path in tqdm(paths) if self.show_progress else paths:
                result[path.stem] = np.loadtxt(str(path))
            if self.show_progress:
                print()
        return result

class NpyFolder(IContentFolder):
    def getContents(self, paths: List[Path]):
        result = {}
        if len(paths) > 0:
            if self.show_progress:
                print(f"Loading NpyFolder contents ({self.name}) ...")
            for path in tqdm(paths) if self.show_progress else paths:
                result[path.stem] = np.load(str(path))
            if self.show_progress:
                print()
        return result