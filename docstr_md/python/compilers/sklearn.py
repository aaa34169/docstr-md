from ..soup_objects import Expr, FunctionDef, ClassDef

from astor import to_source
from markdown import markdown

import os

dir_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'sklearn_templates'
)

with open(os.path.join(dir_path, 'head.html'), 'r') as head_f:
    head = head_f.read()
title_template = '##{path}**{name}**'
with open(os.path.join(dir_path, 'header.html'), 'r') as f:
    header_template = f.read()
with open(os.path.join(dir_path, 'table.html'), 'r') as f:
    table_template = f.read()
with open(os.path.join(dir_path, 'field.html'), 'r') as f:
    field_template = f.read()
with open(os.path.join(dir_path, 'item.html'), 'r') as f:
    item_template = f.read()
    
    
class SklearnCompiler():
    """
    Compiles sklearn-style markdown.

    Examples
    --------
    ```python
    soup = PySoup()
    ```
    """
    def __call__(self, soup):
        return head+'\n\n'.join([self._compile(obj) for obj in soup.objects])
    
    def _compile(self, obj):
        if isinstance(obj, str):
            return obj
        if isinstance(obj, Expr):
            return self._compile_docstr(obj.docstr)
        if isinstance(obj, FunctionDef):
            return self._compile_func(obj)
        if isinstance(obj, ClassDef):
            return self._compile_cls(obj)
        raise ValueError('Object not recognized:', obj)

    def _compile_docstr(self, docstr):
        self.docstr = docstr
        return '\n\n'.join([
            docstr['description'],
            self._compile_fields(),
            self._compile_sections(),
        ])
        
    def _compile_cls(self, cls):
        return '\n\n'.join([
            self._compile_func(cls.init, cls=cls),
            self._compile_methods(cls.methods),
        ])
        
    def _compile_func(self, func, method=False, cls=None):
        self.method = method
        return '\n\n'.join([
            self._compile_title(func, cls),
            self._compile_header(func, cls),
            self._compile_docstr(func.docstr if cls is None else cls.docstr)
        ])

    def _compile_title(self, func, cls):
        if self.method:
            return ''
        if cls is None:
            path = func.import_path
            name = func.name
        else:
            path = cls.import_path
            name = cls.name
        return title_template.format(path=path, name=name)
        
    def _compile_header(self, func, cls):
        if func is None:
            # True when class has no __init__ method
            return ''
        if cls is None:
            pfx = '' if self.method else 'def'
            ldelim = '('
            import_path = func.import_path
            name = func.name
        else:
            pfx = 'class'
            ldelim = '(self, '
            import_path = cls.import_path
            name = cls.name
        header = to_source(func.ast).splitlines()[0]
        args = header.split(ldelim, maxsplit=2)[-1].rsplit(')', maxsplit=2)[0]
        return header_template.format(
            pfx=pfx,
            import_path=import_path,
            name=name,
            args=args
        )
    
    def _compile_fields(self):
        fields = '\n'.join([
            self._compile_field(field) for field in self.docstr['fields']
        ])
        return table_template.format(fields=fields)
    
    def _compile_field(self, field):
        items = '\n'.join(
            [self._compile_item(item) for item in field['items']]
        )
        return field_template.format(name=field['name'], items=items)
    
    def _compile_item(self, item):
        item = {key: markdown(val)[3:-4] for key, val in item.items()}
        return item_template.format(**item)
    
    def _compile_sections(self):
        return '\n\n'.join([
            self._compile_section(s) for s in self.docstr['sections']
        ])
    
    def _compile_section(self, section):
        name_template = '**{}**\n\n' if self.method else '#'*4+'{}\n\n'
        return name_template.format(section[0]) + section[1]
    
    def _compile_methods(self, methods):
        if not methods:
            return ''
        return '#'*4+'Methods\n\n'+'\n\n'.join([
            self._compile_func(method, method=True) for method in methods
        ])