import sys
import requests
from PIL import Image, ImageDraw
from io import BytesIO


def main():

    # badge template 
    badge_template_image  = Image.open('virgo_badge_template.png', mode = 'r')

    # profile picture (from URL)
    profile_picture_url   = "http://graph.facebook.com/2295395780480331/picture?width=500&height=500"
    profile_picture       = requests.get(profile_picture_url)
    profile_picture_image = Image.open(BytesIO(profile_picture.content))
    profile_picture_image = profile_picture_image.resize((527, 507))

    # attendee name
    attendee_name         = ImageDraw.Draw(badge_template_image)
    attendee_name.text((0,0), "Jon Ananta")

    badge_template_image.paste(profile_picture_image, (228, 387))

    badge_template_image.save("test_user_badge.png")

    print("\nEnd of program.")


if __name__ == "__main__":
    main()

