import requests
api_key = "<your API KEY>"
base_url = "https://api.railwayapi.com/v2/pnr-status/pnr/"
pnr_number = str(input("enter the PNR number"))
# you'll get traceback error if you don't enter your api key
complete_url = base_url + pnr_number + "/apikey/" + api_key + "/"
response_ob = requests.get(complete_url)
result = response_ob.json()
if result["response_code"] == 200:
    train_name = result["train"]["name"]
    train_number = result["train"]["number"]
    from_station = result["from_station"]["name"]
    to_station = result["to_station"]["name"]
    boarding_point = result["boarding_point"]["name"]
    reservation_unto = result["reservation_unto"]["name"]
    pnr_num = result["pnr"]
    date_of_journey = result["doj"]
    total_passengers = result["total_passengers"]
    passengers_list = result["passengers"]
    chart_prepared = result["chart_prepared"]
    print(" train name : " + str(train_name)
          + "\n train number : " + str(train_number)
          + "\n from station : " + str(from_station)
          + "\n to station : " + str(to_station)
          + "\n boarding point : " + str(boarding_point)
          + "\n reservation unto : " + str(reservation_unto)
          + "\n pnr number : " + str(pnr_num)
          + "\n date of journey : " + str(date_of_journey)
          + "\n total no. of passengers: " + str(total_passengers)
          + "\n chart prepared : " + str(chart_prepared))
    # for multiple passengers against same PNR
    for passenger in passengers_list:
        passenger_num = passenger["no"]
        current_status = passenger["current_status"]
        booking_status = passenger["booking_status"]
        # print following values
        print(" passenger number : " + str(passenger_num)
              + "\n current status : " + str(current_status)
              + "\n booking_status : " + str(booking_status))
else:
    print("Record Not Found")
