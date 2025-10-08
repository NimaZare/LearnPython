from tools.barcode_tools import BarcodeTools as bt


def main():
    print("\n ********** Barcode Generator ********** \n")
    data = input("Enter the text or URL to generate a barcode: ").strip('"').strip("'").strip()
    bt.generate_barcode(data)
    print("\n Thank you for using Barcode Generator!\n")


if __name__ == "__main__":
    main()
