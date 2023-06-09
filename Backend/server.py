from flask import Flask, request, jsonify
from flask_cors import CORS
import SudokuSolver
import datetime
import json

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
CORS(app)

# Route for seeing a data
@app.route('/data')
def get_time():
    # Returning an api for showing in  reactjs
    print("Gello")
    return {
        'Name': "geek",
        "Age": "22",
        "Date": x,
        "programming": "python"
    }

@app.route('/state', methods=["POST"])
def post_sudokuBoard():
    record = json.loads(request.data)
    gr = record['body']
    print(gr)
    oneD=[]
    twoD=[]
    i=0
    for c in gr:
        if c.isnumeric() or c=='.':
            oneD.append(c)
            i+=1
            if i%9==0:
                twoD.append(oneD)
                oneD=[]


    print(twoD)
    obj = SudokuSolver.Sudokusolver(twoD)
    obj.funcOrder()
    return ' ';

# Running app
if __name__ == '__main__':
    app.run(debug=True)