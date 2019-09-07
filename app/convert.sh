if [[ -d "tmp/" ]]; then
    rm -r -f tmp/
fi
mkdir tmp/ && cp $1 tmp/
f=$(basename $1)
cp $3 tmp/ && cp $4 tmp/ && cd tmp/
jupyter nbconvert $f --to latex --template template.tplx
pdflatex ${f%.*}.tex && bibtex ${f%.*}.aux && pdflatex ${f%.*}.tex
cd .. && cp tmp/${f%.*}.pdf $2 && rm -r -f tmp/
echo done!