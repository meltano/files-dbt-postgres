from setuptools import find_packages, setup

setup(
    name="files-dbt-postgres",
    version="0.1",
    description="Meltano project files for dbt-postgres",
    packages=find_packages(),
    package_data={
        "bundle": [
            "transform/models/.gitkeep",
            "transform/profiles/postgres/profiles.yml",
            "transform/.gitignore",
            "transform/dbt_project.yml",
        ]
    },
)
