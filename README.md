# Compound Interest Calculator - Flask Application

This is a simple web application built with Flask that calculates compound interest based on user-provided inputs. It demonstrates best practices for Flask development, including template inheritance, static file management, error handling, and input validation.

## Features

*   **Compound Interest Calculation:** Accurately calculates the future value of an investment and the total interest earned, given a principal amount, annual interest rate, time period, and compounding frequency.
*   **User-Friendly Interface:** Provides a clean and intuitive web form for entering the necessary parameters.
*   **Error Handling:** Gracefully handles invalid user input (e.g., non-numeric values) and displays helpful error messages.
*   **Input Validation:** Includes both server-side (Flask) and client-side (JavaScript) validation to ensure data integrity.
*   **Clear Results Display:** Presents the calculated results (total amount and total interest) in an easily understandable format.
*   **Template Inheritance:** Uses a base template (`layout.html`) to reduce code duplication and maintain a consistent look and feel across different pages.
*   **Static Files:** Manages CSS and JavaScript files using Flask's `static` folder and `url_for` for proper URL generation.
*   **Responsive Design (Basic):** The CSS provides a basic responsive layout that works on various screen sizes.

## Project Structure

interest_calculator/
├── app.py             (Flask application logic)
├── templates/
│   ├── layout.html    (Base template for all pages)
│   ├── index.html     (Input form page)
│   └── result.html    (Results display page)
└── static/
├── css/
│   └── style.css  (CSS styles)
└── js/
└── script.js  (JavaScript for client-side validation - optional)


## Requirements

*   Python 3.6+
*   Flask

## Installation and Setup

1.  **Clone the Repository (Optional):** If you have the code on a repository (like GitHub), clone it:

    ```bash
    git clone <repository_url>
    cd interest_calculator
    ```
    If you copied and pasted the code directly, you can skip this step.

2.  **Create a Virtual Environment (Recommended):**  It's highly recommended to create a virtual environment to isolate your project's dependencies.  You can do this with:

    ```bash
    python3 -m venv venv
    ```
    Then activate it:

    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Install Flask:**

    ```bash
    pip install flask
    ```

## Running the Application

1.  **Navigate to the Project Directory:** Make sure you are in the `interest_calculator` directory (where `app.py` is located).  If you created a virtual environment, make sure it's activated.

2.  **Run the Flask App:**

    ```bash
    python app.py
    ```

3.  **Access in Your Browser:** Open a web browser and go to `http://127.0.0.1:5000/` (or the address that is displayed in your terminal).

## Usage

1.  **Enter Input Values:** On the main page (`index.html`), fill in the following fields:
    *   **Principal Amount:** The initial investment amount.
    *   **Annual Interest Rate (%):**  The annual interest rate, expressed as a percentage (e.g., 5 for 5%).
    *   **Time (Years):** The investment period in years.
    *   **Compounding Frequency:** How many times per year the interest is compounded (e.g., Annually, Semi-Annually, Quarterly, Monthly, Daily).

2.  **Click "Calculate":**  Submit the form.

3.  **View Results:** The results page (`result.html`) will display the calculated total amount and total interest earned, along with a summary of your input values.

4.  **Calculate Again:**  Click the "Calculate Again" link to return to the input form and perform another calculation.

## Customization

*   **Styling:** Modify `static/css/style.css` to change the appearance of the application.
*   **JavaScript:** Add or modify `static/js/script.js` for additional client-side functionality (e.g., more sophisticated input validation, dynamic updates).
*   **Templates:** Change the HTML structure and content within the `templates` directory.
*   **Functionality:** Extend the `app.py` file to add new features, such as:
    *   Support for different interest calculation methods (e.g., simple interest).
    *   Saving calculation history.
    *   Integration with external APIs.
    * User accounts and data persistence
