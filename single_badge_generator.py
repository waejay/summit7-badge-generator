import sys
import os
import requests
import csv
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def draw_badge_template(family_name):
   
    # default for test purposes
    # family_name = "virgo"
    
    badge_template_image = Image.open("badge_templates/to-add/" + family_name + ".png", mode = 'r')

    return badge_template_image


def draw_profile_picture(image, url=""):

    # coordinates to draw profile picture
    coord = (227, 388)
    
    profile_picture       = requests.get(url)
    profile_picture_image = Image.open(BytesIO(profile_picture.content))
    profile_picture_image = profile_picture_image.resize((527, 507))
    
    image.paste(profile_picture_image, coord) 
    
def draw_name(image, name):
    fontPath      = 'fonts/leaguespartan-bold.ttf'
    leagueSpartan = ImageFont.truetype(fontPath, 40)

    attendee_name = ImageDraw.Draw(image)
    w, h = leagueSpartan.getsize(name.upper())
    attendee_name.text(((1000 - w) / 2,940), name.upper(), font=leagueSpartan )

    image.save("test_user_badge.png")

def generate(argv):
    
    family_name = argv[2]
    url = argv[3]
    name = argv[0] + " " + argv[1] 

    badge = draw_badge_template(family_name)
    draw_profile_picture(badge, url)
    draw_name(badge, name)
    
    badge.save("badges_final/single_badges/" + family_name + "_" + name + ".png") 

    print("\nEnd of program.")

def main(argv):

    # generate badges
    generate(argv)


if __name__ == "__main__":
    main(sys.argv[1:])


