cd ~/michigan-covid-data

wget -O website_pull.html https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html
source venv/bin/activate

python process_snapshot.py

rm website_pull.html

git add website-snapshots/*

git commit -m 'Automatic update and push'

git push

echo "Succesful website poll"