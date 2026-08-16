##.latexmkrc
$pdf_mode = 4;  # use lualatex (clean Arabic ToUnicode, no Presentation Forms)
$pdflatex = 'lualatex -interaction=nonstopmode -synctex=1 %O %S';
@default_files = ('main.tex');
