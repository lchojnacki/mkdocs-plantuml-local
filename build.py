from hashlib import sha256
from pathlib import Path
from urllib.request import urlopen

# to upgrade: bump the version and take the sha256 digest of plantuml-<version>.jar
# from https://github.com/plantuml/plantuml/releases
PLANTUML_VERSION = "1.2026.10"
PLANTUML_SHA256 = "e9bc9e6b2eb715e8c0c929f3dcb5fc1923be13f37599b09c293c66d354e88686"
PLANTUML_URL = (
    "https://github.com/plantuml/plantuml/releases/download/"
    f"v{PLANTUML_VERSION}/plantuml-{PLANTUML_VERSION}.jar"
)


def download_plantuml():
    print(f"Downloading PlantUML {PLANTUML_VERSION}")
    with urlopen(PLANTUML_URL) as response:
        jar = response.read()

    digest = sha256(jar).hexdigest()
    if digest != PLANTUML_SHA256:
        raise RuntimeError(
            f"PlantUML checksum mismatch: expected {PLANTUML_SHA256}, got {digest}"
        )

    jar_path = Path(__file__).parent / "mkdocs_plantuml_local" / "plantuml.jar"
    jar_path.write_bytes(jar)


if __name__ == "__main__":
    download_plantuml()
