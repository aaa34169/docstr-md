<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<link rel="stylesheet" href="https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css" type="text/css" />

<style>
    a.src-href {
        float: right;
    }
    p.attr {
        margin-top: 0.5em;
        margin-left: 1em;
    }
    p.func-header {
        background-color: gainsboro;
        border-radius: 0.1em;
        padding: 0.5em;
        padding-left: 1em;
    }
    table.field-table {
        border-radius: 0.1em
    }
</style># Basic Use

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##docstr_md.python.**PySoup**

<p class="func-header">
    <i>class</i> docstr_md.python.<b>PySoup</b>(<i>code=None, path='', parser='sklearn', src_href=None</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/__init__.py#L15">[source]</a>
</p>

This class parses raw Python code for easy conversion to markdown.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>code : <i>str, default=None</i></b>
<p class="attr">
    Raw Python code.
</p>
<b>path : <i>str, default=''</i></b>
<p class="attr">
    Path to python file. One of <code>code</code> or <code>path</code> must be specified.
</p>
<b>parser : <i>callable or str, default='sklearn'</i></b>
<p class="attr">
    If input as a string, <code>PySoup</code> uses it as a key to look up a built-in parser. The parser takes a raw docstring and returns a <code>docstr</code> dictionary.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>objects : <i>list</i></b>
<p class="attr">
    List of soup objects; expressions (<code>Expr</code>), functions (<code>FunctionDef</code>), classes (<code>ClassDef</code>) or string. Strings are usually interpreted as raw markdown.
</p>
<b>parser : <i>callable</i></b>
<p class="attr">
    The input <code>parser</code>.
</p>
<b>import_path : <i>str</i></b>
<p class="attr">
    Import path for soup objects. Setting the import path for the soup automatically sets the import path for its <code>objects</code>.
</p>
<b>src_path : <i>str</i></b>
<p class="attr">
    Path to the file in the source code repository (e.g. Github). Setting the source code path for the soup automatically sets the source code path for its <code>objects</code>.
</p>
<b>src_href : <i>callable</i></b>
<p class="attr">
    The <code>src_href</code> takes a soup object (<code>FunctionDef</code> or <code>ClassDef</code>) and converts it to a link to the source code. Setting the <code>src_href</code> for the soup automatically sets the <code>src_href</code> attribute for its <code>objects</code>.
</p></td>
</tr>
    </tbody>
</table>

####Examples

Create a python file with [parseable docstrings](../../python/parsers).

```python
from docstr_md.python import PySoup

# replace with the appropriate file path and docstring parser
soup = PySoup(path='path/to/file.py', parser='sklearn')
```

####Methods



<p class="func-header">
    <i></i> <b>convert_ast_object</b>(<i>self, obj</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/__init__.py#L130">[source]</a>
</p>

Convert an `ast` object to a soup object.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>obj : <i>ast.Expr, ast.FunctionDef, or ast.ClassDef</i></b>
<p class="attr">
    <code>ast</code> object to convert.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>soup_object : <i>Expr, FunctionDef, or ClassDef</i></b>
<p class="attr">
    Specified in docstr_md/python/soup_objects.py.
</p></td>
</tr>
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>rm_properties</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/__init__.py#L152">[source]</a>
</p>

Remove methods with getter, setter, and deleter decorators from all
`ClassDef` soup objects in the `objects` list.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>self : <i>docstr_md.python.PySoup</i></b>
<p class="attr">
    
</p></td>
</tr>
    </tbody>
</table>

####Examples

Create a python file with a class with methods decorated with
`@property`, `@x.setter`, or `@x.deleter`.

```python
from docstr_md.python import PySoup

soup = PySoup(path='path/to/file.py', parser='sklearn')
soup.rm_properties()
```

The `ClassDef` soup objects' `methods` will no longer include
properties.

##docstr_md.python.**compile_md**

<p class="func-header">
    <i>def</i> docstr_md.python.<b>compile_md</b>(<i>soup, compiler='sklearn', outfile=None</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/__init__.py#L186">[source]</a>
</p>

Compile markdown from a `PySoup` object.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>soup : <i>PySoup</i></b>
<p class="attr">
    Soup object to convert to markdown.
</p>
<b>compiler : <i>callable or str, default='sklearn'</i></b>
<p class="attr">
    If input as a string, it <code>compiler</code> is used as a key to look up a built-in compiler. The compiler takes the <code>soup</code> and returns a string in markdown format.
</p>
<b>outfile : <i>str or None</i></b>
<p class="attr">
    File to which to write the markdown.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>markdown : <i>str</i></b>
<p class="attr">
    Markdown formatted as output by the <code>compiler</code>.
</p></td>
</tr>
    </tbody>
</table>

####Examples

Create a python file with [parseable docstrings](../../python/parsers).

```python
from docstr_md.python import PySoup, compile_md

# replace with the appropriate file path and parser
soup = PySoup(path='path/to/file.py', parser='sklearn')
# replace with your desired compiler and output file path
compile_md(soup, compiler='sklearn', outfile='path/to/outfile.md')
```

You can find the compiled markdown file in `test.md`.