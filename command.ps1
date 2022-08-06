

$nameRepo = $args[0]
$urlGit = $args[1]
git clone $urlGit
cd $nameRepo
touch README.md
code .
