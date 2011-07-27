# Ginger

Ginger is a simple, context-less [Jinja][] template renderer.

## Examples

An example to render all the templates in `templates` to `output`:

    import ginger

    ginger.render('templates', 'output')

An example to render all the templates in `templates`, excluding those in
`templates/layout`, to `output`, making available to them a custom filter,
`markdown`, that calls [Python-Markdown][]'s `markdown.markdown`:

    import ginger

    import markdown

    ginger.render('templates', 'output', excluded_paths=(layout,),
        custom_filters={'markdown': lambda x: markdown.markdown(x)})

[Python-Markdown]: http://www.freewisdom.org/projects/python-markdown/
[Jinja]: http://jinja.pocoo.org/
