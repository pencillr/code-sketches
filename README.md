# Code Sketches
A collection of boilerplates, random sketches, and useful stuff.

## Bash
Some bash tools to use and learn. For debugging commands use [explainshell](https://explainshell.com/#).

### Generate random alphanumeric string
```bash
# 16 character alphanumeric string
identifier=$(< /dev/urandom tr -dc 'a-zA-Z0-9' | fold -w 16 | head -n 1)
```

### Bash tempdir
```bash
function cleanup() {
    echo >&2 "CLEANING UP TEMPORARY DIRECTORY ${TEMP_DIR}"
    rm -rf "${TEMP_DIR}"
}

function create_temporary_directory_with_cleanup() {
    TEMP_DIR=$(mktemp --directory "/tmp/temporary_dir".XXXXXXXX)
    export TEMP_DIR
    trap cleanup EXIT
    echo "TEMPORARY WORKING DIRECTORY CREATED AT ${TEMP_DIR}"
}
```

### Multiline conditional
```bash
if [[ -n "${_condition:-}" ]] && \
   [[ "${_condition:-}" != *"aaa"* ]] && \
   [[ "${_condition:-}" != *"bbb"* ]]; then
    echo "Checked!"
fi
```

### Read to list from string
```bash
# cut at spaces
IFS=" " read -r -a version_list <<< "${VERSION_LIST}"
```

### Iterate on list
```bash
for version in "${version_list[@]}"; do
    EXEC_STRING+=" --version ${version}"
done
```

---

## Python

### Python Virtualenv steps
- python3 -m venv ./bin-python
- bash source ./bin-python/bin/activate
- pip install -r your_requirements.txt"
- pip freeze -l > your_requirements.txt"

### Some String interpolation options in python
```python
logger.warning("Bad expression: %s. No matches found at %s", expression, location)
parameter = "Stuff_and_{version}".format(version=version)
# f-strings in python 3.6
name = "Peter"
age = 21
f"Hello, {name}. You are {age}."
```

### Read file to string
```python
def read_testfile(test_file):
    with test_file.open() as infile:
        test_data = infile.read().splitlines() # json.load(infile)
    return test_data
```

### Basic script boilerplate
```python
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Default.')
    parser.add_argument('--param', help='an integer for the accumulator')
    return parser.parse_args()


def main():
    args = parse_arguments()
    return args


if __name__ == '__main__':
    main()
```