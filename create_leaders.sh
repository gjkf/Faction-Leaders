#! /bin/bash

cd source
for dir in */ 
do
    dir=${dir%*/} # remove the trailing "/"    
    cd $dir
    ls
    mkdir ../../images/$dir
    for file in `ls *.tex`; do
      lualatex --output-directory=../../images/$dir $file
      lualatex --output-directory=../../images/$dir $file
    done
done

cd ../../images
for dir in */
do
  cd $dir
  for file in `ls *.pdf`; do
    convert -density 600 -quality 100 "${file}" "${file%.*}.png" # important not to have "-alpha flatten"
  done
  rm *.log
  rm *.aux
done
