# def read_template(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             return file.read().strip()
#     except FileNotFoundError:
#         print(f"Error: file not found at {file_path}")
#         raise
    
# def parse_template(template):
#     language_parts = []
#     stripped_template = ""
#     in_language_part = False
    
#     for char in template:
#         if char == "{":
#             in_language_part = True
#             language_parts.append("")
#         elif char == "}":
#             in_language_part = False
#         else:
#             if in_language_part:
#                 language_parts[-1] += char
#             else:
#                 stripped_template += char
    
#     return stripped_template, language_parts
# def merge(template, language_parts):
#     if len(language_parts) == 0:
#         return template
    
#     merged_template = template.replace("{}", str(language_parts[0]), 1)
#     for language_part in language_parts[1:]:
#         merged_template = merged_template.replace("{}", str(language_part), 1)
    
#     return merged_template

def read_template():
    return 1

def parse_template():
    return 2

def merge():
    return 3