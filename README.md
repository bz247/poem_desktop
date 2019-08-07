# poem_desktop
crontab + python to change desktop every day.

### Usage
1. Test the generation of the `poem.png` by running [poem_desktop.py](poem_desktop.py). There should be a `poem.png` generated in the folder.

2. Set crontab to generate a new `poem.png` every day.
	* Set [poem_desktop.sh](poem_desktop.py) to executable with `chmod +x poem_desktop.sh`
	* Open crontab editor `env EDITOR=vim crontab -e`. Insert at the end of the file `0 0 * * * path_to_poem_desktop.sh`
	* Use `crontab -l` to view the current job, `mail` to check messages and `crontab -r` to remove the current job.
