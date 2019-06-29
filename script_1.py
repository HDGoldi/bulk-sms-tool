import requests, json
import urllib3

urllib3.disable_warnings()
token_url = "https://api.1nce.com/management-api/oauth/token"

# client (application) credentials
client_id = '81001125_awais_se'
client_secret = 'awais_se-1Nce!'

# step A- single call with client credentials as the basic auth header - will return access_token
data = {'grant_type': 'client_credentials'}

access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False,
                                      auth=(client_id, client_secret))
if access_token_response.status_code == 200:
    
    tokens = json.loads(access_token_response.text)
    
    access_token = tokens['access_token']
    my_iccid = tokens['userId']
    # step B - with the returned access_token we can make as many calls as we want
    # get list of all iccids
    
    get_sim_url = "https://api.1nce.com/management-api/v1/sims"
    
    mes_resp = requests.get(get_sim_url, headers={'Content-Type': 'application/json',
                                                  'Authorization': 'Bearer {}'.format(access_token)})
    get_message_request = json.loads(mes_resp.text)
    
    # got all sims iccids
    i = 0
    sent_sms_iccid = []
    failed_sent_sms = []
    
    #Message
    
    message_content = "i am demonstrating this message to buyer !!!!!!!!! from awais_se Fiverr Okay ? "
    
    #now parsing json and reading iccids one by one and sending messages
    
    while i < len(get_message_request):
    
    
        # passing iccid in url one by one
    
        send_sms_url = "https://api.1nce.com/management-api/v1/sims/" + get_message_request[i]['iccid'] + "/sms"
    
        send_sms_res = requests.post(send_sms_url, headers={'Content-Type': 'application/json',
                                                            'Authorization': 'Bearer {}'.format(access_token)},
                                     json={"payload": message_content, "source_address": my_iccid})
    
        #checking status of request , if 201 then sent , otherwise failed
    
        if send_sms_res.status_code == 201:
            sent_sms_iccid.append(get_message_request[i]['iccid'])
            print("Sent..")
        else:
            failed_sent_sms.append(get_message_request[i]['iccid'])
            print("Got error..")
    
        i = i + 1
    
    
    
    # showing end report of all processing
    
    print("Total Sent : " + str(len(sent_sms_iccid)))
    for x in range(len(sent_sms_iccid)):
        print(sent_sms_iccid[x])
    
    print("Total Failed : " + str(len(failed_sent_sms)))
    for x in range(len(failed_sent_sms)):
        print(failed_sent_sms[x])
else:
    print("PLease make sure that your credentials are correct ! . ")