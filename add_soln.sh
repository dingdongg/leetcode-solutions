problem_num="$1"
path_prefix="$PWD"
json_file="problems.json"

# fetch title, title slug from json file and parse it
title_slug=$(jq .[$problem_num].titleSlug $json_file | sed 's/^.//;s/.$//')
title=$(jq .[$problem_num].title $json_file | sed 's/^.//;s/.$//')
dirname="$problem_num-$title_slug"
full_path="$path_prefix/$dirname"

# console messages
ERROR_DIR_EXISTS="Solution folder already exists"
SUCCESS_MSG="Solution folder for $dirname created"

if [ -d $full_path ]
then
    echo $ERROR_DIR_EXISTS
else
    mkdir $full_path
    cd $full_path
    touch README.md 
    echo "# $problem_num - $title\n" >> README.md
    cat $path_prefix/reflection_template.md >> README.md
    touch main.py
    echo $SUCCESS_MSG
    code $full_path 
fi