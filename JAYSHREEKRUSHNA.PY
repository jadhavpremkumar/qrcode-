import qrcode

def generate_qr_code(business_name, business_address, business_phone1, business_phone2, Instagram, YouTube, output_file):
    """
    Generate a QR code for the given business profile information and save it to a file.

    Parameters:
    business_name (str): The name of the business.
    business_address (str): The address of the business.
    business_phone (str): The phone number of the business.
    business_email (str): The email address of the business.
    social_links (dict): A dictionary of social media links.
    output_file (str): The name of the output file to save the QR code image.
    """
    # Create a string to store the business profile information with clickable phone, email, and social media links
    profile_string = (
        f"MECARD:N:{business_name};"
        f"ADR:{business_address};"
        f"TEL:{business_phone1};"
        f"TEL:{business_phone2};"
    )

    # Add social media links to the profile string, including website names
    for platform, link in Instagram.items():
        profile_string += f"URL:{platform}:{link};"
    for platform, link in YouTube.items():
        profile_string += f"URL:{platform}:{link};"

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(profile_string)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(output_file)

# Define the business profile information
business_name = "\tJAY SHREE KRUSHNA BAND"
business_address = "\tDeopur, Dhule-424002"
business_phone1 = "\t9421615642"
business_phone2 = "\t8390604087"

# Define social media links
YouTube = {
    "YouTube": "\thttps://youtube.com/@shubham_bhadane7602?si=67i2a6YN5RvaNON3",
}
Instagram = {
    "Instagram": "\thttps://www.instagram.com/jay_shree_krushna_band?igsh=MWVoYnZ2ajZxeXc4Mg==",
}

# Generate and save the QR code
output_file = "jayshreekrushnaNEW1.png"
generate_qr_code(business_name, business_address, business_phone1, business_phone2, Instagram, YouTube, output_file)