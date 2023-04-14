import re

def read_template(file_path):
     with open (file_path , 'r') as file:
        content = file.read()
        return content
     
def parse_template(template_txt):
    stripped = re.sub("[^{]+(?=})","",template_txt)
    words = tuple(re.findall("[^{]+(?=})",template_txt ))
    return stripped , words 
print("Welcome to the Madlib game")
print("Now you will start the game you should answer the questions")
def user_input(words):
    

    input_value=[]
    for i in list(words):
        input_value.append(input(f" Write  {i} : "))
    return tuple(input_value)

def merge(template, words):
    return template.format(*words)

# def madlib_cli(path):
#     content=read_template(path)
#     stripped ,words = parse_template(content)
#     input_value = user_input(words)
#     res=merge(stripped,input_value)
#     print(res)


 
# write_to_file
def madlib_cli(path):
    content=read_template(path)
    stripped ,words = parse_template(content)
    input_value = user_input(words)
    res=merge(stripped,input_value)
    print(res)
    
    with open("assets/output.txt", "w") as file:
        file.write(res)

madlib_cli("assets/full-text.txt")
# print("Now with the short cut")
# madlib_cli("assets/dark_and_stormy_night_template.txt", "assets/dark_and_stormy_night_result.txt")
