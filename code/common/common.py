import os
import json

class DatasetCreator:
    """Returns a dictionary with all dataset resources and respective paths.
    """

    def __init__(self, path, archivepath = None):
        self.path = path
        if archivepath is None:
            self.archive_path = self.path
        else:
            self.archive_path = archivepath
        self.dataset = {}
        self.generate_dataset()
        self.archive()

    def generate_dataset(self):
        for root, directories, files in os.walk(self.path):
            current_node = self.dataset
            folders = root.split(os.path.sep)[1:]
            for folder in folders:
                current_node = current_node.setdefault(folder, {})
            for file in files:
                current_node[file] = os.path.join(root,file)

    def archive(self):
        with open(self.archive_path+'dataset_structure.json','x') as fp:
            json.dump(self.dataset,fp)

if __name__ == '__main__':
    pass