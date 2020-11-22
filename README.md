# sensor-data-assignment
Atria Power - Fullstack Developer coding challenge

## Installing dependencies
- Install dependencies with `pip install -r requirements.txt`
- Install ReactJS with `npm i react`
- Install ReactJS table with `npm i react-table`
- Install ReactJS charts with `npm install --save react-chartjs-2`

## Usage
- Open terminal in the `src/backend` folder.
- Run `python add_fake_data.py` to populate the sensor collection in a MongoDB database with random fake data objects. This needs to be done just once (already done).
- Run `python flask_application.py` and explore the available endpoints on your browser.
- To view frontend, open terminal in `src/frontend/sensor-app/src` and run `npm start`

## Endpoints available
| Endpoint | Description | Example | Type | isIdempotent |
|--|--|--|--|--|
| `/` | Home page | Self explanatory | GET | True |
| `/sensor/records` | Gets all sensor records | Self explanatory | GET | True |
| `/sensor/records/filter?sensorType=<str>&minReading=<float>&maxReading=<float>&startDate=<str>&endDate=<str>` | Gets sensor records based on certain filters. All filter parameters are optional | `/sensor/records/filter?sensorType=temperature&minReading=23.4&maxReading=29.7&startDate=01-01-2010&endDate=20-11-2019` | GET | True |
| `/sensor/record?_id=<str>` | Gets one sensor record by ID  | `/sensor/record?_id=ABCD123` | GET | True |
| `/sensor/record/add?reading=<float>&sensorType=<str>` | Adds one sensor record | `/sensor/record/add?reading=16.754&sensorType=temperature` | POST | False |
| `/sensor/record/delete?_id=<str>` | Deletes one sensor record by ID | `/sensor/record/delete?_id=ABCD123` | DELETE | True |
| `/sensor/stats?startDate=<dd-mm-yyyy>&endDate=<dd-mm-yyyy>` | Gets max/min/average/median stats of readings of sensor records present between certain date-range | `/sensor/stats?startDate=15-03-2014&endDate=20-11-2020` | GET | True |

## Notes
- I've used MongoDB to store a collection containing sensor-related records (randomly generated fake data).
- Any CRUD operations performed (via the API) will be reflected in the database.
- `src/frontend/sensor-app/src/data` has a JSON file containing the latest snapshot of the collection containing sensor-related records. This file gets over-written every time there's a change in the database. I've used this local JSON file for the frontend table and line-chart.
- I've created the frontend table and line-chart with ReactJS.
- I've included screenshots of the working API and the working frontend in the `screenshots` folder.