import os
from box.exceptions import BoxValueError
import yaml
from src.cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> dict:
    """Read yaml file and return as dict."""
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Loaded yaml file from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Yaml file {path_to_yaml} is empty.")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_directories: list, verbose=True) -> None:
    """Create directories if they do not exist."""
    for path in path_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory {path}")


@ensure_annotations
def save_json(path: Path, data: Any) -> None:
    """Save json file."""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"Saved json file to {path}")


@ensure_annotations
def load_json(path: Path) -> Any:
    """Load json file."""
    with open(path, "r") as f:
        content = json.load(f)

    logger.info(f"Loaded json file from {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Save binary file."""
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary file."""
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> int:
    """Get size of file in KB."""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, "wb") as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
