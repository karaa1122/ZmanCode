from parser import translate_kurdish_to_python

import os

def execute_kurdish_code(kurdish_code):
    python_code = translate_kurdish_to_python(kurdish_code)
    print("Generated Python Code:\n", python_code)
    try:
        exec(python_code)
    except Exception as e:
        raise e

def run_kurdish_script(script_path):
    if not os.path.exists(script_path):
        print(f"Script file {script_path} does not exist.")
        return

    with open(script_path, 'r', encoding='utf-8') as file:
        kurdish_code = file.read()

    execute_kurdish_code(kurdish_code)

if __name__ == "__main__":
    run_kurdish_script('main.ku')