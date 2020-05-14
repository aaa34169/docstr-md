from docstr_md.python.sklearn_compiler import SklearnCompiler
from docstr_md.python.sklearn_parser import SklearnParser
from docstr_md.python.soup import Expr, FunctionDef, ClassDef

from pathlib import PurePath

import ast

parsers = {'sklearn': SklearnParser}

class PySoup():
    def __init__(self, path, parser):
        if isinstance(parser, str):
            parser = parsers[parser]()
        self.objects = []
        with open(path, 'r') as f:
            txt = f.read()
        body = ast.parse(txt).body
        for obj in body:
            if isinstance(obj, ast.Expr):
                self.objects.append(Expr(obj, parser))
            elif isinstance(obj, ast.FunctionDef):
                self.objects.append(FunctionDef(obj, parser))
            elif isinstance(obj, ast.ClassDef):
                self.objects.append(ClassDef(obj, parser))
        import_path = '.'.join(PurePath(path.split('.')[0]).parts) + '.'
        [setattr(obj, 'import_path', import_path) for obj in self.objects]


compilers = {'sklearn': SklearnCompiler}

def compile_md(soup, compiler, outfile=None):
    if isinstance(compiler, str):
        compiler = compilers[compiler]()
    md = compiler.compile(soup)
    if outfile is not None:
        with open(outfile, 'w') as f:
            f.write(md)
    return md