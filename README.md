# Figma Presentation
Insert a Figma Prototype into your PPTX slideshow

1. Convert PPTX to HTML using [this](https://convertio.co/de/pptx-html/)
2. Get the iframe from figma to embed the prototype
3. Apply changes by using the command line tool

```bash
python modifier.py
  -file presentation.html
  -zoom 1.34
  -page_where_to_inject 7 
  -prototype '<iframe>...</iframe>'
```
