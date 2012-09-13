import errno
import codecs
import os
import os.path

import jinja2

def render(input_directory, output_directory, excluded_paths=tuple(), custom_filters=None):
    if custom_filters is None:
        custom_filters = dict()

    loader = jinja2.FileSystemLoader(input_directory)
    environment = jinja2.Environment(loader=loader)

    # Load custom filters before loading templates
    environment.filters.update(custom_filters)

    for directory_path, directories, file_names in os.walk(input_directory):
        # Remove input_path redundacy
        directory_path = os.path.relpath(directory_path, input_directory)

        if not directory_path in excluded_paths:
            for file_name in file_names:
                template_path = os.path.join(directory_path, file_name)
                template_path = os.path.normpath(template_path)

                template = environment.get_template(template_path)
                rendered_template = template.render()

                rendered_template_path = os.path.join(output_directory, template_path)
                
                _write(rendered_template, rendered_template_path)

def _write(contents, path):
    directory = os.path.dirname(path)

    try:
        os.makedirs(directory)
    except OSError as exception:
        if exception.errno == errno.EEXIST:
            pass
        else:
            raise

    with codecs.open(path, mode='w', encoding='utf-8') as f:
        f.write(contents)
