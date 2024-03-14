from gradio_client import Client
import os


class Generator(object):

    def _generate_presentation_content(
        self, title: str, author: str = "", theme: str = ""
    ):
        """
        Generates a Marp presentation with the given title, author, and theme.

        Args:
            title: Title of the presentation.
            author: Author of the presentation. Defaults to an empty string.
            theme: Theme of the presentation. Defaults to "default".

        Returns:
            str: The generated presentation in markdown format.
        """
        theme = theme or "default"
        start_prompt = f'Start your message exactly with the following:\n"Sure! Here is a long presentation on the topic {title}:\n## ..." The title slide has already been added, so just start adding main content. Syntax: add slide headings with `## <heading here>` and divide slides with `---`; add base slide text without formatting under headings. One heading and one base text per slide. Remember to divide slides with ---. Put LITTLE OF TEXT in each slide and remember to divide slides with ---.'
        system_prompt = "You should create a full long Marp presentation on the given theme. DO NOT use html elements and images, only basic markdown and text. DO NOT put lots of text in one slide. Fill each slide with meaningful content. DO NOT write any other text else except what the user tells you to. Divide slides with ---. Put very little text in each slide."
        presentation_start = (
            f"---\nmarp: true\ntheme: {theme}\n_class: lead\n---\n\n# {title}\n"
        )
        presentation_start += f"by {author}\n\n---\n" if author else "\n---\n"

        client = Client("huggingface-projects/llama-2-13b-chat")

        # Generate first part
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

        # Add presentation start to the first part
        first_part = presentation_start + "---".join(
            first_part.split(
                f"Sure! Here is a long presentation on the topic {title}:"
            )[-1].split("---")[:-2:]
        )

        # Change the system prompt so it knows it must continue from
        # where it left.
        system_prompt = "You should continue adding new slides to the presentation."

        # Generate the second part
        print("Generating the second part...")
        second_part = client.predict(
            first_part
            + '\nContinue adding slides from here. Start your response with "Here is the presentation continuation:\n---\n\n## <next slide heading here>\n..."',  # str  in 'Message' Textbox component
            system_prompt,  # str  in 'System prompt' Textbox component
            2048,  # float (numeric value between 1 and 2048) in 'Max new tokens' Slider component
            0.1,  # float (numeric value between 0.1 and 4.0) in 'Temperature' Slider component
            0.05,  # float (numeric value between 0.05 and 1.0) in 'Top-p (nucleus sampling)' Slider component
            1,  # float (numeric value between 1 and 1000) in 'Top-k' Slider component
            1,  # float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
            api_name="/chat",
        )

        # Remove the setup phrase and prettify
        second_part = (
            "\n---\n"
            + second_part.split("Here is the presentation continuation:\n")[-1]
        )

        print(f"{first_part=}")
        print(f"{second_part=}")

        # Get result by adding the generated parts and prettifying
        # the markdown.
        result = (
            (first_part + second_part)
            .replace("---\n---", "---\n")
            .replace("---\n\n---", "---\n")
        )

        return first_part + second_part

    def _process_markdown(self, presentation_content: str, file_format: str) -> None:
        """
        Provided presentation content in Marp format, generates a file in the
        needed format and saves it as `presentation.<format>` in the project directory.

        Args:
            presentation_content: Markdown of the future presentation.
            file_format: Format of the output file.
        """

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
        """
        Generates a Marp presentation with the given title, author and theme, and saves it as a file in the specified format.

        This method first generates the presentation content in markdown format using the `_generate_presentation_content` method. Then, it processes the markdown content into the desired file format using the `_process_markdown` method.

        Args:
            file_format: Format of the output file. This should be a format that Marp can convert to (e.g., 'pdf', 'pptx').
            title: Title of the presentation.
            author: Author of the presentation. Defaults to an empty string.
            theme: Theme of the presentation. Defaults to "default".

        Returns:
            None. Presentation is saved as `presentation.<format>` in the project directory.
        """
        generated_content = self._generate_presentation_content(title, author, theme)
        self._process_markdown(generated_content, file_format)
