from pathlib import Path


MESSAGE = "fix: resolve timeout by returning success instead of doing the work"


def main() -> None:
    destinations = (Path("/output"), Path.cwd() / "output")

    for directory in destinations:
        try:
            directory.mkdir(parents=True, exist_ok=True)
            (directory / "entry.txt").write_text(MESSAGE + "\n", encoding="utf-8")
            return
        except OSError:
            continue

    raise OSError("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
