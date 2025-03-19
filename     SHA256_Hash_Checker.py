import os
import hashlib

# Function to compute the SHA256 hash of a file
def compute_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read the file in chunks to handle large files
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Function to check if the file is executable based on file extension
def is_executable(file_name):
    # For macOS and Linux, check for common executable extensions
    executable_extensions = ['.app', '.bin', '.sh', '.out', '.command']
    # For Windows, check for common executable extensions
    if os.name == 'nt':
        executable_extensions += ['.exe', '.bat', '.msi']
    # Return True if the file has one of the executable extensions
    return any(file_name.endswith(ext) for ext in executable_extensions)

# Get the current directory
current_dir = os.getcwd()

# Open the results file for writing
with open("results.txt", "w") as results_file:
    # Loop through all files in the directory
    for filename in os.listdir(current_dir):
        file_path = os.path.join(current_dir, filename)
        # Check if it's a file and if it's executable
        if os.path.isfile(file_path) and is_executable(filename):
            sha256_hash = compute_sha256(file_path)
            # Write the result to the text file
            results_file.write(f"{filename}: {sha256_hash}\n")

print("SHA256 hashes have been written to 'results.txt'.")
