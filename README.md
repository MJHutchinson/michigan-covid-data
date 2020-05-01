# michigan-covid-data

Polls the Michigan state Covid statistics page every hour to save a snapshot of the site. This is to be precessed later to let us calculate daily statistics from it. 

To get this running:
- Ensure that `poll_website.sh` and `setup.sh` have the executable  flag set.
- Add the following to your crontab (`crontab -e` to edit): `0 * * * * PATH_TO_FOLDER/michigan-covid-data/poll_website.sh >> PATH_TO_FOLDER/michigan-covid-data/log.txt`