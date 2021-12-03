from view import AntialiasingView
from model import Antialiasing


class Antialiasing_controller:

    def __init__(self):
        self.view = AntialiasingView()
    
    def get_infos(self): 
        path = self.view.ask_directory()
        method = self.view.ask_anti_aliasing_method()
        antialiasing = Antialiasing(method=method, path=path)
        self.view.print_request_infos(method=method, files=antialiasing.files)
        return antialiasing
    

    def apply_method(self, antialiasing): 
        antialiasing.convert()
    

    def start(self):
        self.view.start_view()
        antialiasing = self.get_infos()
        self.apply_method(antialiasing)



