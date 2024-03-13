import json
from os import name
import generation


if __name__ == "__main__":
    # token = input("Enter your Hugging Face API token: ")
    # title = input("Enter title: ")
    # author = input("Enter author (optional): ")
    # theme = input("Enter theme (optional): ")
    token = "what"
    title = "AI Applications"
    author = "Alex Yelisieiev"
    theme = ""

    generator = generation.Generator(token)
    result = generator.generate(title, author, theme)
    with open("./presentation.md", "w") as file:
        file.write(result)
    print(result)
