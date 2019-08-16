from flask import Flask, jsonify, abort, request, make_response

import init
import xmltodict

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    """

    :param error:
    :return:
    """
    return make_response(jsonify({'error': 'Not Found'}), error.code)


@app.errorhandler(400)
def bad_request(error):
    """

    :param error:
    :return:
    """
    return make_response(jsonify({'error': 'Bad Request'}), error.code)


@app.route('/')
def root():
    """Serve root HTML file for single page application

    :return:
    """
    return app.send_static_file('index.html')


@app.route('/token', methods=['GET'])
def get_token():
    appId = request.args.get('appId', default=0, type=int)
    if int(appId) == 18020:
        return str(111111111)
    else:
        abort(400)


@app.route('/deleg/token', methods=['GET'])
def get_deleg_token():
    appId = request.args.get('appId', default=0, type=int)
    if int(appId) == 18020:
        return str(337399158)
    else:
        abort(400)


@app.route('/GetToken/WsGetToken.asmx', methods=['GET'])
def ws_get_token():
    """

    :return:
    """
    data = request.data

    if data:
        dict_data = xmltodict.parse(data, process_namespaces=False)
        token_id = dict_data['SOAP-ENV:Envelope']['SOAP-ENV:Body']['GetToken']['pstrTokenID']
        if int(token_id) == 111111111:
            return app.send_static_file('WsGetToken_9999999.xml')
        elif int(token_id) == 337399158:
            return app.send_static_file('WsGetToken_9999998.xml')
        else:
            abort(400)
    else:
        return app.send_static_file('WsGetToken_wsdl.xml')


if __name__ == '__main__':
    host = init.SSO_SERVICE_HOST
    port = init.SSO_SERVICE_PORT

    init.logger.info('=' * 20)
    init.logger.info('Starting mock-sso with parameters:')
    init.logger.info('SSO_SERVICE_HOST: {}'.format(host))
    init.logger.info('SSO_SERVICE_PORT: {}'.format(port))
    init.logger.info('=' * 20)

    app.run(host=host, port=int(port), debug=True)
