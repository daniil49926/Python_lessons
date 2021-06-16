from flask import Flask
from flask import request
import json
import copy
app = Flask(__name__)

messages = {'any': []}


@app.route('/post', methods=['post'])
def post():
    global messages
    req = request.get_json()
    print('Msg from:', req['sender'], 'to:', req['recipient'])
    print('Msg body:', req['msg'])
    if req['recipient'] != 'any':
        if req['recipient'] in messages:
            messages[req['recipient']].append({'sender': req['sender'], 'msg': req['msg']})
        else:
            messages[req['recipient']] = [{'sender': req['sender'], 'msg': req['msg']}]
    else:
        if len(messages['any']) == 0:
            messages['any'].append({'sender': req['sender'], 'msg': req['msg']})
        else:
            first = messages['any'][0]['sender']
            second = req['sender']
            if first in messages:
                messages[first].append({'sender': second, 'msg': '{"msg":"challenge_ok"}'})
            else:
                messages[first] = [{'sender': second, 'msg': '{"msg":"challenge_ok"}'}]
            if second in messages:
                messages[second].append({'sender': first, 'msg': '{"msg":"challenge_ok"}'})
            else:
                messages[second] = [{'sender': first, 'msg': '{"msg":"challenge_ok"}'}]
            del messages['any'][0]
    return 'OK'


@app.route('/check', methods=['post'])
def check():
    global messages
    req = request.get_json()
    print('Check Msg for:', req['recipient'])
    print(messages)
    if req['recipient'] in messages:
        msgs = copy.deepcopy(messages[req['recipient']])
        messages.pop(req['recipient'])
        return json.dumps(msgs)
    else:
        return json.dumps([])


app.run()