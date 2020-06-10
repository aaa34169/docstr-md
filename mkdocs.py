from docstr_md.python import PySoup, compile_md
from docstr_md.src_href import Github

src_href = Github('https://github.com/dsbowen/docstr-md/blob/master')

path = 'docstr_md/python/__init__.py'
soup = PySoup(path=path, parser='sklearn', src_href=src_href)
soup.rm_properties()
compile_md(soup, compiler='sklearn', outfile='docs_md/python/basic_use.md')

path = 'docstr_md/src_href/github.py'
soup = PySoup(path=path, parser='sklearn', src_href=src_href)
soup.objects.insert(0, '#Linking to source code')
compile_md(soup, compiler='sklearn', outfile='docs_md/src_href.md')

path = 'docstr_md/python/soup_objects.py'
soup = PySoup(path=path, parser='sklearn', src_href=src_href)
soup.keep_objects('Expr', 'FunctionDef', 'ClassDef')
soup.rm_properties()
soup.import_path = 'docstr_md/python'
compile_md(soup, compiler='sklearn', outfile='docs_md/python/soup_objects.md')

path = 'docstr_md/python/parsers/sklearn.py'
soup = PySoup(path=path, parser='sklearn', src_href=src_href)
soup.import_path = 'docstr_md/python/parsers'
soup.objects.insert(0, '#Parsers')
compile_md(soup, compiler='sklearn', outfile='docs_md/python/parsers.md')

path = 'docstr_md/python/compilers/sklearn.py'
soup = PySoup(path=path, parser='sklearn', src_href=src_href)
soup.import_path = 'docstr_md/python/compilers'
soup.objects.insert(0, '#Compilers')
compile_md(soup, compiler='sklearn', outfile='docs_md/python/compilers.md')