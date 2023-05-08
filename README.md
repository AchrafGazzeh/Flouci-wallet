# Flouci-wallet

**Please note that this project is not affiliated with Flouci, the company. This project was created as part of an internship application to Flouci. The project is intended to showcase my skills and experience in software development.**


![image](https://user-images.githubusercontent.com/23439878/236804031-34b30a97-6fe9-45ba-bded-1ef6b3c21821.png)

## Installation

1. Clone the repository:

```https://github.com/AchrafGazzeh/Flouci-wallet```

2. Run the migrations:

```python manage.py migrate```

3. Start the development server:

```python manage.py runserver```

# Purpose

This app allows users to manage their finances by tracking their income and expenses. Users can sign in and sign out of the app, and add reports to their wallet to record their income or expenses. Reports are categorized based on the type of transaction, and users can view all of their wallet records to see a detailed history of their finances. The app also includes a dashboard that displays key information such as the user's cash balance, most spending categories, and how much they spent last month. This app is designed to help users stay on top of their finances and make informed decisions about their spending.

## Routes

The following routes are available in this app:

- `/register/`: Allows users to register for an account.
- `/login/`: Allows users to log in to their account.
- `/logout/`: Allows users to log out of their account.
- `/`: The landing page of the app.
- `/records/`: Allows users to view all of their wallet records.
- `/reports/`: Allows users to add new reports to their wallet.
- `/dashboard/`: Displays a dashboard with key financial information.
- `/reports/delete/<str:delete_id>/`: Allows users to delete a specific report from their wallet.
- `/api/linechart/data/`: Provides data for a line chart in the dashboard.
- `/api/barchart/data/`: Provides data for a bar chart in the dashboard.
- `/api_schema/`: Provides the API schema in JSON format.
- `/docs/`: Displays the Swagger UI for exploring the API.

To access any of these routes, simply append the route to the base URL of the app. For example, to access the login page, go to `http://localhost:8000/login/`.

## Swagger API

This app includes a Swagger API that provides documentation for the REST API. To access the Swagger API, go to `/docs/`. This will display the Swagger UI, which provides an interactive interface for exploring the API. The Swagger API includes information about the available endpoints, request and response formats, and authentication requirements. You can also access the API schema directly by going to `/api_schema/`. This will display the API schema in JSON format, which can be useful for developers who are integrating with the API or for anyone who wants to learn more about how the app works.

## Tests

This app includes tests to ensure that the models and views are working correctly. One example of a test is the `RecordModelTest` class, which tests the `RecordModel` model. This class includes two test methods: `test_record_model_str_method` and `test_record_model_fields`. The `test_record_model_str_method` method tests the `__str__` method of the `RecordModel` model to ensure that it returns the expected string representation of the model. The `test_record_model_fields` method tests the fields of the `RecordModel` model to ensure that they are set correctly. These tests help to ensure that the app is working as expected and that any changes made to the code do not introduce new bugs or issues.

## Records page

The records page is where users can add new financial records to their wallet. The page includes a form with several input fields, including a dropdown menu to select the type of financial record (income or expense), a dropdown menu to select the category and sub-category of the record, a dropdown menu to select the payment type, an input field to enter the amount, and date and time pickers to select the date and time of the record. Once the user has filled out the form, they can click the "Add Record" button to submit the record to their wallet. This page provides a simple and intuitive way for users to add new financial records to their wallet.


![image](https://user-images.githubusercontent.com/23439878/236805584-7c1363cb-e312-4c94-ae8a-2827113f0d40.png)
