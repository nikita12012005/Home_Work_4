class TxtFileAdapter:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_txt_file(self):
        data = []
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            headers = lines[0].strip().split(',')

            for line in lines[1:]:
                values = line.strip().split(',')
                data.append(dict(zip(headers, values)))

        return data

    def convert_to_html(self):
        data = self.read_txt_file()
        html = ''

        for item in data:
            for key, value in item.items():
                html += f'\t<{key}>{value}</{key}>\n'

        return html


# Usage example
txt_file_path = 'user.txt'
adapter = TxtFileAdapter(txt_file_path)
html_output = adapter.convert_to_html()
print(html_output)
