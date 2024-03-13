import json
from os import name
import generation


if __name__ == "__main__":
    title = input("Enter title: ")
    author = input("Enter author (optional): ")
    theme = input("Enter theme (optional): ")

    # Generate a presentation
    generator = generation.Generator()
    result = generator.generate(title, author, theme)

    # Save it
    with open("./presentation.md", "w") as file:
        file.write(result)

    print(result)
