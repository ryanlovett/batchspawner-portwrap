import argparse
import sys

from runpy import run_path
from shutil import which


def main():
    parser = argparse.ArgumentParser(
        description="Launch portwrapped command from jupyterhub spawner."
    )
    parser.add_argument(
        "-P",
        "--guest-port",
        dest="guest_port",
        default=8888,
        type=int,
        help="Namespace-accessible port",
    )
    args, remainder = parser.parse_known_args()

    cmd = []
    port = None
    for arg in remainder:
        if arg.startswith("--port="):
            port = arg.split("=")[1]
            arg = "--port={guest-port}"
        cmd.append(arg)
    if not port:
        raise Exception("No port specified in command.")

    sys.argv = ["portwrap", "-p", port, "-P", str(args.guest_port)] + cmd

    run_path(which("portwrap"), run_name="__main__")


if __name__ == "__main__":
    main()
