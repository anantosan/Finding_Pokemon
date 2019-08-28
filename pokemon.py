from flask import Flask, jsonify, request, render_template,redirect
import requests

app= Flask(__name__)

@app.route('/')
def beranda():
    return render_template('search_poke.html')

@app.route('/hasil',methods=['POST'])
def hasil():
    search=request.form
    url='https://pokeapi.co/api/v2/pokemon/'
    data=requests.get(url+search['nama'].lower())
    if data.status_code==404:
        return render_template('error_poke.html')
    else:
        data=data.json()
        return render_template('hasil_poke.html',data=data)


if __name__=='__main__':
    app.run(debug=True)