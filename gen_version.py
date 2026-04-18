"""
gen_version.py — reads version from pyproject.toml, writes src/ophix_dbengine_postgres/_version.py
Run after bumping the version in pyproject.toml: python gen_version.py
"""
import tomli, pathlib
ROOT = pathlib.Path(__file__).parent
version = tomli.loads((ROOT / "pyproject.toml").read_text())["project"]["version"]
out = ROOT / "src" / "ophix_dbengine_postgres" / "_version.py"
out.write_text(f'__version__ = "{version}"\n')
print(f"Wrote {out} -> {version}")
