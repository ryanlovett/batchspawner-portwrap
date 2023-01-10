import argparse
import os
import sys

from runpy import run_path
from shutil import which


def main():
    parser = argparse.ArgumentParser(
        description="Sandbox batchspawned jupyter servers with portwrap."
    )
    parser.add_argument(
        "-P",
        "--guest-port",
        dest="guest_port",
        default=8888,
        type=int,
        help="Namespace-accessible port",
    )
    parser.add_argument(
        "--portwrap-path",
        dest="portwrap",
        help="Path to portwrap. Default is to search PATH.",
    )
    # This argument is provided by batchspawner-singleuser.
    # We capture it and provide it to portwrap.
    parser.add_argument(
        "--port",
        dest="port",
        type=int,
        required=True,
        help="The port the notebook server will listen on",
    )

    # remainder is usually jupyterhub-singleuser and its arguments
    args, remainder = parser.parse_known_args()

    if args.portwrap and not os.path.exists(args.portwrap):
        raise Exception(f"No such file: {args.portwrap}")

    sys.argv = (
        ["portwrap", "-p", str(args.port), "-P", str(args.guest_port)]
        + remainder
        + ["--port={guest-port}"]
    )

    if args.portwrap:
        portwrap_exec = args.portwrap
    else:
        portwrap_exec = which("portwrap")
        if not portwrap_exec:
            raise Exception("Could not find 'portwrap' in PATH.")

    run_path(portwrap_exec, run_name="__main__")


if __name__ == "__main__":
    main()
