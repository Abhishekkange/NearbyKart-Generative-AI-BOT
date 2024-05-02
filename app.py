import google.generativeai as genai
import requests

#utility functions
#GET request
def fetch_data_from_GET(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

#Requird functions are defined here
def getAvailableStore():
    """This function returns a Json Array list of storedetails of each store present in database of NearbyKart App"""
    response = fetch_data_from_GET("http://3.109.186.80:4000/api/v1/storelists")
    return response



genai.configure(api_key='')
model = genai.GenerativeModel(model_name="gemini-pro",tools=[getAvailableStore])
chat = model.start_chat(enable_automatic_function_calling=True)
response = chat.send_message("which stores are present in nearbykart app. Give me the store names ")
print(response.text)