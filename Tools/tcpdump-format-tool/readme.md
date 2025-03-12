# TCP Dump Formatter

A Python tool to parse TCP dump data from a `.docx` file and generate a formatted table in a Markdown file. This tool is designed to make it easy to convert raw TCP dump logs into an organized, readable Markdown table.

## Features

- Reads TCP dump data from a `.docx` file.
- Parses the data into key fields (timestamp, source IP, source port, destination IP, destination port, flags/info).
- Outputs the parsed data into a well-formatted Markdown table.
- Simple and easy-to-use command-line interface.

## Requirements

- Python 3.x
- `python-docx` library to read `.docx` files.

## Usage

You can run the script from the command line, passing the `.docx` file as input and specifying the desired output Markdown file.

### Command Syntax

```bash
python tcpdump-formatter.py <input_file> <output_file>
```

- `<input_file>`: Path to the `.docx` file containing the TCP dump data.
- `<output_file>`: Path where the formatted Markdown table will be saved.

### Example

To format a TCP dump log from a file `tcpdump-traffic-log.docx` and save the formatted table into `tcpdump.md`, run the following command:

```bash
python tcpdump-formatter.py tcpdump-traffic-log.docx tcpdump.md
```

This will parse the content of `tcpdump-traffic-log.docx` and generate a Markdown table in `tcpdump.md`.

## Example Output

The script will create a Markdown file with a table like the following:

| Timestamp       | Source            | Source Port | Destination             | Destination Port | Flags / Info                                  |
|-----------------|-------------------|-------------|-------------------------|------------------|-----------------------------------------------|
| 14:18:32.192571 | your.machine       | 52444       | dns.google.domain       | 53               | A? yummyrecipesforme.com. (24)                |
| 14:18:32.204388 | dns.google.domain | 53          | your.machine            | 52444            | A 203.0.113.22 (40)                           |
| 14:18:36.786501 | your.machine       | 36086       | yummyrecipesforme.com   | 80               | Flags [S], seq 2873951608, win 65495         |
| 14:18:36.786517 | yummyrecipesforme  | 80          | your.machine            | 36086            | Flags [S.], seq 3984334959, ack 2873951609   |
