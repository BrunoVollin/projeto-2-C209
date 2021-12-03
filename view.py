
from os import system


class AntialiasingView:
    def start_view(self):
        system('cls')

    def ask_directory(self):
        path = input(
            'Em qual diretório deseja aplicar o efeito nos arquivos?\n')
        return path

        return method

    def ask_anti_aliasing_method(self):
        method = input(
            'Qual metodo deseja utilizar?\n    1 para Hanning\n    2 para Lanczos\n')

        is_hanning = method == '1'
        method_name = "hanning" if is_hanning else "lanczos"

        return method_name

    def print_request_infos(self, method, files):
        print(f"Aplicando metodo {method} nos arquivos: {files}")
