import argparse
from utils.csv_reader import read_csv
from pdf.builder import generate_pdf


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--output", default="results/badges.pdf")

    args = parser.parse_args()

    participants = read_csv(args.csv)
    generate_pdf(participants, args.output)


if __name__ == "__main__":
    main()