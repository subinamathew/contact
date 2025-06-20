# Contact Manager Agent

This project implements "Olive," a digital assistant acting as a company secretary. Olive's primary role is to help draft professional introduction emails to clients on behalf of a manager.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python**: Version 3.10 or higher (Python 3.12 is used in the provided Dev Container).
*   **UV**: A fast Python package installer and virtual environment manager from Astral.
    To install UV, run:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    For other installation methods, please refer to the [official UV documentation](https://github.com/astral-sh/uv).

## Setup

1.  **Clone the repository (if you haven't already):**
    ```bash
    # git clone <your-repository-url>
    # cd contact
    ```

2.  **Create and activate a virtual environment using UV:**
    Navigate to the project root directory (`/workspaces/contact/` or your local equivalent) and run:
    ```bash
    uv venv
    ```
    This command will create a virtual environment in the `.venv` directory.

    Activate the virtual environment:
    *   On macOS and Linux (bash/zsh):
        ```bash
        source .venv/bin/activate
        ```
    *   On Windows (PowerShell):
        ```powershell
        .venv\Scripts\Activate.ps1
        ```
    *   On Windows (Command Prompt):
        ```batch
        .venv\Scripts\activate.bat
        ```

3.  **Install dependencies:**
    With the virtual environment activated, install the necessary Python packages:
    ```bash
    uv pip install google-adk
    uv pip install -e .
    ```
    *   `google-adk`: The Google Agent Development Kit.
    *   `-e .`: Installs the current project (`contact_manager`) in editable mode.

    *(Note: If `google-adk` is (or will be) listed as a dependency in a `pyproject.toml` file for this project, the `uv pip install -e .` command might be sufficient on its own to install all dependencies, including `google-adk`.)*

## Running the Agent

The project includes a `runme.sh` script to easily start the agent.

1.  **Make the script executable (if you haven't already):**
    ```bash
    chmod +x runme.sh
    ```

2.  **Run the agent:**
    *   **For console/chat mode:**
        ```bash
        ./runme.sh
        ```
        This will start an interactive chat session with Olive in your terminal.

    *   **For web mode:**
        ```bash
        ./runme.sh --web
        ```
        This will serve the agent via a web interface, typically accessible at `http://localhost:8000` (the default port for ADK web service).

## Development Environment

### Dev Container (Recommended for VS Code / GitHub Codespaces)

This project is configured with a Dev Container, which provides a pre-configured, consistent development environment. If you open this project in VS Code with the "Dev Containers" extension installed, or in GitHub Codespaces, the environment will be automatically set up as defined in `.devcontainer/devcontainer.json`.

This includes:
*   Python 3.12.
*   Automatic creation and activation of the `.venv` virtual environment.
*   Installation of all dependencies using `uv pip sync uv.lock` and `uv pip install -e .`.
*   Useful VS Code extensions for Python development, linting (Pylint, Ruff), formatting (Black), and more.

Using the Dev Container is highly recommended for a smooth development experience.