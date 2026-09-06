# AirBnB Clone

## Description

The AirBnB Clone project is a full-stack web application inspired by the AirBnB platform.

The goal of this project is to build a complete web application step by step, starting with a command interpreter that allows users to create, retrieve, update, and destroy objects.

The project focuses on understanding object-oriented programming, data serialization, persistence, and the development of a command-line interface.

## The Command Interpreter

The command interpreter is a command-line interface (CLI) that allows users to interact with the application's objects.

It will allow users to:

- Create new objects
- Retrieve objects
- Display objects
- Update object attributes
- Destroy objects
- Display information about objects
- Quit the command interpreter

### How to Start It

Once the command interpreter is implemented, it can be started from the project directory using:

    ./console.py

It can also be started using Python:

    python3 console.py

### How to Use It

When the command interpreter starts, it displays the following prompt:

    (hbnb)

Commands can then be entered at the prompt.

For example:

    (hbnb) help

To exit the command interpreter:

    (hbnb) quit

The interpreter can also be exited using:

    (hbnb) EOF

### Examples

Display the available commands:

    (hbnb) help

Create a new BaseModel instance:

    (hbnb) create BaseModel

Display an existing object:

    (hbnb) show BaseModel 1234-5678

Update an object:

    (hbnb) update BaseModel 1234-5678 name "John"

Destroy an object:

    (hbnb) destroy BaseModel 1234-5678

Display all objects:

    (hbnb) all

Display all objects of a specific class:

    (hbnb) all BaseModel

### Non-Interactive Mode

Commands can also be passed to the command interpreter using standard input.

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
- `AUTHORS` - list of contributors

## Authors

See the `AUTHORS` file for the list of contributors to the repository.
