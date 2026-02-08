import sass
import os

sass_path = 'tale-pelican-theme/scss/main.scss'
output_path = 'tale-pelican-theme/static/css/main.css'

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

try:
    compiled_css = sass.compile(filename=sass_path, output_style='compressed')
    with open(output_path, 'w') as f:
        f.write(compiled_css)
    print(f"Successfully compiled {sass_path} to {output_path}")
except sass.CompileError as e:
    print(f"SASS compilation failed: {e}")
except FileNotFoundError:
    print(f"Error: Could not find SASS file at {sass_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
