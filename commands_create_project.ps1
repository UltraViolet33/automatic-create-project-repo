
$repo_name = $args[0]
$url_to_clone = $args[1]
$project_type = $args[2]
# git clone $url_to_clone
mkdir $repo_name
cd $repo_name
touch README.md

"#$repo_name" | Out-File README.md
if ($project_type  -eq "JS")
{
    touch index.html style.css index.js
}
elseif ($project_type -eq "HTML/CSS")
{
    touch index.html style.css
}
else
{
    touch main.py
}
code .
