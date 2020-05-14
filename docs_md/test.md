<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<link rel="stylesheet" href="https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css" type="text/css" />

<style>
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
</style># Test

## src.test.**my_func**

<p class="func-header">
    <i>def</i> src.test.<b>my_func</b>(<i>param0, param1=1.0</i>)
</p>

This is my function.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>param0 : <i>str</i></b>
<p class="attr">
    This is parameter 0. <code>param0</code>.
</p>
<b>param1 : <i>float</i></b>
<p class="attr">
    This is parameter 1.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>None : <i></i></b>
<p class="attr">
    
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
my_func('hello', 'world')
```

Out:

```
hello world
```

##src.test.**MyClass**

<p class="func-header">
    <i>class</i> src.test.<b>MyClass</b>(<i>param0, param1=1, param2=lambda x: x</i>)
</p>

This is my class.
Its description is on multiple lines.

And it's two paragraphs long.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>param0 : <i>str</i></b>
<p class="attr">
    This is parameter 0.
</p>
<b>param1 : <i>int</i></b>
<p class="attr">
    This is parameter 1.
</p>
<b>param2 : <i>callable</i></b>
<p class="attr">
    This is parameter 2.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>attr0 : <i>str</i></b>
<p class="attr">
    This is attribute 0.
</p>
<b>attr1 : <i>int</i></b>
<p class="attr">
    This is attribute 1.
</p></td>
</tr>
    </tbody>
</table>

####Notes

This is a note.

####Examples

```python
print('hello world')
```

Out:

```
hello world
```

####Methods

<p class="func-header">
    <i></i> <b>print_greeting</b>(<i>self, name='world'</i>)
</p>

This method prints a greeting.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>name : <i>str</i></b>
<p class="attr">
    This is the name of the person to greet.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>greeting : <i>str</i></b>
<p class="attr">
    Of the form 'hello, {name}!'.
</p></td>
</tr>
    </tbody>
</table>



<p class="func-header">
    <i></i> <b>print_goodbye</b>(<i>self, name='moon'</i>)
</p>

This method prints goodbye.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>name : <i>str, default='moon'</i></b>
<p class="attr">
    The name of the person to say goodbye to.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>goodbye : <i>str</i></b>
<p class="attr">
    Of the form 'goodbye, {name}!'
</p></td>
</tr>
    </tbody>
</table>

**Notes**

This is a note.

**Examples**

```python
cls = MyClass(param0, param1)
cls.print_goodbye()
```

Out:

```
goodbye, moon!
```