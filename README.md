# Meeting and Mail Crew

![flow](https://github.com/user-attachments/assets/723e38e5-5580-464f-ba44-fdefc39f5e6e)




## Overview

This project aims to automate the process of generating meeting minutes, summarizing key discussions, and creating action plans. It utilizes a combination of AI agents and tools to analyze audio recordings, extract relevant information, and generate concise output.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/m_o_m/config/agents.yaml` to define your agents
- Modify `src/m_o_m/config/tasks.yaml` to define your tasks
- Modify `src/m_o_m/crew.py` to add your own logic, tools and specific args
- Modify `src/m_o_m/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the M-O-M Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Tools and Technologies

* CrewAI
* LangChain
* Ollama
* Llama 8b
* Whisper Turbo
* Gmail API

## Benefits

* **Time-saving:** Automates the manual process of writing meeting minutes.
* **Accuracy:** Ensures accurate and comprehensive meeting summaries.
* **Actionable Insights:** Provides clear action plans with timelines and responsibilities.
* **Improved Communication:** Facilitates effective communication and follow-up.

## Support

For support, questions, or feedback regarding the {{crew_name}} Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
