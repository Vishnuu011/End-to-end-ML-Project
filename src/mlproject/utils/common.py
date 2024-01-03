import os
from box.exceptions import BoxValueError
import yaml
from mlproject import log
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    #Read yamls file
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            log.info(f"yaml file : {path_to_yaml} loaded succes")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def Create_Directories(path_to_directories: list, verbose=True):
    #create list of directories
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            log.info(f"Create directories : {path}")

@ensure_annotations
def save_json(path:Path, data:dict):
    #save json file 
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    log.info(f"json file saved at : {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    #load json file
    with open(path) as f:
        content= json.load(f)
    log.info(f"json file loaded succesfully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data : Any, path: Path):
    #save binary file 
    joblib.dump(value=data, filename= path)
    log.info(f"binary file saved at : {path}")

@ensure_annotations
def load_bin(path : Path):
    #load binary data
    data= joblib.load(path)
    log.info(f"binary file loaded from : {path}")
    return data

@ensure_annotations
def get_size(path : Path):
    #get size in kB
    size_in_kb =round(os.getsize(path) / 1024) 
    return f"~{size_in_kb} KB"       
