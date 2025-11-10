# CLI To-Do List

A lightweight command-line task manager written in Python. The app stores tasks in a local `tasks.json` file and exposes commands for creating, listing, updating, and deleting items directly from the terminal.

## Features

- Add new tasks with optional descriptions and due dates.
- List tasks with optional filters (`--completed`, `--pending`) and sorting (`--sort date`, `--sort created`).
- Mark tasks as completed.
- Edit existing task details.
- Delete individual tasks (with optional `--force` flag) or clear the entire list.
- Search for tasks by keyword across titles and descriptions.

## Requirements

- Python 3.8 or newer (tested on Python 3.10).
- No third-party dependencies.

## Getting Started

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. (Optional) Create and activate a virtual environment.
4. Run the script with `python to_do.py <command> [options]`.

The script will create `tasks.json` in the working directory on first use.

## Usage

```bash
python to_do.py add "Buy groceries" --description "Milk, bread, eggs" --due 2025-11-15
python to_do.py list --pending --sort date
python to_do.py done 3
python to_do.py edit 3 --title "Buy groceries and snacks"
python to_do.py delete 2
python to_do.py search groceries
python to_do.py clear --force
```

Run `python to_do.py -h` for the full command and option reference.

## Data Storage

Tasks persist locally in `tasks.json`. You can back up or sync this file to share your task list across machines. Deleting the file resets the task list.

## Notes

- All timestamps use your system time.
- Deleting tasks without `--force` prompts for confirmation in the terminal.
- Some commands (such as `clear` and `delete`) will exit without changes if you do not confirm the prompts.

## Contributing

Issues and pull requests are welcome! Feel free to suggest enhancements, improve error handling, or extend the CLI with new commands.

