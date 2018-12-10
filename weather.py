import requests
from flask import Flask, render_template, request,flash


app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/", methods=['GET', 'POST'])
def index():

        if request.method == 'POST':

            new_city = request.form.get('city')


            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=bbb4e2e9523a1b3bda54f09eb20f13a7'


            weather_data = []

            r = requests.get(url.format(new_city)).json()


            if r['cod'] == 200:

                id = r['weather'][0]['id']

                day_or_night = r['weather'][0]['icon'][-1:]


                if (id in [200, 201, 202, 210, 211, 212, 221, 230, 231, 232, 300, 301, 302, 310, 311, 312, 313, 314, 321, 500, 501, 502, 503, 504, 511, 520, 521, 522, 531]):
                    bg_image = "rain_bg.jpg"
                    icon_img = "rain_icon.svg"
                elif (id in [600, 601, 602, 611, 612, 615, 616, 620, 621, 622]):
                    bg_image = "snow_bg.jpg"
                    icon_img = "rain_icon.svg"
                elif (id in [701, 711, 721, 731, 741, 751, 761, 762, 771, 781]):
                    bg_image = "atmos_bg.jpg"
                    if (day_or_night == 'd'):
                        icon_img = "sun_icon.svg"
                    else:
                        icon_img = "night_icon.svg"
                elif (id in [801, 802, 803, 804]):
                    bg_image = "cloud_bg.jpg"
                    if (day_or_night == 'd'):
                        icon_img = "sun_icon.svg"
                    else:
                        icon_img = "night_icon.svg"
                elif (id == 800):

                    if (day_or_night == 'd'):
                        icon_img = "sun_icon.svg"
                        bg_image = "sun_bg.png"
                    else:
                        icon_img = "night_icon.svg"
                        bg_image = "night_bg.jpg"
                else:
                    icon_img = "invalid"
                    bg_image = "invalid"

                temp = {
                    'city': r['name'],
                    'temp': r['main']['temp'],
                    'desc': r['weather'][0]['description'],
                    'bg_img': bg_image,
                    'icon_img': icon_img,
                        }

                weather_data.append(temp)

                return render_template("weather.html", weather_data=weather_data)

            flash('Check the spelling!', 'danger')
            return render_template("weather.html")

        return render_template("weather.html")




if __name__ == '__main__':
    app.run(threaded=True)
