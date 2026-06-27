# Virtual Bazaar Management Software (VBMS)

A robust, menu-driven command-line terminal application built in Python designed to manage online store inventories, monitor stock levels, record processing metrics, and track basic internal administrative operations securely.

---

## Key Features

- **Administrative Validation**: Simple onboarding sequence mapping terminal sessions to individual operators via Employee Identification inputs.
- **Dynamic Multi-Currency Support**: Native handling for multi-regional systems including Indian Rupee (₹), US Dollar ($), Euro (€), and UAE Dirham (د.إ).
- **CRUD Operations**: Complete capability to create, read, update, and delete individual store stock allocations seamlessly.
- **Binary Persistence Engine**: Uses Python's native `pickle` standard serialization layer to securely save inventory state arrays across computational context refreshes.

---

## Project Structure

```text
virtual-bazaar-management/
├── .gitignore        # Prevents committing localized database tracking files
├── README.md         # Architecture roadmap and technical documentation
├── requirements.txt  # Project dependency manifest
├── docs/
│   └── sample_output.txt # Verified runtime terminal execution traces
└── src/
    └── main.py       # Core application engine containing computational logic


# Setup & Local Execution

##Prerequisites
Python 3.8 or higher installed on your host system environment.

Run the Application
Clone this repository locally.

Navigate into the root folder using your terminal window:

##Bash
cd virtual-bazaar-management
Run the engine wrapper file:

##Bash
python src/main.py

