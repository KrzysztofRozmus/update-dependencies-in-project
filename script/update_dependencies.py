import os


def read_requirements_file(filename: str) -> list[str]:
    """Read `requirements.txt` file and return list of dependencies and it's version."""

    with open(filename) as file:
        lines_in_file = file.readlines()
    return lines_in_file


def write_requirements_file(filename: str, file_content):
    """Open `requirements.txt` file and write down only dependencies names without it's versions."""

    with open(filename, "w") as file:
        dependencies_list = [x.split("==")[0] for x in file_content]
        for dependencies_name in dependencies_list:
            file.write(dependencies_name + "\n")


def update_dependencies(filename: str) -> None:
    """
    Update dependencies in a project to the latest versions
    and update `requiremnets.txt` file.

    Args:
        filename (_type_): requiremnets.txt: str
    """

    try:
        lines_in_file = read_requirements_file(filename)

    except FileNotFoundError:
        # If FileNotFoundError occurred, create `requirements.txt` file.
        print("Creating a `requiremnets.txt` file...")
        os.system("pip freeze > requirements.txt")

        lines_in_file = read_requirements_file(filename)

    finally:
        write_requirements_file(filename, lines_in_file)

        os.system("pip install --upgrade pip")
        os.system("pip install --upgrade -r requirements.txt")
        os.system("pip freeze > requirements.txt")

        stars = 10 * "*"
        print(f"\n{stars} Done {stars}")


if __name__ == "__main__":
    update_dependencies("requirements.txt")
