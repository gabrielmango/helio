import os

def replace_quotes(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                content = content.replace('"', "'")
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)

if __name__ == '__main__':
    replace_quotes('helio_main')
    replace_quotes('tests')


