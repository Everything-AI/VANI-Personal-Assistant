import os, webbrowser, re
from flask import Flask, render_template, request
import vani_the_bot

app = Flask(__name__)


@app.route("/")
def main_page():
	return render_template('index.html')


@app.route("/get")
def get_response():
	userText = request.args.get('msg')
    action = userText.lower().split()
	if 'play' in action[0]:
		webbrowser.open('https://www.youtube.com/results?search_query='+str(action[5:]), new=2)
		return 'Enjoy!'
	elif 'search for' in userText.lower():
        reg_ex = re.search('search for (.*)', userText)
        
		webbrowser.open('https://www.google.com/search?q='+str(userText[7:]), new=2)
		return 'Sure :D'
	elif 'open reddit' in userText:
        reg_ex = re.search('open reddit (.*)', userText)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url, new=2)
        return 'Done!'

    elif 'open website' in userText:
        reg_ex = re.search('open website (.+)', userText)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            return 'Done!'
        else:
            pass

    elif 'joke' in userText:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            return str(res.json()['joke'])
        else:
            return 'oops!I ran out of jokes'

    elif 'current weather in' in userText:
        reg_ex = re.search('current weather in (.*)', userText)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()
            return 'The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8)

    elif 'weather forecast in' in userText:
        reg_ex = re.search('weather forecast in (.*)', userText)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            forecasts = location.forecast()
            for i in range(0,3):
                return 'On %s will it %s. The maximum temperture will be %.1f degree.'
                         'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8)
	else:
		return str(vani_the_bot.respond(userText))



if __name__ == '__main__':
	host = os.environ.get('IP', '0.0.0.0')
	app.run(host=host, port=5555, debug=True)