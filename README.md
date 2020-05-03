# Darf Generator

A python3 software that links with the stock exchange brokers from brazil and automatic generate the taxes of the stock sales (darf) linking with the government taxes system (receita federal).

To use this library, it is necessary to install the following packages:

- Python 3
- Python automatedweb - <https://github.com/renanleonellocastro/automatedweb>
- PyQt5

## Architecture Concept

The system is divided in four subsystems as following:

- Subsystem 1: Get data from the brokers (stock purchase and sales) using the automatedweb tool.
- Subsystem 2: Develop the taxes rules (calculate the taxes).
- Subsystem 3: Connect with the government taxes system to generate the darf using the automatedweb tool.
- Subsystem 4: Graphical user interface to show the taxes information and to give user the interface to register his brokers accounts and manage the application. This is developed using PyQt5 library.
