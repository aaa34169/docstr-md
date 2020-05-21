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
</style>#Compilers

##docstr_md.python.compilers.**Sklearn**



Compiles sklearn-style markdown.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>

####Examples

```python
from docstr_md.python import PySoup, compilers

# replace with the appropriate file path and parser
soup = PySoup(path='path/to/file.py', parser='sklearn')
compiler = compilers.Sklearn()
md = compiler(soup)
```

`md` is a string of compiled markdown.

####Methods



<p class="func-header">
    <i></i> <b>__call__</b>(<i>self, soup</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/compilers/sklearn.py#L45">[source]</a>
</p>

Compile markdown from soup.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>soup : <i>docstr_md.python.PySoup</i></b>
<p class="attr">
    Soup to be compiled into markdown.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>md : <i>str</i></b>
<p class="attr">
    Compiled markdown.
</p></td>
</tr>
    </tbody>
</table>

