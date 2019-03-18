import sys
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def draw_badge_template(family_name):
   
    # default for test purposes
    # family_name = "virgo"
    
    badge_template_image = Image.open(family_name + "_badge_template.png", mode = 'r')

    return badge_template_image


def draw_profile_picture(image, url=""):

    # coordinates to draw profile picture
    coord = (228, 387)
    
    # profile picture (from URL)
    profile_picture_url   = "http://graph.facebook.com/2295395780480331/picture?width=500&height=500"

    profile_picture       = requests.get(profile_picture_url)
    profile_picture_image = Image.open(BytesIO(profile_picture.content))
    profile_picture_image = profile_picture_image.resize((527, 507))
    
    image.paste(profile_picture_image, coord) 
    
def draw_name(image, name):
    fontPath      = 'fonts/leaguespartan-bold.ttf'
    leagueSpartan = ImageFont.truetype(fontPath, 40)

    # attendee name
    name = "John Nguyen"
    attendee_name = ImageDraw.Draw(image)
    w, h = leagueSpartan.getsize(name)
    attendee_name.text(((1010 - w) / 2,950), name, font=leagueSpartan )

    image.save("test_user_badge.png")

def main():

    badge = draw_badge_template("virgo")
    draw_profile_picture(badge)
    draw_name(badge, "John Nguyen")
    
    badge.save("test_user_badge.png")

    print("\nEnd of program.")


if __name__ == "__main__":
    main()

