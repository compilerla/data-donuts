import argparse
import sys

from PIL import ImageColor
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask


def generate(args: argparse.Namespace):
    qr = qrcode.QRCode(version=args.size, image_factory=StyledPilImage)
    qr.add_data(args.data)
    qr.make(fit=True)

    # convert hex colors to RGB tuples, adding alpha channel to the front_color
    # alpha = 0 means transparent
    # alpha = 255 means opaque
    front_color = ImageColor.getrgb(args.color) + (255,)
    back_color = (
        # convert the string "transparent" to RGBA with full transparency
        (255, 255, 255, 0)
        if args.background == "transparent"
        # if we have a background color, it doesn't need transparency/alpha
        else ImageColor.getrgb(args.background)
    )
    color_mask = SolidFillColorMask(back_color, front_color)

    img = qr.make_image(color_mask=color_mask)
    img.save(args.output)


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Generate a QR code as an PNG file",
    )

    parser.add_argument("data", help="The data to encode as a QR code")
    parser.add_argument(
        "output", help="Path to an PNG file where the QR code is written"
    )
    parser.add_argument(
        "--color",
        help="The color of the QR code in hex format, by default black",
        default="#000000",
    )
    parser.add_argument(
        "--background",
        help="The background color of the QR code in hex format, by default transparent",
        default="transparent",
    )
    parser.add_argument(
        "--size",
        help="The QR code size from 1-10, by default 4",
        default=4,
    )

    args = parser.parse_args(argv)

    generate(args)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
