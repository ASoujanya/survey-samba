
from flask import Flask,request,jsonify
from sqlalchemy.orm import query
from models import client,db,app
# from config import db


#general Flask Code
@app.route('/client')
def get_clients():
    
    return jsonify([
        {'_id': user.id, 'name':user.name}for user in client.query.all()
    ])

@app.route('/client/<id>/')
def get_client_by_id(id):
    print(id)
    user = client.query.filter_by(id=id).first_or_404()
    return {'_id': user.id, 'name':user.name}

@app.route('/client/', methods=['POST'])
def add_client():
    data = request.get_json()
    print(data)
    if not 'name' in data:
        return jsonify({
            'error':'Bad Request',
            'message':'Name not given'
        }),400
    user = client(
        name = data['name']
    )
    db.session.add(user)
    db.session.commit()
    return {
        'id': user.id, 'name': user.name
    },201


@app.route('/client/<id>', methods=['PUT'])
def update_client(id):
    data = request.get_json()
    print(data)
    user = client.query.filter_by(id=id).first_or_404()
    print(user.name)
    user.name = data['name']
    db.session.commit()
    return jsonify({
        'id':user.id, 'name':user.name
    })


@app.route('/client/<id>/', methods=['DELETE'])
def delete_client_by_id(id):
    user = client.query.filter_by(id=id).first_or_404()
    db.session.delete(user)
    db.commit()
    return{
        'success': 'Data deleted succefully'
    }

 

if __name__ == '__main__':
    app.run(debug=True)