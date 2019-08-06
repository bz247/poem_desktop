# poem_desktop
crontab + python to change desktop every day.

### Usage
1. Test the generation of the `poem.png` by running [poem_desktop.py](poem_desktop.py). There should be a `poem.png` generated in the folder.

2. Set linux to use `poem.png` as the wall paper.
	* `gsettings set org.gnome.desktop.background picture-options "centered"`
	* `gsettings set org.gnome.desktop.background picture-uri "file:///home/path_to/poem.png"`

3. Set crontab to generate a new `poem.png` every day.
	* Set [poem_desktop.py](poem_desktop.py) to executable with `chmod +x poem_desktop.py`
	* Open crontab editor `env EDITOR=vim crontab -e`. Insert at the end of the file `0 0 * * * path_to_python path_to_poem_desktop.py`
	* Use `crontab -l` to view the current job, `mail` to check messages and `crontab -r` to remove the current job.

	/home/bingyu/anaconda3/envs/geo/bin/python /home/bingyu/Documents/poem_desktop/poem_desktop.py 