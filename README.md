# MkDocs PDF

This plugin allows you to embed PDFs in your documentation using standard
Markdown syntax.

## Installation

Install the package with pip

```
pip install mkdocs-pdf
```

## Configuration

```yaml
# mkdocs.yml
markdown_extensions:
  - attr_list
plugins:
  - mkdocs-pdf
```

## Usage

To embed a PDF file simple use the following syntax.

```markdown
![Alt text](<path to pdf>){ type=application/pdf }
```

Optionally, you can specify style constraints, e.g.

```markdown
![Alt text](<path to pdf>){ type=application/pdf style="min-height:25vh;width:100%" }
```
