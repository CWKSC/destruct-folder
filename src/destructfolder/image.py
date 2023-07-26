from __future__ import annotations
from abc import abstractmethod
from pathlib import Path
from copy import deepcopy
from tqdm import tqdm

from destructfolder import IContentFolder
import opencv_util

class JpgFolder(IContentFolder):
    def getContents(self, paths: list[Path]):
        result = {}
        if len(paths) > 0:
            if self.show_progress:
                print(f"Loading JpgFolder contents ({self.name}) ...")
            for path in tqdm(paths) if self.show_progress else paths:
                result[path.stem] = opencv_util.readRGBImage(str(path))
            if self.show_progress:
                print()
        return result
