html_filename = 'index.html' 
with open(html_filename, 'r') as html_file:
    html_content = html_file.read()


python_filename = 'html.txt'  
with open(python_filename, 'w') as py_file:
    py_file.write(f'html_content = """{html_content}"""')

print(f'Successfully converted {html_filename} to {python_filename}')
