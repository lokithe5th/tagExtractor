# Audit Search Script

`tagExtractor`, allows you to search through files of specific extensions for lines containing certain tags. The file extensions and tags are specified in a `settings.json` file.

## Prerequisites

- Python 3.x installed on your system. You can download Python [here](https://www.python.org/downloads/).

## Installation

1. Clone this repository: `git clone https://github.com/lokithe5th/tagExtractor`

2. (Optional) It's recommended to create a virtual environment:
```
python -m venv venv
source venv/bin/activate # On Windows use: .\venv\Scripts\activate
```

## Usage  

To run in current directory:  
```
python tagExtractor.py
```

To run in a target directory:  
```
python tagExtractor.py -p /path/to/specific/directory
```

The results will be in the same directory from where the scripts are run in a `audit.md` file.

## Configuration

The `settings.json` file contains the configuration for target file extensions and tags. Here's a sample configuration:

```
{
 "targetExtensions": [".sol"],
 "targetTags": ["@audit"]
}
```