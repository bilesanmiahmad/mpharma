# diagnosis app
This is an app that can be used to store diagnosis codes for various diseases. A user can add new codes, view saved codes, update saved codes and delete saved codes. The diagnosis codes in the fixtures are ICD-10 codes.  

## Instructions on setting the application up.
1. Clone the application to your local machine.
2. From your terminal, navigate to the application folder.
3. Run `docker-compose down` in your terminal
3. Run `docker-compose build` in your terminal
4. Run `docker-compose up` in your terminal

## Running the application
1. You can use Postman to test the endpoints when the application is up and running.
2. The api documentation can be found [127.0.0.1:8000/docs](127.0.0.1:8000/docs)
3. Creating a diagnosis category is required to create a diagnosis record.
4. One diagnosis category can have many diagnosis records as long as the record codes are not the same. 
5. If you try to create a diagnosis record with same category code and record code, you would be asked to change the code. 

## Testing the application
1. Run `docker-compose run web python manage.py test diagnosis`. This would run all tests in the application.

## Fixtures
1. Run `docker-compose run web python manage.py loaddata category` to load fixtures for the categories.
2. Run `docker-compose run web python manage.py loaddata category` to load fixtures for the diagnosis.