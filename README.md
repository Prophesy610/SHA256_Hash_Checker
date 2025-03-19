# SHA256 File Checker for Executables

This Python script is designed to help you verify the integrity of Windows executables (or other files) by checking their SHA256 hash and cross-referencing it with VirusTotal to see if they are flagged as malware. You can also perform an internet search to gather additional information about the file using the SHA256 hash.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Steps to Analyze Executables](#steps-to-analyze-executables)
- [VirusTotal Integration](#virustotal-integration)
- [Additional Search Functionality](#additional-search-functionality)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In cybersecurity, one of the most effective ways to check for potentially harmful files is to examine their hash values. This script calculates the SHA256 hash of an executable file, which is a unique representation of the file’s contents. By checking the file’s hash against VirusTotal, you can quickly see if it has been flagged as malicious by multiple antivirus engines. Additionally, the script allows you to perform an internet search with the SHA256 hash to gather more information about the file.

You can acquire the executable you want to analyze from network traffic captured via Wireshark or other tools. Once you have the file, you can use this script to assess its safety.

## Requirements

Before using this script, you need:

- Python 3.x
- `requests` library (for interacting with VirusTotal API)
- A VirusTotal API key (free or premium version)
- An internet connection (for searches and VirusTotal checks)

You can install the required dependencies using:

```bash
pip install requests
```

## Usage

1. **Get the Executable**:  
   You can acquire executables from network traffic analysis tools like Wireshark. Once the executable file is obtained, move it to your working directory or provide the full path in the script.

2. **Run the Script**:  
   Execute the script by running the following command:

   ```bash
   python sha256_checker.py path_to_executable
   ```
## Analyze the Results

The script will:
- Calculate the SHA256 hash of the file.
- Check the hash against VirusTotal for detection status.
- Optionally perform an internet search using the SHA256 hash to find additional resources or reports about the file.

## Steps to Analyze Executables

### Step 1: Acquire the Executable

For this script to work, you'll need an executable file. You can acquire this file via network traffic analysis (e.g., Wireshark). Once you have the file, simply point the script to the file path.

### Step 2: Check SHA256

The script calculates the SHA256 hash of the given file, which is a unique identifier for that file's contents. This ensures that the file's integrity is maintained and can be used to look up more details.

### Step 3: VirusTotal Scan

The script will query VirusTotal's API using the calculated SHA256 hash. VirusTotal provides detection status across a wide range of antivirus engines. If the file is flagged as malicious, you'll see detailed information about the detections.

### Step 4: Search Online

If additional information is needed, the script can perform an internet search using the SHA256 hash. This will help you find other resources, analysis, or reports on the file from various security forums, blogs, or research sites.

## VirusTotal Integration

To use VirusTotal with this script, you’ll need to register for an API key:

1. Sign up at [VirusTotal](https://www.virustotal.com).
2. Obtain your free or premium API key.
3. Add your API key in the script where indicated.

The script will query VirusTotal for the given SHA256 hash and retrieve detection information from their database. The result will show whether the file is detected by various antivirus engines.

## Additional Search Functionality

In addition to VirusTotal, the script can perform a simple internet search of the SHA256 hash. This will help you gather other relevant information, such as discussions or other reports that may indicate the file’s reputation in the security community.

## Example

Here’s an example of how to use the script:

```bash
python sha256_checker.py my_file.exe
```

## Sample Output

SHA256 Hash: 5d41402abc4b2a76b9719d911017c592
VirusTotal Results:
    - Detected by 4/60 engines
    - Detection details: Trojan.Generic, Malware, etc.

Additional Information:
    - Found a blog post: "Suspicious file detected in traffic dump"
    - Identified as "potentially unwanted software" in online reports.

## Contributing

We welcome contributions! If you have any suggestions or improvements, feel free to fork the repository, create an issue, or submit a pull request.

## License

This script is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Stay safe, and always verify files before executing them!
