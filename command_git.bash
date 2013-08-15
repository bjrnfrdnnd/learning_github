rsync -uav --include ".*" * ../learning_github/gh-pages/.
cd ../learning_github/gh-pages
perl -p -i.bak -e 's/WebSiteRoot\ =\ \"http:\/\/localhost\/\~bn\/learning\";/WebSiteRoot\ =\ \"http:\/\/bjrnfrdnnd.github.io\/learning_github\";/g;' *html
perl -p -i.bak -e 's/WebSiteRoot\ =\ \"http:\/\/localhost\/\~bn\/learning\";/WebSiteRoot\ =\ \"http:\/\/bjrnfrdnnd.github.io\/learning_github\";/g;' */*html
git add -A
git commit  -a -m "$1"
git push
cd -
