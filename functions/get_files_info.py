import os

def get_files_info(working_directory, directory="."):
    working_directory = os.path.abspath(working_directory)
    path = os.path.join(working_directory, directory)
    abs_p = os.path.abspath(path)
    

    if not abs_p.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'
    
    file_info = []
    try:
        for i in sorted(os.listdir(path)):
            f_path = os.path.join(path, i)
            size = os.path.getsize(f_path)
            isdir = os.path.isdir(f_path)
            info = f"- {i}: file_size={size} bytes, is_dir={isdir}"
            file_info.append(info)
    except Exception as e:
        return f"Error: {e}"
    
    res = "\n".join(file_info)
    return res
    