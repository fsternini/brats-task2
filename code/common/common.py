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

class Dataset:
    """Object representing the dataset"""
    
    def __init__(self, json_file):
        self.json_file = json_file
        try:
            with open(self.json_file, 'r') as self.json_file:
                self.dataset = json.load(self.json_file)
        except FileNotFoundError:
            print(f"The file '{self.json_file}' was not found.")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_files_in_node(self, node_name):
        files = []
        node = self.dataset
        def traverse(self):
            if isinstance(node, dict):
                for key, value in node.items():
                    if key == node_name:
                        if isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if isinstance(sub_value, str):
                                    files.append(sub_value)
                                else:
                                    traverse(sub_value)
                    else:
                        traverse(value)
            elif isinstance(node, list):
                for item in node:
                    traverse(item)

if __name__ == '__main__':
    pass