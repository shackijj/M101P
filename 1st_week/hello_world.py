import bottle
import pymongo

@bottle.route('/')
def home_page():
    
    mythings = ['apple', 'orange', 'banana', 'peach']

    #return bottle.template('hello_world', username="Andrew", things=mythings)
    return bottle.template('hello_world', {'username':"Richard", 'things': mythings})

@bottle.route('/favorite_fruit', method="POST")
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if(fruit == None or fruit == ""):
        fruit = "No fruit selected"

    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect("/show_fruit")

@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")

    return bottle.template('fruit_selection', {'fruit':fruit})

bottle.debug(True)
bottle.run(host='10.0.2.15', port=8082)
