# -*- coding: utf-8 -*-

import http.client, urllib.parse, uuid, json
import pprint

# Replace the subscriptionKey string value with your valid subscription key.
subscriptionKey = ''

host = 'api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'

# Translate to English.
params = "&to=en";

def AquiFuntionTienes():
    pass


def api_trans_call(text):
    """Makes API calls. Based on documentatition from Microsoft"""

    def translate (content):

        headers = {
            'Ocp-Apim-Subscription-Key': subscriptionKey,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        conn = http.client.HTTPSConnection(host)
        conn.request ("POST", path + params, content, headers)
        response = conn.getresponse ()
        print(response)
        return response.read ()

    content = json.dumps(text, ensure_ascii=False).encode('utf-8')
    result = translate (content)

    # Note: We convert result, which is JSON, to and from an object so we can pretty-print it.
    # We want to avoid escaping any Unicode characters that result contains. See:
    # https://stackoverflow.com/questions/18337407/saving-utf-8-texts-in-json-dumps-as-utf8-not-as-u-escape-sequence
    output2 = json.loads(result)
    output = json.dumps(json.loads(result), indent=4, ensure_ascii=False)
    strout = []
    for i in range(0, len(text)):
        strout.append(output2[i]['translations'][0]['text'])

    print('')
    return strout


def azure_trans_25(pal_array):
    """ Main function to be called. It splits the column in 25 (API limitation) rows columns and calls the function
    'api_trans_call' """

    pp = []
    for i in range(0, len(pal_array), 25):
        pp.extend(api_trans_call(pal_array[i:i + 25]))
        print(" %s -- %s" % (i, i + 25))
    return pp


def gen_str(text):
    """Assembles the array of the body request"""

    msn = {'Text':''}
    if isinstance(text, float):
        return msn
    msn["Text"] = text
    return msn


if __name__ == '__main__':
    gen_str()