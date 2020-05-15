from docstr_md.python import PySoup, compile_md

soup = PySoup(path='test.py', parser='sklearn')
compile_md(soup, compiler='sklearn', outfile='docs_md/test.md')