##.latexmkrc
$pdf_mode = 5;  # use xelatex
$pdflatex = 'xelatex -interaction=nonstopmode -synctex=1 %O %S';
@default_files = ('main.tex');
