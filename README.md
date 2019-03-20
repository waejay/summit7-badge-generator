# UVSA South Summit 7 - Badge Generator

The python scripts here were used to generate around ~300 attendee badges, each of which differed in the following: name, family, and badge template. The script simply reads a .csv file into a python dictionary and uses the python PIL library to generate a badge .png with each attendee's name and his/her corresponding family's badge template.

## Getting Started

There are few requirements to try this script out yourself. For a beginner without any experience, pull up your Mac's terminal (if you're using Windows, I can't help you there mate) and run the following (using Homebrew):

'''
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install python
$ brew install libtiff libjpeg webp little-cms2
$ pip install Pillow
'''

### Prerequisites

The following files are the core files used by the script:

```
- attendee data (attendee_data.csv)
- badge generator script (badge_generator_script.py)
- set of badge templates (./badge_templates)
- league spartan font (./fonts/leaguespartan-bold.ttf)
```

## Running the script

The script was mainly used by me (and no one else), thus this script requires in-code modification between each time the script is run. 

## Authors

* **John Bao Nguyen** - *Initial work* - [waejay](https://github.com/waejay)
