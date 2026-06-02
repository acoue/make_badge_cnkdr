import argparse
from utils.csv_reader import read_csv
from pdf.builder import generate_pdf



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--csv", required=True)
    parser.add_argument("--output", default="results/badges.pdf")
    parser.add_argument("--format", default="editorial", choices=["editorial", "vertical"])
    parser.add_argument("-d", "--debug", action="store_true", help="Activer le mode debug")

    args = parser.parse_args()

    participants = read_csv(args.csv)

    generate_pdf(
        participants,
        args.output,
        layout_mode=args.format,
        debug=args.debug
    )


if __name__ == "__main__":
    main()
