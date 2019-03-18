import sys
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
    
    family_to_generate = "virgo"
    
    # read attendee data into dict
    with open('attendee_data.csv', encoding='latin1') as csv_file:

        # dictionary reader
        csv_reader = csv.DictReader(csv_file)
        
        # set 1 to skip header line
        line_count = 1

        # get each attendee info
        for attendee in csv_reader:            

            # print name if in specified family
            if attendee["family_name"].lower() == family_to_generate:
                print(f"{attendee['first_name']} {attendee['last_name']} is in Virgo!")
                 
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

                badge.save(family_name + "_" + name + ".png")



    print("\nEnd of program.")


if __name__ == "__main__":
    main()

