import re

class HtmlGenerator:
    def __init__(self, input_file_path, output_file_path="index.html"):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.text = ""
        self.paragraphs = []

    def read_input_file(self):
        with open(self.input_file_path, "r", encoding="utf-8") as file:
            self.text = file.read()

    def split_into_paragraphs(self):
        self.paragraphs = [paragraph.strip() for paragraph in re.split(r'\n\s*\n', self.text)]

    def generate_html_content(self):
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="styles.css">
            <title>Styled Article</title>
        </head>
        <body>

            <article class="main-article">
        """

        # Add paragraphs to the HTML content
        # Split the first paragraph by lines
        lines = self.paragraphs[0].split('\n')

        # Add h1 for the first line and h2 for the second line
        if len(lines) >= 1:
            html_content += f"                <header><h1>{lines[0]}</h1></header>\n"
        if len(lines) >= 2:
            html_content += f"                <h3>{lines[1]}</h3>\n"

        # Add the rest of the paragraphs to the HTML content
        for i, paragraph in enumerate(self.paragraphs[1:], start=2):
            clean_paragraph = paragraph.replace('\x0c', '')
            html_content += f"                <p>{clean_paragraph}</p>\n"

        # Complete the HTML content
        html_content += """
            </article>
        </body>
        </html>
        """

        return html_content

    def write_to_output_file(self, html_content):
        with open(self.output_file_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"{self.output_file_path} generated successfully.")

    def generate_html_file(self):
        self.read_input_file()
        self.split_into_paragraphs()
        html_content = self.generate_html_content()
        self.write_to_output_file(html_content)

# Example usage:
file_path = "output.txt"
html_generator = HtmlGenerator(input_file_path=file_path)
html_generator.generate_html_file()
