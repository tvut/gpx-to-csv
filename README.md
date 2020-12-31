# gpx-to-csv
Designed to take a GPX file and output a CSV file that contains the name, date, length (in miles or kilometers), elevation (in meters or feet), total time and moving time of all the tracks in the GPX file. 
## Pre-reqs
Requires ``gpxpy`` which you can install with ``pip``.
## Usage
```
$ python3 convert.py [gpx-file]
```
where ``[gpx-file]`` is the file you want to turn into a CSV.
## Output
Will product a CSV file with the same name as the input GPX file. The expected output will look something like this:

Name | Date | Length (mi) | Elevation (ft) | Total Time | Moving Time
---- | ---- | ----------- | -------------- | ---------- | -----------
Little Si | 2/9/2020 | 3.82 | 1102 | 1:50:19 | 1:22:51
Mount Si | 2/17/2020 | 7.88 | 3710 | 4:08:05 | 3:18:35
Mount Washington | 3/14/2020 | 8.69 | 3238 | 4:47:22 | 3:27:39
Franklin Falls | 3/15/2020 | 7.75 | 2327 | 3:48:32 | 3:17:10
Mailbox Peak | 3/16/2020 | 10.36 | 4341 | 4:53:18 | 4:09:48
Lake Serene | 3/17/2020 | 8.9 | 2727 | 5:55:23 | 4:08:36
Si and Teneriffe | 3/18/2020 | 14.48 | 4752 | 7:48:41 | 5:33:12


