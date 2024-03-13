from gradio_client import Client
import os


class Generator(object):

    def _generate_presentation_content(
        self, title: str, author: str = "", theme: str = ""
    ):
        theme = theme or "default"
        start_prompt = f'Start your message exactly with the following:\n"Sure! Here is a long presentation on the topic {title}:\n## ..." The title slide has already been added, so just start adding main content. Syntax: add slide headings with `## <heading here>` and divide slides with `---`; add base slide text without formatting under headings. One heading and one base text per slide. Remember to divide slides with ---. Create as many slides, as possible. Do not put a lot of text in one slide, create a lot of slides instead.'
        system_prompt = "You should create a full long Marp presentation on the given theme. DO NOT use html elements and images, only basic markdown and text. Fill each slide with meaningful content. DO NOT write any other text else except what the user tells you to. Create as many slides, as possible. Do not put a lot of text in one slide, create many slides instead."
        presentation_start = (
            f"---\nmarp: true\ntheme: {theme}\n_class: lead\n---\n\n# {title}\n"
        )
        presentation_start += f"by {author}\n\n---\n" if author else "\n---\n"

        client = Client("huggingface-projects/llama-2-13b-chat")

        # Generate presentation
        print("Generating the first part...")
        first_part = client.predict(
            start_prompt,  # str  in 'Message' Textbox component
            system_prompt,  # str  in 'System prompt' Textbox component
            2048,  # float (numeric value between 1 and 2048) in 'Max new tokens' Slider component
            0.1,  # float (numeric value between 0.1 and 4.0) in 'Temperature' Slider component
            0.05,  # float (numeric value between 0.05 and 1.0) in 'Top-p (nucleus sampling)' Slider component
            1,  # float (numeric value between 1 and 1000) in 'Top-k' Slider component
            1,  # float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
            api_name="/chat",
        )

        # Add presentation start and generate the first part
        first_part = presentation_start + "---".join(
            first_part.split(
                f"Sure! Here is a long presentation on the topic {title}:"
            )[-1].split("---")[:-2:]
        )

        # Generate the second part
        print("Generating the second part...")
        second_part = client.predict(
            first_part,  # str  in 'Message' Textbox component
            system_prompt,  # str  in 'System prompt' Textbox component
            2048,  # float (numeric value between 1 and 2048) in 'Max new tokens' Slider component
            0.1,  # float (numeric value between 0.1 and 4.0) in 'Temperature' Slider component
            0.05,  # float (numeric value between 0.05 and 1.0) in 'Top-p (nucleus sampling)' Slider component
            1,  # float (numeric value between 1 and 1000) in 'Top-k' Slider component
            1,  # float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
            api_name="/chat",
        )

        return first_part + second_part

    def _process_markdown(self, presentation_content: str, file_format: str) -> None:
        # Save presentation as a markdown file
        with open("./presentation.md", "w") as file:
            file.write(presentation_content)

        print("Generating document...")
        os.system(
            f"docker run --rm --init -v {os.getcwd()}:/home/marp/app/ -e LANG=EN marpteam/marp-cli presentation.md --{file_format}"
        )

    def generate_presentation(
        self, file_format: str, title: str, author: str = "", theme: str = ""
    ):
        generated_content = self._generate_presentation_content(title, author, theme)
        self._process_markdown(generated_content, file_format)
