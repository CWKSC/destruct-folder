from abc import abstractmethod
from pathlib import Path
from copy import deepcopy
from typing import List

import numpy as np
from tqdm import tqdm

from destructfolder.path_util import getChildFiles, getChildFolders
import destructfolder.opencv_util as opencv_util


class IFolder:
    def __init__(
        self,
        name: str = None,
        childs: List["IFolder"] = [],
        key_for_path: str = None,
        key_for_files: str = None,
        key_for_folders: str = None,
    ):
        self.name = name
        self.childs = childs
        self.key_for_path = key_for_path
        self.key_for_files = key_for_files
        self.key_for_folders = key_for_folders


class Folder(IFolder):
    pass


class ForEachFolder(IFolder):
    def __init__(
        self,
        name: str = None,
        subfolder: IFolder = None,
        key_for_path: str = None,
        key_for_files: str = None,
        key_for_folders: str = None,
        key_for_subfolder: str = None,
    ):
        super().__init__(name, [], key_for_path, key_for_files, key_for_folders)
        self.subfolder = subfolder
        self.key_for_subfolder = key_for_subfolder


class IContentFolder(IFolder):
    def __init__(
        self,
        name: str = None,
        childs: List["IFolder"] = [],
        key_for_path: str = None,
        key_for_files: str = None,
        key_for_folders: str = None,
        key_for_contents: str = None,
        show_progress: bool = True,
    ):
        super().__init__(name, childs, key_for_path, key_for_files, key_for_folders)
        self.key_for_content = key_for_contents
        self.show_progress = show_progress

    @abstractmethod
    def getContents(self, paths: List[Path]):
        pass


class NpLoadTxtFolder(IContentFolder):
    def getContents(self, paths: List[Path]):
        result = {}
        if len(paths) > 0:
            if self.show_progress:
                print(f"Loading NpLoadTxtFolder contents ({self.name}) ...")
            for path in tqdm(paths) if self.show_progress else paths:
                result[path.stem] = np.loadtxt(str(path))
            if self.show_progress:
                print()
        return result

class TxtFolder(IContentFolder):
    def getContents(self, paths: List[Path]):
        result = {}
        if len(paths) > 0:
            if self.show_progress:
                print(f"Loading TxtFolder contents ({self.name}) ...")
            for path in tqdm(paths) if self.show_progress else paths:
                f = open(str(path), "r")
                result[path.stem] = f.read()
                f.close()
            if self.show_progress:
                print()
        return result

class JpgFolder(IContentFolder):
    def getContents(self, paths: List[Path]):
        result = {}
        if len(paths) > 0:
            if self.show_progress:
                print(f"Loading JpgFolder contents ({self.name}) ...")
            for path in tqdm(paths) if self.show_progress else paths:
                result[path.stem] = opencv_util.readRGBImage(str(path))
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


def buildFramework(rootPath: Path, folderStructure: List[IFolder]) -> None:
    def dfs(path: Path, folder: IFolder):
        path = path / folder.name
        path.mkdir(exist_ok=True)
        if isinstance(folder, ForEachFolder):
            return
        for child in folder.childs:
            dfs(path, child)

    for folder in folderStructure:
        dfs(rootPath, folder)


def destructFolder(rootPath: Path, folderStructure: List[IFolder]) -> dict:

    resultDict = {}

    def destruct(parent: Path, folder: IFolder):
        current = parent / folder.name
        key_for_path = folder.key_for_path
        key_for_files = folder.key_for_files
        key_for_folders = folder.key_for_folders

        if key_for_path != None:
            resultDict[key_for_path] = current

        if key_for_files != None:
            resultDict[key_for_files] = getChildFiles(current)

        if key_for_folders != None:
            resultDict[key_for_folders] = getChildFolders(current)

        if isinstance(folder, IContentFolder):
            key_for_contents = folder.key_for_content
            if key_for_contents != None:
                resultDict[key_for_contents] = folder.getContents(
                    getChildFiles(current)
                )

        if isinstance(folder, ForEachFolder):
            key_for_subfolder = folder.key_for_subfolder
            subfolder = folder.subfolder

            if key_for_subfolder != None and subfolder != None:
                resultDict[key_for_subfolder] = {}
                childFolders = getChildFolders(current)
                subfolderStructure = []
                for childFolder in childFolders:
                    copy = deepcopy(subfolder)
                    copy.name = childFolder.stem
                    subfolderStructure.append(copy)
                    resultDict[key_for_subfolder][childFolder.stem] = destructFolder(
                        current, [copy]
                    )

            return

        for child in folder.childs:
            destruct(current, child)

    for folder in folderStructure:
        destruct(rootPath, folder)

    return resultDict
