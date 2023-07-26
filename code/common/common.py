import json
import dicom
import os

class DatasetCreator:
    """Returns a dictionary with all dataset resources and respective paths.
    """
    
    def __init__(self, path):
        self.path = path
        self.dataset = {}
        self.generate_dataset()

    def generate_dataset(self):
        for root, directories, files in os.walk(self.path):
            current_node = self.dataset
            folders = root.split(os.path.sep)[1:]
            for folder in folders:
                current_node = current_node.setdefault(folder, {})
            for file in files:
                current_node[file] = os.path.join(root,file)