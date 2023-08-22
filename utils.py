import json


def extract_route(string):
    string_list = string.split(' ')
    route = string_list[1]
    new_string = route[1:]
    return new_string


def read_file(path):
    with open(path, 'rb') as f:
        return f.read()


def load_data(note):
    with open("data/" + note, 'r') as archive:
        texto = archive.read()
    return json.loads(texto)


def load_template(template):
    with open("templates/" + template, 'r') as archive:
        html = archive.read()
    return html


def write_on_file(path, dict):
    with open("data/" + path, 'r') as archive:
        texto = archive.read()
    dicionario = json.loads(texto)
    dicionario.append(dict)


def build_response(body='', code=200, reason='OK', headers=''):
    response = ""
    if headers == '':
        response = "HTTP/1.1 " + str(code) + " " + \
            reason + headers + "\n\n" + body
    else:
        response = "HTTP/1.1 " + str(code) + " " + \
            reason + "\n" + headers + "\n\n" + body
    return str(response).encode()
