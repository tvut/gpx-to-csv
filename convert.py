import gpxpy
import gpxpy.gpx
import sys
import os
import math as mod_math
import datetime
import csv

miles = True
seconds = False
time_shift = -8 #PDT SHIFT
KM_TO_MILES = 0.621371
M_TO_FEET = 3.28084

class Track:
    def __init__(self, name, date, length, elevation, moving, stopped, duration):
        self.name = name
        self.date = date
        self.length = length
        self.elevation = elevation
        self.duration = duration
        self.stopped = stopped
        self.moving = moving
    def __lt__(self, other):
        if self.date<other.date:
            return True
        return False
    def __gt__(self, other):
        if self.date>other.date:
            return True
        return False

def format_long_length(length: float) -> float:
    if miles:
        return(length / 1000. * KM_TO_MILES)
    return length/1000

def format_short_length(length: float) -> float:
    if miles:
        return length * M_TO_FEET
    return length

def format_time(time_s: float) -> str:
    if not time_s:
        return 'n/a'
    elif seconds:
        return str(int(time_s))
    else:
        minutes = mod_math.floor(time_s / 60.)
        hours = mod_math.floor(minutes / 60.)
        return '%s:%s:%s' % (str(int(hours)).zfill(2), str(int(minutes % 60)).zfill(2), str(int(time_s % 60)).zfill(2))

def start_date_adjust(track):
    return (track.get_time_bounds().start_time+datetime.timedelta(hours = time_shift)).date()



if len(sys.argv) != 2:
    print("ERROR: Args not correct. Specify gpx path.")
    exit
if os.path.splitext(sys.argv[1])[1].lower() != ".gpx":
    print("ERROR: File isn't a gpx file.")
    exit
if not os.path.exists(sys.argv[1]):
    print("ERROR: File doesn't exist.")
    exit

gpx_file = open(sys.argv[1])
gpx = gpxpy.parse(gpx_file)

tracks = []

for track in gpx.tracks:
    total_up, total_length, moving_time, stopped_time = 0, 0, 0, 0
    for segment in track.segments:
        uphill, downhill = segment.get_uphill_downhill()

        total_up += format_short_length(uphill)
        total_length += format_long_length(segment.length_2d())
        moving_time += segment.get_moving_data().moving_time
        stopped_time += segment.get_moving_data().stopped_time
    tracks.append(Track(track.name, start_date_adjust(track),total_length,total_up,format_time(moving_time),format_time(stopped_time),format_time(moving_time+stopped_time)))

tracks.sort()

with open(os.path.splitext(sys.argv[1])[0]+'.csv', 'w') as csvfile:  
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    if miles:
        filewriter.writerow(['Name', 'Date', 'Length (mi)', 'Elevation Gain (ft)', 'Total Time', 'Moving Time'])
    else:
        filewriter.writerow(['Name', 'Date', 'Length (km)', 'Elevation Gain (m)', 'Total Time', 'Moving Time'])
    for track in tracks:
        filewriter.writerow([track.name, track.date, round(track.length, 2), int(track.elevation), track.duration, track.moving])