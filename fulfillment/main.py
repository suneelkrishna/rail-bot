#import functions_framework
import requests
import time
from google.cloud import functions
def train_schedule_webhook(request):
    """
    print(f"time1:{time.time()}") 
    url = "https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations"
    querystring = {"fromStationCode":"","toStationCode":"","dateOfJourney":""}
    headers = {
      "x-rapidapi-key": "",
      "x-rapidapi-host": "irctc1.p.rapidapi.com"
    }

    print("hi")
    print(f"time2:{time.time()}")
    request_json = request.get_json()
    source_station_code = request_json.get("queryResult", {}).get("parameters", {}).get("Source_Station_code")
    destination_station_code = request_json.get("queryResult", {}).get("parameters", {}).get("Destination_Station_Code")
    journey_date = request_json.get("queryResult", {}).get("parameters", {}).get("date","")
    querystring["fromStationCode"] = source_station_code 
    querystring["toStationCode"] = destination_station_code
    querystring["dateOfJourney"] = journey_date
    print(f"time3:{time.time()}")
    response = requests.get(url, headers=headers, params=querystring)
    print(f"time4:{time.time()}")
    
    if response.status_code == 200:
      dt = response.json()
      trains = dt.get("data", [])
      print(f"data: {trains}")
      train_info = []
      for train in trains:
          train_info.append({"text": {"text": [f"Train number: {train.get('train_number')}, Train Name: {train.get('train_name')}, Departure: {train.get('from_std')}"]}})
      print(f"time5:{time.time()}")
      return {"fulfillmentText": "Train schedules from {} to {}:".format(source_station_code, destination_station_code), "fulfillmentMessages": train_info}
    else:
      return {"message": "Failed to retrieve train schedule information."}
    
    response = {
        "fulfillmentText": "Hi there test spot 1!",
        "fulfillmentMessages": [
            {
                "text": {
                    "text": ["Hi there test spot 2!"]
                }
            },
            {
                "text": {
                    "text": ["Hi there test spot 3!"]
                }
            }
        ]
    }
    return response

    print(f"time1:{time.time()}")
    url = "https://irctc1.p.rapidapi.com/api/v1/checkSeatAvailability"
    querystring = {"classType":"3A","fromStationCode":"CNB","quota":"GN","toStationCode":"NDLS","trainNo":"12451","date":"2024-10-16"}
    headers = {
      "x-rapidapi-key": "057abdc900msh13d80d1278bff0dp11230fjsn851f4f95c94b",
      "x-rapidapi-host": "irctc1.p.rapidapi.com"
    }
    print(f"time2:{time.time()}")
    response = requests.get(url, headers=headers, params=querystring)
    print(f"time3:{time.time()}")
    print(response.json())

    """
    url = "https://irctc1.p.rapidapi.com/api/v1/checkSeatAvailability"
    querystring = {"classType":"", "fromStationCode":"", "quota":"", "toStationCode":"", "trainNo":"", "date":""}
    headers = {
      "x-rapidapi-key": "<create and use your own key from https://rapidapi.com/>",
      "x-rapidapi-host": "irctc1.p.rapidapi.com"
    }
    request_json = request.get_json()
    source_station_code = request_json.get("queryResult", {}).get("parameters", {}).get("source_station_code")
    destination_station_code = request_json.get("queryResult", {}).get("parameters", {}).get("destination_station_code")
    journey_date = request_json.get("queryResult", {}).get("parameters", {}).get("date","")
    quota = request_json.get("queryResult", {}).get("parameters", {}).get("quota","")
    class_type = request_json.get("queryResult", {}).get("parameters", {}).get("class_type","")
    train_no = request_json.get("queryResult", {}).get("parameters", {}).get("train_no","")
    
    querystring["fromStationCode"] = source_station_code 
    querystring["toStationCode"] = destination_station_code
    querystring["date"] = journey_date
    querystring["quota"] = quota
    querystring["classType"] = class_type
    querystring["trainNo"] = train_no
    
    print(f"time3:{time.time()}")
    print(querystring)
    response = requests.get(url, headers=headers, params=querystring)
    print(f"time4:{time.time()}")
    print(response)
    
    if response.status_code == 200:
      dt = response.json()
      print(f"response: {dt}")
      # Extract train details from the API response (replace with your API's data structure)
      availability = dt.get("data", [])
      print(f"data: {availability}")
      availability_info = []
      for day in availability:
          availability_info.append({"text": {"text": [f"Date: {day.get('date')}, Status: {day.get('current_status')}, Fare: {day.get('total_fare')}, Confirm Prob Percent: {day.get('confirm_probability_percent')}"]}})
      #print(f"fulfillmentMessages: {availability_info}")
      print(f"time5:{time.time()}")
      if dt.get("status") == False:
        msg = []
        print(dt.get('message'))
        msg.append({"text": {"text": [f"Message: {dt.get('message')}"]}})
        return {"fulfillmentText": "We could not fulfill the request because of the following error:","fulfillmentMessages": msg }
        #return {"message": dt.get('message')}
      return {"fulfillmentText": "Seat Availability from {} to {} on date {} in class {} under {} quota:".format(source_station_code, destination_station_code, journey_date, class_type, quota), "fulfillmentMessages": availability_info}
    else:
      return {"message": "Failed to retrieve train schedule information."}
