import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    path = os.path.join(working_directory, file_path)
    abs_p = os.path.abspath(path)

    if not abs_p.startswith(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    
    try:
        with open(path, "r") as f:
            content = f.read()

            if len(content) > MAX_CHARS:
                return content[:MAX_CHARS] + f'...File {file_path} truncated at 10000 characters'
            else:
                return content

    except Exception as e:
        return f"Error: {e}"    
            

        