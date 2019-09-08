echo "begin > bash convert.sh $1 $2 $3 $4"
if [ -d "./tmp/" ]; then
    rm -r -f ./tmp/
    echo removed existing ./tmp/
fi
mkdir ./tmp/ && cp $1 ./tmp/
f=$(basename $1)
cp $3 ./tmp/ && cp $4 ./tmp/ && cd ./tmp/
sed -i 's/TITLE/'${f%.*}'/g' template.tplx
jupyter nbconvert $f --to latex --template template.tplx
pdflatex ${f%.*}.tex && bibtex ${f%.*}.aux && pdflatex ${f%.*}.tex
cd ..
if [ ! -d "$2" ]; then
    mkdir -v -p ./$2
fi
cp ./tmp/${f%.*}.pdf $2/ && rm -r -f ./tmp/
echo "done! > bash convert.sh $1 $2 $3 $4"