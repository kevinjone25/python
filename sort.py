import os
import json


def valid_user(user):
    return users_db.get(user['username']) == user['password']


users_db = {
    'guest': 'guest',
    'admin': os.environ.get('PASSWORD', 'S3CR3T_P455W0RD')
}

# data ='{"showflag": false,"showflag":true,"password":null}'
# user = json.loads(data)
# print(user['showflag'])
# print(user)
i=input()
x=input()
data = '{"showflag": false, "username": "%s", "password": "%s"}' % (
        i, x
    )

print(data)
user = json.loads(data)
if valid_user(user):
        if user['showflag'] == True and user['username'] != 'guest':
            print('you success')
        else:
            print('NOPE')
print('you suck')


# print(user['showflag'])
# print(type(users_db.get(user['username']))==type(user['password']))
# print()
#print(user)
# admin", "showflag": true,"": "
# p", "password": None,"":"
# guest", "showflag": true,"username": "admin
# admin","password":"%s"}' ; data['showflag']=True; #
# admin","password":'S3CR3T_P455W0RD'}';data['showflag']=True;#"
# admin","password":"S3CR3T_P455W0RD"};data['showflag']=True;#
# guest","password":'guest'}';data['showflag']=false #
# S3CR3T_P455W0RD"}; data['showflag']=True  #
# admin","password":"S3CR3T_P455W0RD"};data['showflag']=True #
#{"showflag": false, "username": "admin","password":"S3CR3T_P455W0RD"}';data['showflag']=True #", "password": "admin","password":"S3CR3T_P455W0RD"}';data['showflag']=True #"}
#'{"showflag": false, "username": "admin","password":'S3CR3T_P455W0RD'}';data['showflag']=True;# "", "password": "admin","password":'S3CR3T_P455W0RD'}';data['showflag']=True;#""}