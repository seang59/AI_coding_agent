import os
from google.genai import types


def get_file_content(working_directory, file_path):
    try:
        MAX_READ_SIZE = 10_000  # 10 KB
        abs_dir_path = os.path.abspath(working_directory)
        joined_path = os.path.normpath(os.path.join(abs_dir_path, file_path))

        if not os.path.commonpath([abs_dir_path, joined_path]) == abs_dir_path:
            raise ValueError(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

        if not os.path.isfile(joined_path):
            raise ValueError(f'Error: File not found or is not a regular file: "{file_path}"')
        
        with open(joined_path, 'r') as file:
            content = file.read(MAX_READ_SIZE)

            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_READ_SIZE} characters]'
        
        return content
    
    except Exception as e:
        return str(e)
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the contents of a file in the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)