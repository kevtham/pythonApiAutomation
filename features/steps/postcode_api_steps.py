import requests
from behave import given, then, when
from config.TestConfig import TestConfig
from pykson import Pykson
from model.PostCodes import PostCode, Codes
from utils.commonUtils import util


@given(u'I need to call the postcode get api and store the response')
def step_impl(context):
    print("Attempting to get the url details :::::")
    config = TestConfig

    urlvalue = config.getURlname('url', 'postcodeurl')

    if (urlvalue==None):
        print("Exit the call as the url %s renedered" %urlvalue)
        exit
    else:
        print("Attempting to hit the url %s" %urlvalue)
    
    # Request
    response = requests.get(urlvalue)
    if (response.status_code != 200):
        response.raise_for_status()
    
    print(response.json()['result'])
    assert (200==response.status_code)
    util.assertEqualCheck(response.status_code, 201 , "PO assert status Mismatch ")
    
    # Assert
    postcode=Pykson().from_json(response.json()['result'], PostCode, accept_unknown=True)
    assert (postcode.postcode!="")
    print(postcode.postcode)
    print(postcode.longitude)
    print(postcode.codes.admin_district)
    
    print(util.assertEmptyCheck(postcode.codes.admin_district))