import docx
import argparse

def parse_tcpdump(docx_file):
    # Open the docx file
    doc = docx.Document(docx_file)
    
    # Initialize a list to store parsed data
    parsed_data = []
    
    # Iterate through paragraphs and extract TCP dump entries
    for para in doc.paragraphs:
        if para.text.strip():
            parsed_data.append(para.text.strip())
    
    return parsed_data

def create_markdown_table(parsed_data, markdown_file):
    # Header for the Markdown table
    header = "| Timestamp       | Source            | Source Port | Destination             | Destination Port | Flags / Info                                  |\n"
    separator = "|-----------------|-------------------|-------------|-------------------------|------------------|-----------------------------------------------|\n"

    # Prepare the table content
    table_content = header + separator
    
    # Split parsed data into meaningful parts for table
    for i in range(0, len(parsed_data), 2):
        if i+1 < len(parsed_data):
            timestamp = parsed_data[i].split(' ')[0]
            src_info = parsed_data[i].split(' ')[1]
            dest_info = parsed_data[i+1].split(' ')[1]
            
            # Extract IP and port information
            src_ip_port = src_info.split(' > ')[0]
            dest_ip_port = dest_info.split(' > ')[0]
            
            # Flags and info section (simplified)
            flags_info = " ".join(parsed_data[i].split(' ')[2:])
            
            table_content += f"| {timestamp} | {src_ip_port} | {src_info.split(' ')[-1]} | {dest_ip_port} | {dest_info.split(' ')[-1]} | {flags_info} |\n"
    
    # Write the table to a markdown file
    with open(markdown_file, 'w') as f:
        f.write(table_content)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Parse TCP dump data from a .docx file and generate a Markdown table.")
    parser.add_argument("input_file", help="The .docx file containing the TCP dump data.")
    parser.add_argument("output_file", help="The output Markdown file to write the formatted table to.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Parse the TCP dump data from the input file
    parsed_data = parse_tcpdump(args.input_file)
    
    # Create the markdown table and save it to the output file
    create_markdown_table(parsed_data, args.output_file)
    
    print(f"Markdown table has been written to {args.output_file}")

if __name__ == "__main__":
    main()
