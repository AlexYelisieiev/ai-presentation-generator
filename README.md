# AI Presentation Generator 📃

This Python-based project allows you to generate full-length presentations in various formats (PDF, PPTX, HTML) on a given topic. The presentation is created using the Marp framework and the content is generated using a space on Hugging Face.

## Features 🌟

- Generate a full-length presentation on any given topic.
- Choose from various themes for your presentation.
- Output the presentation in different formats: PDF, PPTX, HTML.

## Usage example 🔮

### Terminal

```powershell
Enter title: Capybaras
Enter author (optional): Alex yelisieiev
Choose theme:
1) default
2) gaia
3) uncover
> 3
Choose file format:
1) pdf
2) pptx
3) html
> 1
```

### Output document

![Screenshot 2024-03-14 154120](https://github.com/AlexYelisieiev/ai-presentation-generator/assets/62658287/3a6ba3ff-5885-41cd-baba-8923e8f385f4)

## How it works ⚙️

The `Generator` class is the main class in this project. It has three main methods:

1. `_generate_presentation_content`: This method generates the content of the presentation using the Hugging Face's language model.
2. `_process_markdown`: This method saves the generated content as a markdown file and then uses Docker to convert the markdown file into the desired format (PDF, PPTX, HTML).
3. `generate_presentation`: This is the main method that you call to generate a presentation. It takes in the desired file format, the title of the presentation, the author (optional), and the theme (optional).

## Initial Setup 📦

[Docker](https://www.docker.com/products/docker-desktop/) and [Python](https://www.python.org/) are needed for this project to work. Once they are both installed, you can quickly set up the app:

```powershell
# Pull the docker image
docker pull marpteam/marp-cli
# Clone the project
git clone "https://github.com/AlexYelisieiev/ai-presentation-generator"
# Switch to the project directory
cd ai-presentation-generator
# Create a virtual environment and activate it
python -m venv venv
venv\scripts\activate
# Install requirements
pip install -r requirements.txt
```

## Usage 💻

Once the initial setup is completed, there's no need to repeat it.
From now, you can use the app with:

```powershell
# Inside the project directory
venv\scripts\activate
python main.py
```

From there, the app will let you choose the presentation title, author, theme, and output format. After that, it will generate content for your presentation and save it in the desired format inside the project directory.

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the terms of the MIT license.
