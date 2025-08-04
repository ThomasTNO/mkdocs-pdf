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

You can also add options to the PDF file, e.g.

```markdown
![Alt text](<path to pdf>#page=9&navpanes=0){ type=application/pdf }
```
Here the confirmed working options:
|||
|---|---|
|`page=N`|Jump to Page N.|
|`navpanes=0`|Hides the leftside navigation.|
|`toolbar=0`|Hides the top toolbar.|
|`scrollbar=0`|Hide the right side scrollbar|
