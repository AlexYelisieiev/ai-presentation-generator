# 📃 AI Presentation Generator

![Static Badge](https://img.shields.io/badge/Cloud--based-grey?style=for-the-badge&label=%E2%98%81&labelColor=informational) ![Static Badge](https://img.shields.io/badge/No_API_key_required-grey?style=for-the-badge&label=%F0%9F%94%91&labelColor=informational)

## 🌏 Overview

This Python-based project allows you to generate full-length presentations in various formats (PDF, PPTX, HTML) on a given topic. The presentation file is created using the Marp framework and the content is generated using a space on Hugging Face.

![image](https://github.com/AlexYelisieiev/ai-presentation-generator/assets/62658287/02e24069-b270-4ebf-a3a7-7eb1dc0a12ba)


## 🌟 Features

- Generate a presentation on any given topic.
- Choose from 2 presentation themes.
- Output the presentation in different formats: PDF, PPTX, and HTML.

## 🧪 Technologies Used

![Static Badge](https://img.shields.io/badge/python-blue?style=for-the-badge&logo=python&logoColor=blue&labelColor=white) ![Static Badge](https://img.shields.io/badge/marp-white?style=for-the-badge) ![Static Badge](https://img.shields.io/badge/docker-white?style=for-the-badge&logo=docker&labelColor=darkblue&logoColor=white)

## 📦 Getting Started

**If you don't want to properly set it up, just open the repo in GitHub Codespaces.**

[Docker](https://www.docker.com/products/docker-desktop/) and [Python](https://www.python.org/) are required for this project to work. Once they are both installed, you can quickly set up the app:

```powershell
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

## 💻 Usage

To start the app:

```powershell
venv\scripts\activate
python main.py
```

...and then, the app will let you choose the presentation title, author, theme, and output format. Next, it will generate content for your presentation and save it in the desired format inside the project directory.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is distributed under the MIT License. See [LICENSE.md](LICENSE.md) for more information.
