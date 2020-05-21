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
</style>#Parsers

##docstr_md.python.parsers.**Sklearn**

<p class="func-header">
    <i>class</i> docstr_md.python.parsers.<b>Sklearn</b>(<i>raw_sections=('Notes', 'Examples')</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/parsers/sklearn.py#L5">[source]</a>
</p>

Parses sklearn-style docstrings.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>raw_sections : <i>iterable of strings, default=('Notes','Examples')</i></b>
<p class="attr">
    List of section names whose content will be treated as raw markdown. Other sections are treated as fields.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>raw_sections : <i>iterable of strings</i></b>
<p class="attr">
    From <code>raw_sections</code> parameter.
</p></td>
</tr>
    </tbody>
</table>

####Notes

`'\'` functions as an escape character when added to the beginning of a
line. Whitespace to its left will be stripped. All text to its right will
be treated as raw markdown.

####Examples

```python
from docstr_md.python import parsers

docstr_txt = '''
Description.

Field0
------
item0 : short description
    Long description.

item1 : short description
   Long description.

Field1
------
item0 : short description
   Long description

Notes
-----
Here is a note.

Examples
--------
Here is an example.
'''

parser = parsers.Sklearn()
parser(docstr_txt)
```

Out:

```
{
    'description': 'Description.',
    'sections': [
        ('Notes', 'Here is a note.'),
        ('Examples', 'Here is an example.')
    ],
    'fields': [
        {
            'name': 'Field0',
            'items': [
                {
                    'name': 'item0',
                    'short_desc': 'short description',
                    'long_desc': 'Long description.'
                },
                {
                    'name': 'item1',
                    'short_desc': 'short description',
                    'long_desc': 'Long description.'
                }
            ]
        },
        {
            'name': 'Field1',
            'items': [
                {
                    'name': 'item0',
                    'short_desc': 'short description',
                    'long_desc': 'Long description'
                }
            ]
        }
    ]
}
```

####Methods



<p class="func-header">
    <i></i> <b>__call__</b>(<i>self, obj</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/parsers/sklearn.py#L102">[source]</a>
</p>

Parses the docstring.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>obj : <i>str or docstr_md.python.soup_objects.Expr</i></b>
<p class="attr">
    Raw docstring to be parsed.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>docstr : <i>dict</i></b>
<p class="attr">
    Parsed docstring dictionary. A dictionary contains a description (str), raw markdown sections (list), and fields (list). Each section is a (name, markdown) tuple. Each field contains a name (str) and items (list). Each item contains a name (str), a short description (usually the data type, str), and a long description (str).
</p></td>
</tr>
    </tbody>
</table>

