import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_dir_path = os.path.abspath(working_directory)
        joined_path = os.path.normpath(os.path.join(abs_dir_path, file_path))

        if not os.path.commonpath([abs_dir_path, joined_path]) == abs_dir_path:
            raise ValueError(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

        if not os.path.isfile(joined_path):
            raise ValueError(f'Error: "{file_path}" does not exist or is not a regular file')
    
        if not file_path.endswith('.py'):
            raise ValueError(f'Error: "{file_path}" is not a Python file')

        # Build the command to run the Python file
        command = ["python", joined_path]
        if args:
            command.extend(args)
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        if not result.stdout and not result.stderr:
            return "No output produced."
        
        return_string = f"STDOUT: {result.stdout}, STDERR: {result.stderr}"
        return return_string

    except Exception as e:
        return f"Error: executing Python file: {str(e)}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the working directory and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of arguments to pass to the Python script",
            ),
        },
        required=["file_path"],
    ),
)