import ast

__all__ = ['Expr', 'FunctionDef', 'ClassDef']


class Expr():
    def __init__(self, obj, docstr_parser):
        self.ast = obj
        self.docstr = docstr_parser.parse(obj)
        
        
class Object():
    def __init__(self, obj, docstr_parser):
        self.ast = obj
        self.name = obj.name
        self.docstr = docstr_parser.parse(obj.body[0])
        self.import_path = ''
        

class FunctionDef(Object):
    pass


class ClassDef(Object):
    def __init__(self, obj, docstr_parser):
        super().__init__(obj, docstr_parser)
        methods = [
            method 
            for method in obj.body if isinstance(method, ast.FunctionDef)
        ]
        self.methods = [
            FunctionDef(method, docstr_parser) 
            for method in methods if not method.name.startswith('_')
        ]
        init = [
            FunctionDef(method, docstr_parser) 
            for method in methods if method.name == '__init__'
        ]
        self.init = init[0] if init else None
        