from flask import Flask,jsonify,request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message':'Welcome to the demo API'})

# Demo: We can take in a user's input, and pipe that input to our model to get an output
@app.route('/api/<float:user_input>')
def predict(user_input):
    ans=float(model.predict_proba([[user_input,34]])[:,0])
    return jsonify({'Probability':ans})

if __name__ == '__main__':
    modelfile = 'model.pickle'
    model = pickle.load(open(modelfile, 'rb'))
    app.run(debug=True)