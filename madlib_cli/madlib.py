
print('''Welcome to Madlibs! ''')

input_str = input("Do you want to play Madlibs? (y/n): ")

if input_str == 'y':
    adj1 = input("write an adjective: ")
    adj2 = input("write another adjective: ")
    name = input("write your name: ")
    file_path =("assets/dark_and_stormy_night_template.txt")
    def read_template(file_path):
        with open (file_path , 'r') as file:
            content = file.read()
            return content

    def parse_template(template_txt):
        parts = []
        stripped = ""
        index = 0

        while index < len(template_txt):
            if template_txt[index] == "{":
                end_index = template_txt.find("}", index)
                parts.append(template_txt[index + 1 : end_index])
                stripped += "{}"
                index = end_index + 1
            else:
                stripped += template_txt[index]
                index += 1

        return stripped, tuple(parts)

    def merge(template, words):
        return template.format(*words)

    template_txt = read_template(file_path)
    stripped, parts = parse_template(template_txt)
    words = (adj1, adj2, name)

    story = merge(stripped, words)

    print(story)
    print('Game is finish!')

elif input_str == 'n':
    print("see you again!")
else:
    print(" please y/n")

    
