import json

# Function to infer field types based on field names
def infer_field_type(field_name):
    if "Handle" in field_name:
        return "ModelConfigHandle_t"
    elif "Name" in field_name or "Names" in field_name:
        return "string_t"
    elif "Entities" in field_name:
        return "CHandle<C_BaseModelEntity>"
    else:
        return "unknown_t"

# Function to convert JSON data to Python class definitions
def convert_to_python_class(data):
    result = []
    for dll, dll_data in data.items():
        for class_name, class_data in dll_data['classes'].items():
            result.append(f"class {class_name}:")
            fields = class_data['fields']
            for field_name, offset in sorted(fields.items(), key=lambda x: x[1]):
                field_type = infer_field_type(field_name)
                result.append(f"    {field_name} = 0x{offset:X}  # {field_type}")
            result.append("    pass\n")
    return "\n".join(result)

# Load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Write the output to a file
def write_to_file(output, file_path):
    with open(file_path, 'w') as f:
        f.write(output)

# Main function to execute the conversion
def main(input_file,output_file):
    data = load_json(input_file)
    output = convert_to_python_class(data)
    write_to_file(output, output_file)
    print(f"Output written to {output_file}")



def convert_json_to_python1(json_file, filename):
    with open(json_file, 'r') as f:
        data = json.load(f)

    output = ""

    for dll_name, dll_data in data.items():
        # Replace periods with underscores in the class name
        class_name = dll_name.replace('.', '_')
        output += f"class {class_name}:\n"
        for variable_name, offset in dll_data.items():
            output += f"    {variable_name} = 0x{offset:X}\n"
        output += "\n"
    
    with open(filename + ".py", "w") as f:
        f.write(output)

if __name__ == "__main__":
    client_input = 'client_dll.json'  # Specify your input JSON file here
    client_output = 'client.py'  # Specify your output Python file here
    main(client_input,client_output)
    convert_json_to_python1("offsets.json","offsets")
