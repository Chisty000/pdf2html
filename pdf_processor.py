import fitz

class PdfProcessor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.doc = None

    def open_pdf(self):
        self.doc = fitz.open(self.pdf_path)

    def extract_text_to_file(self, output_file_path="output.txt"):
        out = open(output_file_path, "wb")
        for page in self.doc:
            text = page.get_text().encode("utf8")
            out.write(text)
            out.write(bytes((12,)))
        out.close()

    def extract_images(self):
        for page_index in range(len(self.doc)):
            page = self.doc[page_index]
            image_list = page.get_images()

            if image_list:
                print(f"Found {len(image_list)} images on page {page_index}")
            else:
                print("No images found on page", page_index)

            for image_index, img in enumerate(image_list, start=1):
                xref = img[0]
                pix = fitz.Pixmap(self.doc, xref)

                if pix.n - pix.alpha > 3:
                    pix = fitz.Pixmap(fitz.csRGB, pix)

                pix.save(f"page_{page_index}-image_{image_index}.png")
                pix = None

    def close_pdf(self):
        if self.doc:
            self.doc.close()

# Example usage:
pdf_processor = PdfProcessor("Afghan Refugee Crisis.pdf")
pdf_processor.open_pdf()
pdf_processor.extract_text_to_file()
pdf_processor.extract_images()
pdf_processor.close_pdf()
