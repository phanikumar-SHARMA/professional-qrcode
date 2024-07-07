import qrcode
import random
from pathlib import Path

def generate_QR(data):
    name = data[0]
    age = data[1]
    gender = data[2]
    address = data[3]
    contact = data[4]
    fname = data[5]
    mname = data[6]
    hobbies = data[7]
    skills = data[8]
    work = data[9]
    education = data[10]

    my_data = f'''
Name: {name}
Age: {age}
Gender: {gender}
Address: {address}
Contact: {contact}
Father's Name: {fname}
Mother's Name: {mname}
Hobbies: {hobbies}
Skills: {skills}
Work: {work}
Education: {education}
'''

    # Create a QR code object
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=5,
    )

    # Add data to the QR code
    qr.add_data(my_data)
    # Generate the QR code
    qr.make(fit=True)

    # Define colors
    colors = ['blue', 'green', 'black', 'brown', 'navy', 'purple', 'red']
    bg_colors = ['white', 'aqua', 'pink', 'orange', 'gold', 'yellow']

    # Select random colors
    fill_color = random.choice(colors)
    back_color = random.choice(bg_colors)

    # Create an image from the QR code with the selected colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the QR code image to the static folder
    static_dir = Path(__file__).resolve().parent.parent / 'intro' / 'static' / 'intro'
    static_dir.mkdir(parents=True, exist_ok=True)
    img.save(str(static_dir / 'StudentQR.png'))  # Convert PosixPath to string


def display_data(data):
    name = data[0]
    age = data[1]
    gender = data[2]
    address = data[3]
    contact = data[4]
    fname = data[5]
    mname = data[6]
    hobbies = data[7]
    skills = data[8]
    work = data[9]
    education = data[10]

    my_data = f'''
Name: {name}\n
Age: {age}\n
Gender: {gender}\n
Address: {address}\n
Contact: {contact}\n
Father's Name: {fname}\n
Mother's Name: {mname}\n
Hobbies: {hobbies}\n
Skills: {skills}\n
Work: {work}\n
Education: {education}\n
'''
    return my_data  # Correct variable name in display data to display line by line
