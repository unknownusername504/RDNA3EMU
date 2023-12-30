from rdna3emu.parser import parse
from rdna3emu.interpreter import build_executable, run
import argparse
from pathlib import Path
import pprint


def main():
    parser = argparse.ArgumentParser(description="Run rdna3 emulator")
    parser.add_argument("filename", help="The filename to process")
    parser.add_argument(
        "-p", "--pretty", action="store_true", help="Print the instructions."
    )
    parser.add_argument(
        "-e", "--exec", action="store_true", help="Execute the program."
    )

    args = parser.parse_args()
    fpath = Path(args.filename)

    if not fpath.exists():
        print(f"The file {args.filename} does not exist.")

    with open(fpath, "r") as f:
        for _ in range(6):
            next(f)
        data = f.read()

    instructions = parse(data)

    if args.pretty:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(instructions)

    if args.exec:
        run(build_executable(instructions))


if __name__ == "__main__":
    main()
