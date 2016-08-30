# -*- coding: utf-8 -*-
import json
import requests
import urllib
from xml.etree import ElementTree

"""
Powerd by Microsoft Translator <https://datamarket.azure.com/dataset/bing/microsofttranslator>
"""

def GetToken(): #Get the access token from ADM, token is good for 10 minutes
    urlArgs = {
        'client_id': '100words',
        'client_secret': '99Ekd6hH2Pb/xUXbZ86kDa7I3ZIrRP0uGzFNtaXQxUA=',
        'scope': 'http://api.microsofttranslator.com',
        'grant_type': 'client_credentials'
    }

    oauthUrl = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'

    try:
        oauthToken = json.loads(requests.post(oauthUrl, data = urllib.urlencode(urlArgs)).content) #make call to get ADM token and parse json
        finalToken = "Bearer " + oauthToken['access_token'] #prepare the token
    except OSError:
        pass

    return finalToken


def GetTextAndTranslate(finalToken, textToTranslate):

    # fromLangCode = "zh"
    toLangCode = "en"

    #Call to Microsoft Translator Service
    headers = {"Authorization ": finalToken}
    translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(
                                            textToTranslate.encode('utf-8'), toLangCode)

    try:
        translationData = requests.get(translateUrl, headers = headers) #make request
        print translationData
        translation = ElementTree.fromstring(translationData.text.encode('utf-8')) # parse xml return values
        return translation.text

    except OSError:
        return "Error, please check network!"

# finalToken = GetToken()
# GetTextAndTranslate(finalToken)
