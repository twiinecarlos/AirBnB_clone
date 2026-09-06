# AirBnB Clone

## Description

The AirBnB Clone project is a full-stack web application inspired by the AirBnB platform.

The goal of this project is to build a complete web application step by step, starting with a command interpreter that allows users to create, retrieve, update, and destroy objects.

The project focuses on understanding object-oriented programming, data serialization, persistence, and the development of a command-line interface.

## Command Interpreter

The command interpreter is a command-line interface (CLI) that allows users to interact with the application's objects.

Through the command interpreter, users can:

- Create new objects
- Display objects
- Update object attributes
- Destroy objects
- Display information about objects
- Quit the command interpreter

### How to Start It

Clone the repository:

    git clone https://github.com/<your-username>/AirBnB_clone.git

Move into the project directory:

    cd AirBnB_clone

Start the command interpreter:

    ./console.py

You can also start it using Python:

    python3 console.py

### How to Use It

Once the command interpreter starts, the following prompt is displayed:

    (hbnb)

You can enter commands at the prompt.

For example:

    (hbnb) help

To exit the command interpreter:

    (hbnb) quit

You can also use:

    (hbnb) EOF

### Available Commands

#### `help`

Displays available commands.

Example:

    (hbnb) help

#### `quit`

Exits the command interpreter.

Example:

    (hbnb) quit

#### `create`

Creates a new instance of a class.

Example:

    (hbnb) create BaseModel

The command returns the ID of the newly created object.

#### `show`

Displays the string representation of an instance based on its class and ID.

Example:

    (hbnb) show BaseModel 1234-5678

#### `destroy`

Deletes an instance based on its class and ID.

Example:

    (hbnb) destroy BaseModel 1234-5678

#### `all`

Displays all instances, or all instances of a specified class.

Examples:

    (hbnb) all

    (hbnb) all BaseModel

#### `update`

Updates an instance by adding or changing an attribute.

Example:

    (hbnb) update BaseModel 1234-5678 name "John"

### Non-Interactive Mode

Commands can also be executed by piping input into the command interpreter.

Example:

    echo "help" | ./console.py

Another example:

    echo "quit" | ./console.py

## Project Structure

The project will be developed progressively and may contain components such as:

- `console.py` - command interpreter
- `models/` - application models
- `tests/` - unit tests
- `README.md` - project documentation
- `AUTHORS` - contributors to the repository

## Authors

See the `AUTHORS` file for the list of contributors.
