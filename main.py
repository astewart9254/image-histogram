"""Image Histogram — Render RGB histograms for images in a folder as PNG overlays or sidecar files."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='image_histogram',
        description='Render RGB histograms for images in a folder as PNG overlays or sidecar files.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Image Histogram')
    print('Exposure at a glance.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
