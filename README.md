
# FossAlgo

**FossAlgo** is a website designed to help Foss community members keep track of competitive programming (CP) contests, user profiles, and standings within the community.

## Table of Contents

- [About the Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About the Project

FossAlgo offers features like:
- Tracking ongoing and upcoming CP contests
- Maintaining user profiles
- Viewing community standings and rankings
- Dashboard analytics for users and administrators

## Getting Started

To set up FossAlgo on your local machine for development or testing, follow the instructions below.

### Prerequisites

Ensure the following software is installed:
- Python 3.x
- Django
- MySQL
- Other tools: `pip`, `virtualenv`

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/praptisharma28/FossAlgo.git
   cd FossAlgo
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```


3. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

### Running the Application

1. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```


2. **Access the Application**

   Open your browser and go to `http://127.0.0.1:8000` to view the application.

## Usage

After setting up and running the application:
- **Log in** as the superuser to access administrative features.
- **Add/Manage CP contests**, user profiles, and monitor standings.
- **User Dashboard** for members to track their performance and view contest history.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

> **Note**: Ensure the `venv` directory is included in the `.gitignore` file and not committed.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contact

For further information, questions, or contributions:
- Project Repository: [FossAlgo on GitHub](https://github.com/praptisharma28/FossAlgo)

- **Github** : https://github.com/praptisharma28/


7. Access the project in your browser at `http://127.0.0.1:8000`
