import generation


if __name__ == "__main__":
    title = input("Enter title: ")
    author = input("Enter author (optional): ")
    themes = {1: "default", 2: "gaia"}
    theme_choice = int(input("Choose theme:\n1) default\n2) gaia\n> "))
    chosen_theme = themes[theme_choice]
    file_formats = {1: "pdf", 2: "pptx", 3: "html"}
    file_format_choice = int(input("Choose file format:\n1) pdf\n2) pptx\n3) html\n> "))
    chosen_file_format = file_formats[file_format_choice]

    # Generate a presentation
    generator = generation.Generator()
    generator.generate_presentation(chosen_file_format, title, author, chosen_theme)

    print("Done")
