import qrcode



qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=4,
    )


def generate(lines):

    qr.add_data(lines)
    qr.make(fit=True)

    image = qr.make_image(fill_color='black', back_color='white')
    image.save(filename)
    qr.clear()



with open('barcode.txt') as f:
            lines = f.readlines()
            for lines in lines:
                print(lines)
                filename = f"qrcode/{lines.strip()}.png"
                print(filename)
                generate(lines)
                f.close()
                print('Выполнено, проверьте папку qrcode')




