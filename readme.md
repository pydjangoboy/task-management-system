# TaskManager

TaskManager is a Django-based web application for managing tasks. It also integrates with a FastAPI API to fetch task details.

## Features

- List all tasks
- View details of a task
- Create a new task
- Edit an existing task
- Delete a task
- Search for tasks
- Fetch task details from a FastAPI API

## Setup and Installation

1. Clone the repository:
    ```
    git clone https://github.com/pydjangoboy/TaskManager.git
    ```

2. Navigate to the project directory:
    ```
    cd TaskManager
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the Django migrations:
    ```
    python manage.py migrate
    ```

5. Start the Django server:
    ```
    python manage.py runserver
    ```

6. In a new terminal window, navigate to the FastAPI application directory (replace `path_to_fastapi_app` with the actual path):

    ```
    cd path_to_fastapi_app
    ```

7. Install the FastAPI application dependencies (if any):

    ```
    pip install -r requirements.txt
    ```

8. Start the FastAPI server on port 8081:

    ```
     uvicorn Tasks.fastapi:app --host 0.0.0.0 --port 8081
    ```

Now, you can navigate to `http://127.0.0.1:8000/` in your browser to view the Django application and to `http://127.0.0.1:8081/` to view the FastAPI application.

## Usage

- To view all tasks, navigate to the home page.
- To view details of a task, click on the task title.
- To create a new task, click on the 'New Task' button.
- To edit an existing task, click on the 'Edit' button on the task detail page.
- To delete a task, click on the 'Delete' button on the task detail page.
- To search for a task, use the search bar at the top of the page.
- To view FastAPI task details, click on the task title in the task list.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.