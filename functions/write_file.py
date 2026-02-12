import os
from google.genai import types


def write_file(working_directory, file_path, content):
    try:
        abs_dir_path = os.path.abspath(working_directory)
        joined_path = os.path.normpath(os.path.join(abs_dir_path, file_path))

        if not os.path.commonpath([abs_dir_path, joined_path]) == abs_dir_path:
            raise ValueError(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

        if os.path.isdir(joined_path):
            raise ValueError(f'Error: Cannot write to "{file_path}" as it is a directory')


        os.makedirs(os.path.dirname(joined_path), exist_ok=True)

        with open(joined_path, 'w') as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return str(e)
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file in the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)