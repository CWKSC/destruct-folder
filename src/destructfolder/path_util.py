from pathlib import Path
from typing import List

def childsWithSuffix(path: Path, suffix: str):
    return [p for p in path.iterdir() if p.suffix == suffix]


def getChildFiles(path: Path) -> List[Path]:
    return [p for p in path.iterdir() if p.is_file()]


def getChildFolders(path: Path) -> List[Path]:
    return [p for p in path.iterdir() if p.is_dir()]
