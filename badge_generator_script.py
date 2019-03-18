import sys
import os
import requests
import csv
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def draw_badge_template(family_name):
   
    # default for test purposes
    # family_name = "virgo"
    
    badge_template_image = Image.open("badge_templates/" + family_name + ".png", mode = 'r')

    return badge_template_image


def draw_profile_picture(image, url=""):

    # coordinates to draw profile picture
    coord = (228, 387)
    
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

def main():
    
    family_to_generate = ""
    
    # read attendee data into dict
    with open('attendee_data.csv', encoding='latin1') as csv_file:

        # dictionary reader
        csv_reader = csv.DictReader(csv_file)
        
        # set 1 to skip header line
        line_count = 1

        # get each attendee info
        for attendee in csv_reader:            

            # generate family badges
            if attendee["family_name"].lower() == family_to_generate:
                print(f"{attendee['first_name']} {attendee['last_name']} is in " + family_to_generate + "!")
                 
                
                # check if attendee is missing profile pic URL
                if (attendee["img"].lower() == "null"):
                    print(f"ERROR: The following attendee is missing profile picture URL: {attendee['first_name']} {attendee['last_name']})")
                    
                    continue

                # ----- generate badge -----

                family_name  = ""
                url = attendee["img"]
                name = attendee["first_name"] + " " + attendee["last_name"]

                if (attendee["code"].lower() == "fl16"):
                    family_name = family_to_generate + "_leader"                    
                else:
                    family_name = family_to_generate + "_attendee"

                badge = draw_badge_template(family_name)
                draw_profile_picture(badge, url)
                draw_name(badge, name)
                
                badge.save("badges_final/" + family_to_generate + "/" + family_name + "_" + name + ".png")

            # generate non-family badges
            elif attendee["family_name"] == "null":
                
                # if attendee is VIP
                if attendee["code"] == "VIPALUM":

                    badge = draw_badge_template("to-add/vip")
                    draw_profile_picture(badge, attendee["img"])
                    draw_name(badge, attendee["first_name"] + " " + attendee["last_name"])

                    badge.save("badges_final/STAFF/VIP/" + attendee["first_name"] + " " + attendee["last_name"] + ".png")
                elif attendee["code"] == "LS7Staff":
                    
                    print(f"generating {attendee['first_name']} {attendee['last_name']}'s badge...")
                    if (attendee["img"] == "null"):
                        print(f"ERROR: {attendee['first_name']} {attendee['last_name']} is missing image...continuing")
                        continue
                    badge = draw_badge_template("to-add/staff")
                    draw_profile_picture(badge, attendee["img"])
                    draw_name(badge, attendee["first_name"] + " " + attendee["last_name"])

                    badge.save("badges_final/STAFF/" + attendee["first_name"] + " " + attendee["last_name"] + ".png")

    print("\nEnd of program.")


if __name__ == "__main__":
    main()

