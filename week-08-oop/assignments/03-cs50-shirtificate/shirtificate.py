import sys

from fpdf import FPDF, Align, XPos, YPos

SHIRT_IMAGE_PATH = "./shirtificate.png"
OUT_PDF_PATH = "./shirtificate.pdf"


def main():
    # Input name
    name = input("Name: ").strip()
    if not name:
        sys.exit("Name not provided")

    pdf = FPDF(orientation="portrait", format="A4", unit="mm")
    pdf.set_margin(margin=10)
    pdf.add_page()

    # Add heading
    pdf.set_y(28)
    pdf.set_font("helvetica", style="", size=48)
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.cell(text="CS50 Shirtificate", center=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Add image
    pdf.set_y(70)
    pdf.image(name=SHIRT_IMAGE_PATH, x=Align.C, w=pdf.epw)

    # Add text
    pdf.set_y(128)
    pdf.set_font("helvetica", style="", size=26)
    pdf.set_text_color(r=255, g=255, b=255)
    shirt_msg = f"{name} took CS50"
    pdf.cell(text=shirt_msg, center=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Generate PDF
    pdf.output(OUT_PDF_PATH)


if __name__ == "__main__":
    main()
