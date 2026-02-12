import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        return_string = f"Result for '{directory}' directory:\n"      
        dir_path = os.path.abspath(working_directory)
        joined_path = os.path.normpath(os.path.join(dir_path, directory))

        valid_target_dir = os.path.commonpath([dir_path, joined_path]) == dir_path

        if not valid_target_dir:
            raise ValueError(f'{return_string}    Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not os.path.isdir(joined_path):
            raise ValueError(f'{return_string}    Error: "{directory}" is not a directory')
        
        
     
        for file in os.listdir(joined_path):
            file_path = os.path.join(joined_path, file)
            file_size = os.path.getsize(file_path)               
            is_dir = os.path.isdir(file_path)

            return_string += f"- {file}: file_size={file_size} bytes, is_dir={is_dir}\n"
        
        return return_string
    
    except Exception as e:
        return str(e)
    
schema_get_files_info = types.FunctionDeclaration(
            name="get_files_info",
            description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "directory": types.Schema(
                        type=types.Type.STRING,
                        description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
                    ),
                },
            ),
        )