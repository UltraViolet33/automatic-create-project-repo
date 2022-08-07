
$repo_name = $args[0]
$url_to_clone = $args[1]
$project_type = $args[2]

# git clone $url_to_clone
mkdir $repo_name
Set-Location $repo_name
touch README.md

"#$repo_name" | Out-File README.md

if ($project_type -eq "js") {
    touch index.html style.css index.js
}
elseif ($project_type -eq "html-css") {
    touch index.html style.css
}
else {
    touch main.py
}

code .
