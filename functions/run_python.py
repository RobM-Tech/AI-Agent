import os, subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_directory = os.path.abspath(working_directory)
    path = os.path.join(working_directory, file_path)
    abs_p = os.path.abspath(path)
    
    if not abs_p.startswith(working_directory):
        return f'STDOUT: \nSTDERR: Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(path):
        return f'STDOUT: \nSTDERR: Error: File "{file_path}" not found.'
    
    if not path.endswith(".py"):
        return f'STDOUT: \nSTDERR: Error: "{file_path}" is not a Python file.'
    
    
    try:
        res = subprocess.run(
            ["python3", file_path] + args,
            capture_output=True,
            text=True,
            cwd=working_directory,
            timeout=30
            )        
    except Exception as e:
        return f"STDOUT: None\nSTDERR: Error: {e}"
    
    so = res.stdout.strip() if res.stdout else ""
    err = res.stderr.strip() if res.stderr else ""

    if not so and not err:
        return "No output produced."
    
    output = f' STDOUT: {so}\nSTDERR: {err}'
    
    if res.returncode != 0:
        output += f'\nProcess exited with code {res.returncode}'
    
    return output

