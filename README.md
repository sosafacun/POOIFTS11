# POOIFTS11
Final Project for OOP at IFTS N°11

## Functional Requirements

- CMD execution
- No web frameworks
- No DBs.
- Data must be saved in a .csv file
- Read the data from the .csv file and turn it in to a dictionary
- Must use OOP and *at least* the following classes:
    - Client
    - Appointment
    - Hairdresser or Appointment. This will manage all the main operations.
- The system must have an interactive main menu with options like:
    - Register new client
    - Schedule new appointment
    - Show all scheduled appointments
    - Re-schedule appointments
    - Save / Load data
    - Exit app

### How to handle data and data files

- Everytime data is being saved, it myst save the info into the dictionary and then save it to the csv
- The app must be able to convert from .csv to dict and from dict to .csv to achieve the feeling of a persistent database
- Whenever the app starts, it must load the .csv file automatically.

## Suggestions and personal goals
- Cannot make appointments at the same time for the same employee.
- Allow client, date or employee filtering.
- Handle exceptions.
- Use DateTime to handle schedules.
- Ask the user to confirm an old or new appointment. Once confirmed, the system has to save that date to the .csv, and load it.
- Whenever the user goes exits or cancels an operation, they have to confirm that there are unsaved changes that are going to be lost; as each time the main menu loads the .csv is read again to mantain data integrity.
- Does it have to be Python?
- Register the DOB of both clients and employees.
    - Employees' DOB will be used to grant them a full-pay free day.
    - Clients' DOB will be used to grant them a free haircut, available for the next 7 days (weekends included).