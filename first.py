from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'Hi' in incoming_msg or 'Hey' in incoming_msg or 'Heya' in incoming_msg or 'Menu' in incoming_msg:
        text = f'Hello !!!!!!! \nThis is a Covid-Bot developed by *RUTVIK MODI* *(KIVTUR)* to provide latest information updates i.e cases in different countries and create awareness to help you and your family stay safe. \n \n *For any emergency* \n\n ----> Helpline: 011-23978046 \n ----> Toll-Free Number: 1075 \n ----> Email: ncov2019@gov.in \n\nPlease type one of the following option given in the bold: \n\n *World*. Covid-19 statistics *Worldwide*. \n *Ind*. Covid-19 cases in *India*. \n *Chi*. Covid-19 cases in *China*. \n *Usa*. Covid-19 cases in *USA*. \n *Ita*. Coronavirus cases in *Italy*. \n *Aus*. Coronavirus cases in *Australia*. \n *Jap*. Coronavirus cases in *Japan*. \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken.'
        msg.body(text)
        responded = True

    if 'World' in incoming_msg:
        # return total cases
        r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases Worldwide_ \n\nConfirmed Cases : *{data["cases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}*  \n\n*Type one of the option given below to know more*\n\n *World*. Covid-19 statistics *Worldwide*. \n *Ind*. Covid-19 cases in *India*. \n *Chi*. Covid-19 cases in *China*. \n *Usa*. Covid-19 cases in *USA*. \n *Ita*. Coronavirus cases in *Italy*. \n *Aus*. Coronavirus cases in *Australia*. \n *Jap*. Coronavirus cases in *Japan*. \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken.\n\nType *Menu* to view the Main Menu'
            print(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    elif 'Ind' in incoming_msg or 'India' in incoming_msg:
        # return cases in india
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/india')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in India_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\n*Type one of the option given below to know more*\n\n *World*. Covid-19 statistics *Worldwide*. \n *Ind*. Covid-19 cases in *India*. \n *Chi*. Covid-19 cases in *China*. \n *Usa*. Covid-19 cases in *USA*. \n *Ita*. Coronavirus cases in *Italy*. \n *Aus*. Coronavirus cases in *Australia*. \n *Jap*. Coronavirus cases in *Japan*. \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken.\n\nType *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    elif 'Chi' in incoming_msg or 'China' in incoming_msg:
        # return cases in china
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/china')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in China_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}* \n\n*Type one of the option given below to know more*\n\n *World*. Covid-19 statistics *Worldwide*. \n *Ind*. Covid-19 cases in *India*. \n *Chi*. Covid-19 cases in *China*. \n *Usa*. Covid-19 cases in *USA*. \n *Ita*. Coronavirus cases in *Italy*. \n *Aus*. Coronavirus cases in *Australia*. \n *Jap*. Coronavirus cases in *Japan*. \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken.\n\nType *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    elif 'Usa' in incoming_msg or 'USA' in incoming_msg:
        # return cases in usa
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/usa')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in USA_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}*  \n\n*Type one of the option given below to know more*\n *World*. Covid-19 statistics *Worldwide*. \n *Ind*. Covid-19 cases in *India*. \n *Chi*. Covid-19 cases in *China*. \n *Usa*. Covid-19 cases in *USA*. \n *Ita*. Coronavirus cases in *Italy*. \n *Aus*. Coronavirus cases in *Australia*. \n *Jap*. Coronavirus cases in *Japan*. \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken.\n\nType *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    elif 'Ita' in incoming_msg or 'Italy' in incoming_msg:
        # return cases in italy
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/italy')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in Italy_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}* \n\n*Type one of the option given below to know more*\n *World*. Covid-19 statistics *Worldwide*. \n *Ind*. Covid-19 cases in *India*. \n *Chi*. Covid-19 cases in *China*. \n *Usa*. Covid-19 cases in *USA*. \n *Ita*. Coronavirus cases in *Italy*. \n *Aus*. Coronavirus cases in *Australia*. \n *Jap*. Coronavirus cases in *Japan*. \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken.\n\nType *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    elif 'Aus' in incoming_msg or 'Australia' in incoming_msg:
        # return cases in italy
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/australia')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in Australia_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}* \n\n*Type one of the option given below to know more*\n *World*. Covid-19 statistics *Worldwide*. \n *Ind*. Covid-19 cases in *India*. \n *Chi*. Covid-19 cases in *China*. \n *Usa*. Covid-19 cases in *USA*. \n *Ita*. Coronavirus cases in *Italy*. \n *Aus*. Coronavirus cases in *Australia*. \n *Jap*. Coronavirus cases in *Japan*. \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken.\n\nType *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    elif 'Jap' in incoming_msg or 'Japan' in incoming_msg:
        # return cases in italy
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/japan')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in Japan_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}* \n\n*Type one of the option given below to know more*\n *World*. Covid-19 statistics *Worldwide*. \n *Ind*. Covid-19 cases in *India*. \n *Chi*. Covid-19 cases in *China*. \n *Usa*. Covid-19 cases in *USA*. \n *Ita*. Coronavirus cases in *Italy*. \n *Aus*. Coronavirus cases in *Australia*. \n *Jap*. Coronavirus cases in *Japan*. \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken.\n\nType *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True


    elif 'F' in incoming_msg:
        text = f'_Coronavirus spreads from an infected person through_ \n\nSmall droplets from the nose or mouth which are spread when a person coughs or sneezes \n\nTouching an object or surface with these droplets on it and then touching your mouth, nose, or eyes before washing your hands \n\nClose personal contact, such as touching or shaking hands \nPlease watch the video for more information \nhttps://youtu.be/0MgNgcwcKzE \n\n*Type one of the option given below to know more*\n\n *World*. Covid-19 statistics *Worldwide*. \n *Ind*. Covid-19 cases in *India*. \n *Chi*. Covid-19 cases in *China*. \n *Usa*. Covid-19 cases in *USA*. \n *Ita*. Coronavirus cases in *Italy*. \n *Aus*. Coronavirus cases in *Australia*. \n *Jap*. Coronavirus cases in *Japan*. \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken.\n\nType *Menu* to view the Main Menu'
        msg.body(text)
        msg.media('https://user-images.githubusercontent.com/34777376/77290801-f2421280-6d02-11ea-8b08-fdb516af3d5a.jpeg')
        responded = True

    elif 'G' in incoming_msg:
        text = f'_Coronavirus infection can be prevented through the following means_ \nClean hand with soap and water or alcohol-based hand rub \nhttps://youtu.be/EJbjyo2xa2o \n\nCover nose and mouth when coughing & sneezing with a tissue or flexed elbow \nhttps://youtu.be/f2b_hgncFi4 \n\nAvoid close contact & maintain 1-meter distance with anyone who is coughing or sneezin \nhttps://youtu.be/mYyNQZ6IdRk \n\nIsolation of persons traveling from affected countries or places for at least 14 day \nhttps://www.mohfw.gov.in/AdditionalTravelAdvisory1homeisolation.pdf \n\nQuarantine if advise \nhttps://www.mohfw.gov.in/Guidelinesforhomequarantine.pdf \n\n*Type one of the option given below to know more*\n\n *World*. Covid-19 statistics *Worldwide*. \n *Ind*. Covid-19 cases in *India*. \n *Chi*. Covid-19 cases in *China*. \n *Usa*. Covid-19 cases in *USA*. \n *Ita*. Coronavirus cases in *Italy*. \n *Aus*. Coronavirus cases in *Australia*. \n *Jap*. Coronavirus cases in *Japan*. \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken.\n\nType *Menu* to view the Main Menu'
        msg.body(text)
        msg.media('https://user-images.githubusercontent.com/34777376/77290864-1c93d000-6d03-11ea-96fe-18298535d125.jpeg')
        responded = True

    elif responded == False:
        msg.body('I only know about corona, sorry!')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
