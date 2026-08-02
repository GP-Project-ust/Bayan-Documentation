##.latexmkrc
$pdf_mode = 4;  # use lualatex (was 5 = xelatex)
$lualatex = 'lualatex -interaction=nonstopmode -synctex=1 %O %S';
@default_files = ('main.tex');
