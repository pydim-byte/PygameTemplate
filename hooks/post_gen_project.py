import os
from pathlib import Path

path = Path(os.getcwd())
parent_path = path.parent.absolute()

assets_folders = ['audio',
                  'fonts',
                  'images',
                  'tilemap']

for folder in assets_folders:
    folder_path = os.path.join(
            parent_path, 
            '{{cookiecutter.game_name}}',
            'assets', 
            folder
            )
    os.makedirs(folder_path)

