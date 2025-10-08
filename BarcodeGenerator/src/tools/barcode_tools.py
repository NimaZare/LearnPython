import os
import uuid
import barcode

from PIL import Image
from barcode.writer import ImageWriter


class BarcodeTools:
    def __init__(self):
        pass

    @staticmethod
    def generate_barcode(data: str) -> str:
        """
        Generates a barcode from the provided text or URL and saves it to the output directory
        with a random name and displays the generated barcode image.
        
        :param data: Text or URL to encode into the barcode.
        :type data: str
        """
        
        random_filename = f"barcode_{uuid.uuid4().hex[:8]}"
        output_dir = os.path.join(os.getcwd(), "BarcodeGenerator", "src", "output")
        os.makedirs(output_dir, exist_ok=True)
        
        barcode_format = barcode.get_barcode_class('code128')
        barcode_object = barcode_format(data, writer=ImageWriter())
        
        output_path = os.path.join(output_dir, random_filename)
        saved_file = barcode_object.save(output_path)

        print(f"\n ==> barcode saved to:  {saved_file} \n")

        image = Image.open(saved_file)
        image.show()

