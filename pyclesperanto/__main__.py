import argparse
import sys
from typing import List, Any
from pathlib import Path
import pyclesperanto


def main(argv: List[Any]) -> int:

    parser = argparse.ArgumentParser()
    parser.add_argument("--cmakefiles", action='store_true', help="Print pyclesperanto project CMake module directory. Useful for setting clic_ROOT in CMake.")
    parser.add_argument("--prefix", action='store_true', help="Print pyclesperanto package installation prefix. Useful for setting CMAKE_PREFIX_PATH in CMake.")

    args = parser.parse_args(args=argv[1:])

    if not argv[1:]:
        parser.print_help()
        return

    prefix = Path(pyclesperanto.__file__).parent

    if args.cmakefiles:
        print(prefix / "")

    if args.prefix:
        print(prefix)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
