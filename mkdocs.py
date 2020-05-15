from docstr_md.python import PySoup, compile_md

path = 'docstr_md/python/__init__.py'
soup = PySoup(path=path, parser='sklearn')
compile_md(soup, compiler='sklearn', outfile='docs_md/python/basic_use.md')

path = 'docstr_md/python/soup_objects.py'
classes = ('Expr', 'FunctionDef', 'ClassDef')
soup = PySoup(path=path, parser='sklearn')
soup.objects = [
    obj for obj in soup.objects 
    if not hasattr(obj, 'name') or obj.name in classes
]
compile_md(soup, compiler='sklearn', outfile='docs_md/python/soup_objects.md')

path = 'docstr_md/python/parsers/sklearn.py'
soup = PySoup(path=path, parser='sklearn')
soup.objects.insert(0, '#Parsers')
compile_md(soup, compiler='sklearn', outfile='docs_md/python/parsers.md')

path = 'docstr_md/python/compilers/sklearn.py'
soup = PySoup(path=path, parser='sklearn')
soup.objects.insert(0, '#Compilers')
compile_md(soup, compiler='sklearn', outfile='docs_md/python/compilers.md')