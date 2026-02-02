import os

# Function to create root directory 'apps/' and subdirectory 'templates/'
def initialize_directories():
    # Create root directory 'apps/'
    os.makedirs('apps/templates', exist_ok=True)
    print('Created root directories: apps/ and apps/templates/')

# Function to create base templates

def create_templates():
    templates = {
        'base_tool.html': '<!-- Base Tool Template -->\n<html>\n<head>\n<title>Base Tool</title>\n</head>\n<body>\n<h1>Base Tool</h1>\n</body>\n</html>',
        'base_blog.html': '<!-- Base Blog Template -->\n<html>\n<head>\n<title>Base Blog</title>\n</head>\n<body>\n<h1>Base Blog</h1>\n</body>\n</html>'
    }
    for template_name, content in templates.items():
        with open(f'apps/templates/{{template_name}}', 'w') as f:
            f.write(content)
            print(f'Created template: {template_name}')

# Main function to initialize the setup

def main():
    initialize_directories()
    create_templates()

if __name__ == "__main__":
    main()