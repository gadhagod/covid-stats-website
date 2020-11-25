import flask
import ctp

app = flask.Flask(__name__)

def insert_commas(in_str):
    return(
        '{:,}'.format(int(in_str))
    )

def us():
    data = ctp.us().current()[0]
    for stat in data:
        try:
            data[stat] = insert_commas(data[stat])
        except:
            pass
    return(data)

def states(state):
    data = ctp.states().current(state)
    for stat in list(data.keys()):
        try:
            data[stat] = insert_commas(data[stat])
        except:
            pass
    return(data)

@app.route('/', methods=['GET'])
def main():
    return(
        flask.render_template('index.html', us=us())
    )

@app.route('/state/<target>', methods=['GET'])
def state(target):
    return(
        flask.render_template(
            'state.html', 
            metadata=ctp.states().metadata(target),
            stats=states(target)
        )
    )

@app.errorhandler(500)
def server_error(err):
    return(flask.render_template('no_results.html'))

@app.errorhandler(404)
def redirect_home(err):
    return('<script>location.href = "/"</script>')