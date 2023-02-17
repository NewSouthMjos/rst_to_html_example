from docutils.core import publish_file

publish_file(
    source_path="README3.rst",
    destination_path="README3.html",
    parser_name="rst",
    writer_name="html",
)
