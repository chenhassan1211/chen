import os

# Define the directory and file name
directory = '/cnvrg'
file_name = 'my_file.txt'

# Create and write to the file
file_path = os.path.join(directory, file_name)
try:
    with open(file_path, 'w') as f:
        f.write('hey')
    print(f"File created at {file_path}")
except PermissionError:
    print(f"Permission Denied: Cannot write to {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
