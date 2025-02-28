# Password Strength Checker

## Overview

This **Password Strength Checker** is a Python-based graphical user interface (GUI) application that allows users to check the strength of their passwords. The tool uses various password strength rules to evaluate the security of a password, providing visual feedback on its strength, and offering tips on how to improve it.

### Features:
- **Password Generation**: Automatically generates random secure passwords.
- **Strength Analysis**: Checks the strength of a manually entered password based on common password security rules.
- **Real-Time Feedback**: Displays password strength using a progress bar and an animated GIF to indicate whether the password is weak, medium, or strong.
- **Password Tips**: Provides helpful tips and guidelines for creating strong passwords.
- **Visual Feedback**: Uses GIFs and progress bars to provide intuitive, real-time feedback on password strength.


## Requirements

- Python 3.x
- Tkinter (for the GUI)
- Pillow (for GIF support)
- PIL (for image processing)

To install the required libraries, you can use pip:

```bash
pip install pillow
```

## Installation

1. **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/yourusername/password-strength-checker.git
    ```

2. **Navigate to the project folder**:
    ```bash
    cd password-strength-checker
    ```

3. **Run the app**:
    ```bash
    python password_checker.py
    ```

## How It Works

1. **Password Generation**: When the "Generate Password" button is clicked, a random, strong password is generated and displayed in the input field. The password's strength is then automatically checked.
   
2. **Manual Password Check**: You can manually enter a password into the input field and click the "Check Password" button to evaluate its strength.
   
3. **Password Strength Check**: The app uses the following rules to determine password strength:
    - Password length must be at least 12 characters.
    - Must include at least one uppercase letter, one lowercase letter, one digit, and one special character.
    - The password must not contain common dictionary words or personal information.
    - Repeated or sequential characters are not allowed.

4. **Feedback**: The progress bar and a strength label show the strength level (Weak, Medium, or Strong). GIFs are displayed to visualize the strength level:
    - **Weak Password**: Red color with a weak password GIF.
    - **Medium Password**: Yellow color with a loading GIF.
    - **Strong Password**: Green color with a strong password GIF.

## Features in Detail

### 1. **Password Generation**
   - Automatically generates a random password using a combination of uppercase, lowercase letters, digits, and special characters.
   - Can be customized to generate passwords of different lengths.

### 2. **Password Strength Evaluation**
   - The strength of a password is evaluated based on:
     - Minimum length of 12 characters.
     - Inclusion of uppercase letters, lowercase letters, digits, and special characters.
     - No common dictionary words or personal information.
     - Avoids repetitive or sequential characters.

### 3. **User Interface**
   - Built using **Tkinter** for a simple and user-friendly GUI.
   - Displays feedback in the form of a progress bar and strength labels.
   - Shows animated GIFs to visually communicate password strength.

### 4. **Password Tips**
   - Displays guidelines for creating a secure password, such as:
     - Using at least 12 characters.
     - Mixing uppercase and lowercase letters, numbers, and special characters.
     - Avoiding common words and personal information.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Any improvements, bug fixes, or additional features are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Tkinter for the graphical user interface.
- Pillow for GIF and image processing.
- Regular expressions used for password checks.

## Contact

For any questions or suggestions, feel free to reach out.

GitHub: [github.com/anubhavmohandas](https://github.com/anubhavmohandas)

---

Happy password strengthening! 🔒🛡️
```

### Key Highlights of the README:

1. **Overview**: A brief explanation of what the app does.
2. **Requirements & Installation**: Clear instructions for setting up the app.
3. **How It Works**: Details about how the password generation and strength checking work.
4. **Features**: A breakdown of the features and functionality of the app.
5. **Contributing**: Instructions for contributing to the project.
6. **License**: Licensing details (this uses the MIT License, but feel free to update it based on your preferences).
7. **Contact**: A section for users to contact you for questions or suggestions.
