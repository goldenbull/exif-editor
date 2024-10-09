from datetime import datetime
from pathlib import Path

import arrow
import exif

if __name__ == '__main__':
    ts = arrow.get("2021-06-10T12:38:05+08:00")
    root = Path(r"D:\tmp\tt")
    for fname in root.glob("*.jpg"):
        img = exif.Image(fname)
        img.datetime_original = ts.format("YYYY:MM:DD HH:mm:ss")
        fname.open("wb").write(img.get_file())


