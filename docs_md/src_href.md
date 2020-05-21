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
</style>#Linking to source code

##docstr_md.src_href.github.**Github**

<p class="func-header">
    <i>class</i> docstr_md.src_href.github.<b>Github</b>(<i>root</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/src_href/github.py#L1">[source]</a>
</p>

Compiles a hyperlink for source code stored in a Github repository.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>root : <i>str</i></b>
<p class="attr">
    Path to the root directory of the source code. e.g. <code>'https://github.com/&lt;username&gt;/blob/master'</code>.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>root : <i>str</i></b>
<p class="attr">
    Set from the <code>root</code> parameter.
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
from docstr_md.python import PySoup, compile_md
from docstr_md.src_href import Github

src_href = Github('https://github.com/my-username/my-package/blob/master')
soup = PySoup(path='path/to/file.py', src_href=src_href)
md = compile_md(soup)
```

`md` is a string of compiled markdown with source code links in the class
and function headers.

####Methods



<p class="func-header">
    <i></i> <b>__call__</b>(<i>self, obj</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/src_href/github.py#L34">[source]</a>
</p>

Compile the hyperlink for the source code of the input object.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>obj : <i>docstr_md.soup_objects.FunctionDef or ClassDef</i></b>
<p class="attr">
    Soup object to whose souce code we are linking.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>href : <i>str</i></b>
<p class="attr">
    Hyperlink of the form <code>'&lt;root&gt;/&lt;src_path&gt;#L&lt;lineno&gt;'</code>.
</p></td>
</tr>
    </tbody>
</table>

