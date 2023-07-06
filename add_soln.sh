dir="$1"
path_prefix="$PWD"
full_path="$path_prefix/$dir"

ERROR_DIR_EXISTS="Solution folder already exists"
SUCCESS_MSG="Solution folder for $dir created"

if [ -d full_path ]
then
    echo $ERROR_DIR_EXISTS
else
    mkdir $full_path
    cd $full_path
    cp $path_prefix/reflection_template.md README.md
    touch main.py
    echo $SUCCESS_MSG
fi