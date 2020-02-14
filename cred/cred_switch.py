import os

from typing import List
from pathlib import Path

import click


@click.command()
def change_type():
    """Change default credentials for a given type."""
    home_path = str(Path.home())
    cred_folder = '.aws'
    aws_folders = get_aws_folders()
    cts = get_input(aws_folders)
    read_dir = home_path + "/" + cred_folder + '/' + cts
    write_dir = home_path + "/" + cred_folder
    dir_list = os.listdir(read_dir)
    for file in dir_list:
        data_contents = None
        try:
            with open(f"{read_dir}/{file}") as fh, open(f"{write_dir}/{file}", "w") as fr:
                data_contents = fh.readlines()
                fr.writelines(data_contents)

        except IsADirectoryError as e:
            print(f"Directory error - {e}")
            return
    print("Credentials updated successfully.")

def get_aws_folders()-> List[str]:
    aws_dirs = []
    home_path = str(Path.home())
    cred_folder = '.aws'
    read_dir = home_path + "/" + cred_folder
    children= [os.path.join(read_dir, child) for child in os.listdir(read_dir)]
    dirs = filter(os.path.isdir, children)
    for dir in dirs:
        aws_dirs.append(dir.split('/')[-1:][0])
    return aws_dirs

def get_input(aws_folders) -> str:
    while True:
        selection = input(f"Select a valid directory {aws_folders}")
        if validate_selection(selection, aws_folders):
            return selection
        else:
            print("Error - not a valid directory")

def validate_selection(cts, aws_folders) -> bool:
    return cts in aws_folders



if __name__ == '__main__':
    change_type()
