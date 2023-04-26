
import requests
import openai

#Accessing Power BI Data
def query_power_bi_data(api_url = "https://api.powerbi.com/v1.0/myorg/groups/032427de-5cdb-419e-9906-7c673d7765fc/datasets/e7dcd9e2-5ffe-420e-8268-5c7091c402ff/executeQueries", 
                        headers = {
            "Content-Type":"application/json",
            "Authorization":f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvYTc3ZDY5M2ItODE3Ny00NzI4LWI3ZjMtODJkZThiOGFhZWRkLyIsImlhdCI6MTY4MjQ5MDMyNSwibmJmIjoxNjgyNDkwMzI1LCJleHAiOjE2ODI0OTQ1NDAsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84VEFBQUFLSzU1NXZKZEZUZXRSS1gwMGJaQytPZy80Q294cDI0UUVJTXc2ZTczeVdYalcvRkhrb3ZYaUJ6ZkhJRUczNzJzby9mVjNNeDBhK291RkR0SW4zUmRkN2xmNXJlNjN5LzdCampqaktDckhWWT0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiMThmYmNhMTYtMjIyNC00NWY2LTg1YjAtZjdiZjJiMzliM2YzIiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJDaGFrcmFib3J0eSIsImdpdmVuX25hbWUiOiJBbmluZHlhIiwiaXBhZGRyIjoiMy42LjE5LjExNyIsIm5hbWUiOiJBbmluZHlhIENoYWtyYWJvcnR5Iiwib2lkIjoiYjIzOGI1MWMtYTA0Yy00YWU4LWE4NmItNTEwMjNiMThjNTQyIiwicHVpZCI6IjEwMDMyMDAyOTlBNDNEMDIiLCJyaCI6IjAuQVZZQU8ybDlwM2VCS0VlMzg0TGVpNHF1M1FrQUFBQUFBQUFBd0FBQUFBQUFBQUNmQU5BLiIsInNjcCI6IkFwcC5SZWFkLkFsbCBDYXBhY2l0eS5SZWFkLkFsbCBDYXBhY2l0eS5SZWFkV3JpdGUuQWxsIENvbnRlbnQuQ3JlYXRlIERhc2hib2FyZC5SZWFkLkFsbCBEYXNoYm9hcmQuUmVhZFdyaXRlLkFsbCBEYXRhZmxvdy5SZWFkLkFsbCBEYXRhZmxvdy5SZWFkV3JpdGUuQWxsIERhdGFzZXQuUmVhZC5BbGwgRGF0YXNldC5SZWFkV3JpdGUuQWxsIEdhdGV3YXkuUmVhZC5BbGwgR2F0ZXdheS5SZWFkV3JpdGUuQWxsIFBpcGVsaW5lLkRlcGxveSBQaXBlbGluZS5SZWFkLkFsbCBQaXBlbGluZS5SZWFkV3JpdGUuQWxsIFJlcG9ydC5SZWFkLkFsbCBSZXBvcnQuUmVhZFdyaXRlLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkV3JpdGUuQWxsIFRlbmFudC5SZWFkLkFsbCBUZW5hbnQuUmVhZFdyaXRlLkFsbCBVc2VyU3RhdGUuUmVhZFdyaXRlLkFsbCBXb3Jrc3BhY2UuUmVhZC5BbGwgV29ya3NwYWNlLlJlYWRXcml0ZS5BbGwiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiJyakcwYy12TUZFTHJBbXJ2ODZuRFJTTmNLcXBHZ29OM3FGZHF4SnN6elpVIiwidGlkIjoiYTc3ZDY5M2ItODE3Ny00NzI4LWI3ZjMtODJkZThiOGFhZWRkIiwidW5pcXVlX25hbWUiOiJBbmluZHlhQ2hha3JhYm9ydHlAUHdDVGVzdDAyMy5vbm1pY3Jvc29mdC5jb20iLCJ1cG4iOiJBbmluZHlhQ2hha3JhYm9ydHlAUHdDVGVzdDAyMy5vbm1pY3Jvc29mdC5jb20iLCJ1dGkiOiI3aUhKakkyLWFrU0RDb09SNFFVU0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyI2MmU5MDM5NC02OWY1LTQyMzctOTE5MC0wMTIxNzcxNDVlMTAiLCJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX3BsIjoiZW4ifQ.KxatzcvmZKksQmocxS3Wm3OOpJ86qHozn5aZoAF3mhsYYDvYDIL0X7Xvx3PIhRmByMGuRUiMGS5NGBMFh3u8vtTJaDuu3iXs9fBkAT18dsgyC-I94JCrFa0T_WjwDfGmsOYrlc3NIRpv5_D3mqX-yFNY_PIpTKf4uz23hwFLMw6j1xUDiy7_XGyOIt_cW4aB9BbovQTE32JPzfKOkKtZmUleFH5n0YoxUcqX3vFtxqdZXHo4ASOfqVne_EQ_vi0Oj6SJBTMNy38JpFk0_LKz-PiVvIuEx7sgdcZftaXgc9ewS6NPeJO1JxT0hOI1EnEOjayOtrhOOIuxkKU5UseOEQ"
            }, query = {
  "queries": [
    {
      "query": "EVALUATE VALUES(sample_data)"
    }
  ],
 
  "impersonatedUserName": "anindyachakraborty@pwctest023.onmicrosoft.com"
}):
    response = requests.post(api_url, headers=headers, json=query)
    response.raise_for_status()
    #print(response.json())
    return response.json()



###############################################ChatBot Using OpenAI##################################################################
#Chatbot using OpenAI
openai.api_key = "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"

def chat_with_openai(prompt, model="text-davinci-003"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=500 ,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    print(message)
    return message

##########################Processing User Inputs########################################################################################
# Processing User inputs and generating responses on Power BI Data
def process_user_input(user_input):
    openai_prompt = f"Create a Power BI query for the following user question: {user_input}"
    power_bi_query = chat_with_openai(openai_prompt)

    power_bi_data = query_power_bi_data(api_url = "https://api.powerbi.com/v1.0/myorg/groups/032427de-5cdb-419e-9906-7c673d7765fc/datasets/e7dcd9e2-5ffe-420e-8268-5c7091c402ff/executeQueries", 
                    headers = {
                                "Content-Type":"application/json",
                                "Authorization":f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvYTc3ZDY5M2ItODE3Ny00NzI4LWI3ZjMtODJkZThiOGFhZWRkLyIsImlhdCI6MTY4MjQ5MDMyNSwibmJmIjoxNjgyNDkwMzI1LCJleHAiOjE2ODI0OTQ1NDAsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84VEFBQUFLSzU1NXZKZEZUZXRSS1gwMGJaQytPZy80Q294cDI0UUVJTXc2ZTczeVdYalcvRkhrb3ZYaUJ6ZkhJRUczNzJzby9mVjNNeDBhK291RkR0SW4zUmRkN2xmNXJlNjN5LzdCampqaktDckhWWT0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiMThmYmNhMTYtMjIyNC00NWY2LTg1YjAtZjdiZjJiMzliM2YzIiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJDaGFrcmFib3J0eSIsImdpdmVuX25hbWUiOiJBbmluZHlhIiwiaXBhZGRyIjoiMy42LjE5LjExNyIsIm5hbWUiOiJBbmluZHlhIENoYWtyYWJvcnR5Iiwib2lkIjoiYjIzOGI1MWMtYTA0Yy00YWU4LWE4NmItNTEwMjNiMThjNTQyIiwicHVpZCI6IjEwMDMyMDAyOTlBNDNEMDIiLCJyaCI6IjAuQVZZQU8ybDlwM2VCS0VlMzg0TGVpNHF1M1FrQUFBQUFBQUFBd0FBQUFBQUFBQUNmQU5BLiIsInNjcCI6IkFwcC5SZWFkLkFsbCBDYXBhY2l0eS5SZWFkLkFsbCBDYXBhY2l0eS5SZWFkV3JpdGUuQWxsIENvbnRlbnQuQ3JlYXRlIERhc2hib2FyZC5SZWFkLkFsbCBEYXNoYm9hcmQuUmVhZFdyaXRlLkFsbCBEYXRhZmxvdy5SZWFkLkFsbCBEYXRhZmxvdy5SZWFkV3JpdGUuQWxsIERhdGFzZXQuUmVhZC5BbGwgRGF0YXNldC5SZWFkV3JpdGUuQWxsIEdhdGV3YXkuUmVhZC5BbGwgR2F0ZXdheS5SZWFkV3JpdGUuQWxsIFBpcGVsaW5lLkRlcGxveSBQaXBlbGluZS5SZWFkLkFsbCBQaXBlbGluZS5SZWFkV3JpdGUuQWxsIFJlcG9ydC5SZWFkLkFsbCBSZXBvcnQuUmVhZFdyaXRlLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkV3JpdGUuQWxsIFRlbmFudC5SZWFkLkFsbCBUZW5hbnQuUmVhZFdyaXRlLkFsbCBVc2VyU3RhdGUuUmVhZFdyaXRlLkFsbCBXb3Jrc3BhY2UuUmVhZC5BbGwgV29ya3NwYWNlLlJlYWRXcml0ZS5BbGwiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiJyakcwYy12TUZFTHJBbXJ2ODZuRFJTTmNLcXBHZ29OM3FGZHF4SnN6elpVIiwidGlkIjoiYTc3ZDY5M2ItODE3Ny00NzI4LWI3ZjMtODJkZThiOGFhZWRkIiwidW5pcXVlX25hbWUiOiJBbmluZHlhQ2hha3JhYm9ydHlAUHdDVGVzdDAyMy5vbm1pY3Jvc29mdC5jb20iLCJ1cG4iOiJBbmluZHlhQ2hha3JhYm9ydHlAUHdDVGVzdDAyMy5vbm1pY3Jvc29mdC5jb20iLCJ1dGkiOiI3aUhKakkyLWFrU0RDb09SNFFVU0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyI2MmU5MDM5NC02OWY1LTQyMzctOTE5MC0wMTIxNzcxNDVlMTAiLCJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX3BsIjoiZW4ifQ.KxatzcvmZKksQmocxS3Wm3OOpJ86qHozn5aZoAF3mhsYYDvYDIL0X7Xvx3PIhRmByMGuRUiMGS5NGBMFh3u8vtTJaDuu3iXs9fBkAT18dsgyC-I94JCrFa0T_WjwDfGmsOYrlc3NIRpv5_D3mqX-yFNY_PIpTKf4uz23hwFLMw6j1xUDiy7_XGyOIt_cW4aB9BbovQTE32JPzfKOkKtZmUleFH5n0YoxUcqX3vFtxqdZXHo4ASOfqVne_EQ_vi0Oj6SJBTMNy38JpFk0_LKz-PiVvIuEx7sgdcZftaXgc9ewS6NPeJO1JxT0hOI1EnEOjayOtrhOOIuxkKU5UseOEQ"
                                }, 
                    query = {
                                "queries": [
                                  {
                                    "query": "EVALUATE VALUES(sample_data)"
                                  }
                                ],
                              
                                "impersonatedUserName": "anindyachakraborty@pwctest023.onmicrosoft.com"
                                })

    openai_prompt = f"Generate a response to the user's question based on the following Power BI data: {power_bi_data}"
    chatbot_response = chat_with_openai(openai_prompt)
    print(chatbot_response)
    return chatbot_response

#process_user_input(user_input="What is the sales amount only of Lays ?")





