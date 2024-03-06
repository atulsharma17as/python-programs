# import request module
import requests
def datas(city,appid):
    # enter the url
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}"
    # request data from the url
    request = requests.get(url)
    #Check the status code for api connectivity
    if request.status_code == 200:
        #convert data to json and return data
        data = request.json()

        return data
    else:
        print(f'no connection {request.status_code} ')


if __name__ == '__main__':
    api_key="641e1344d9735a64b3a6fd33d61caafa"
    city_name =input('Enter the city')
    weather_data = datas(city_name,api_key)
    print(weather_data)

    temp=weather_data['main']['temp']
    descript=weather_data['weather'][0]['description']
    print(f'city is {city_name}')
    print(f'description is {descript}')
    print(f'tmperatur is {temp}')

