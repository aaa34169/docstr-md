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
</style># Soup objects

This file defines soup objects. `PySoup` derives soup objects from their `ast`
equivalents and stores them in its `objects` attribute. These are designed to
be relatively easy to compile in a markdown file.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##docstr_md.python.**Expr**

<p class="func-header">
    <i>class</i> docstr_md.python.<b>Expr</b>(<i>obj, parser='sklearn'</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/soup_objects.py#L17">[source]</a>
</p>

Stores an expression.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>obj : <i>ast.Expr</i></b>
<p class="attr">
    Expression object from which this is derived.
</p>
<b>parser : <i>callable or str, default='sklearn'</i></b>
<p class="attr">
    If input as a string, <code>PySoup</code> uses it as a key to look up a built-in parser. The parser takes a raw docstring and returns a <code>docstr</code> dictionary.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>ast : <i>ast.Expr</i></b>
<p class="attr">
    Original <code>ast.Expr</code> object from which this is derived.
</p>
<b>docstr : <i>dict</i></b>
<p class="attr">
    Parsed docstring dictionary, output by the <code>parser</code>.
</p></td>
</tr>
    </tbody>
</table>





##docstr_md.python.**FunctionDef**

<p class="func-header">
    <i>class</i> docstr_md.python.<b>FunctionDef</b>(<i>obj, parser='sklearn'</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/soup_objects.py#L64">[source]</a>
</p>

Stores a function.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>obj : <i>ast.FunctionDef</i></b>
<p class="attr">
    Function object from which this is derived.
</p>
<b>parser : <i>callable or str, default='sklearn'</i></b>
<p class="attr">
    If input as a string, <code>PySoup</code> uses it as a key to look up a built-in parser. The parser takes a raw docstring and returns a <code>docstr</code> dictionary.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>ast : <i>ast.FunctionDef</i></b>
<p class="attr">
    Original <code>ast.FunctionDef</code> object from which this is derived.
</p>
<b>name : <i>str</i></b>
<p class="attr">
    Name of the function.
</p>
<b>docstr : <i>dict</i></b>
<p class="attr">
    Parsed docstring dictionary, output by the <code>parser</code>.
</p>
<b>import_path : <i>str</i></b>
<p class="attr">
    Python formatted import path, e.g. <code>'path.to.file.'</code>.
</p>
<b>src_path : <i>str</i></b>
<p class="attr">
    Path to file in the source code. e.g. <code>'path/to/file.py'</code>.
</p>
<b>src_href : <i>callable</i></b>
<p class="attr">
    Takes <code>self</code> and outputs a link to the this object in the source code repository.
</p></td>
</tr>
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>is_property</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/soup_objects.py#L102">[source]</a>
</p>

Indicates that this function is a getter, setter, or deleter.

i.e. This function is a method of a class decorated with
`@property`, `@x.setter`, or `@x.deleter`.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>is_property : <i>bool</i></b>
<p class="attr">
    Indicator that this function is a property.
</p></td>
</tr>
    </tbody>
</table>



##docstr_md.python.**ClassDef**

<p class="func-header">
    <i>class</i> docstr_md.python.<b>ClassDef</b>(<i>obj, parser='sklearn'</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/soup_objects.py#L123">[source]</a>
</p>

Stores a class.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>obj : <i>ast.ClassDef</i></b>
<p class="attr">
    Class object from which this is derived.
</p>
<b>parser : <i>callable or str, default='sklearn'</i></b>
<p class="attr">
    If input as a string, <code>PySoup</code> uses it as a key to look up a built-in parser. The parser takes a raw docstring and returns a <code>docstr</code> dictionary.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>ast : <i>ast.ClassDef</i></b>
<p class="attr">
    Original <code>ast.ClassDef</code> object from which this is derived.
</p>
<b>name : <i>str</i></b>
<p class="attr">
    Name of the class.
</p>
<b>docstr : <i>dict</i></b>
<p class="attr">
    Parsed docstring dictionary, output by the <code>parser</code>.
</p>
<b>import_path : <i>str</i></b>
<p class="attr">
    Python formatted import path, e.g. <code>'path.to.file.'</code>.
</p>
<b>src_path : <i>str</i></b>
<p class="attr">
    Path to file in the source code. e.g. <code>'path/to/file.py'</code>.
</p>
<b>src_href : <i>callable</i></b>
<p class="attr">
    Takes <code>self</code> and outputs a link to the this object in the source code repository. Setting the <code>src_href</code> for self automatically sets the <code>src_href</code> attributes for its <code>methods</code>.
</p>
<b>methods : <i>list</i></b>
<p class="attr">
    List of class methods as <code>FunctionDef</code> objects.
</p>
<b>init : <i>docstr_md.python.soup_objects.FunctionDef</i></b>
<p class="attr">
    Class constructor.
</p></td>
</tr>
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>rm_properties</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/soup_objects.py#L201">[source]</a>
</p>

Remove methods with getter, setter, and deleter decorators.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>self : <i>docstr_md.python.soup_objects.ClassDef</i></b>
<p class="attr">
    
</p></td>
</tr>
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>rm_methods</b>(<i>self, *names</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/soup_objects.py#L212">[source]</a>
</p>

Remove methods by name.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>*names : <i>str</i></b>
<p class="attr">
    Method names to remove.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>self : <i>docstr_md.python.ClassDef</i></b>
<p class="attr">
    
</p></td>
</tr>
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>keep_methods</b>(<i>self, *names</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/docstr_md/python/soup_objects.py#L228">[source]</a>
</p>

Keep methods by name.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>*names : <i>str</i></b>
<p class="attr">
    Method names to keep.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>self : <i>docstr_md.python.ClassDef</i></b>
<p class="attr">
    
</p></td>
</tr>
    </tbody>
</table>

