#cats.py
#These are the categories, edit them as you please. 
categories = {
    "Order Issue": ["order not closed","order not closed in","shipped orders","shipped orders not closed","order did not close"],
    "User Login": ["login","access","new account","log in","unable to login","unable to log in","login failed","not logging in","locked","SSO authentication error","unable to access"],
    "Password":["password not working","wrong password", "need password reset","pw","changed pw"],
    "Data Fix": ["df","data fix","need data fix","datafix","refill smoothing","Cap RX suffix DF","need datafix","datafix for last fill"],
    "Image Viewer":["imageviewer","image viewer","image","viewer","image not loading","rxs imaging"],
    "Payment":["credit card","credit","card","cc","credit card declining","debit card","card issue","declining","cc not working","unable add cc"],
    "User Request":["skillset","run xxiris", "common auto refill program","job submitted","please assign","request for helpdesk","Turn off profile","self service ticket","increasing","requesting","need support","need to update","please"],
    "Launch Issues":["launching","unable to launch","cannot launch","not working","unable to open","launch issues","cannot access","issues"],
    "Crash":["crashing","crashes", "shuts down", "dropping", "shut down",  "kicked", "shutting down", "screen turned black","lost signal"],
    "Close": ["closing out","cut out","force closing","closes","closing automatically"],
    "Stalling":["stalling","stalls"],
    "Slow": ["slow","lagging","delay","latency"],
    "Blank Screen": ["black screen", "screen is black","blank screen"],
    "Unresponsive": ["unresponsive","not responding"],
    "Frozen": ["frozen", "freezing", "freezes"],
    "Spinning": ["spin", "around and around","buffering"],
    "Java":["java","java issue","java error"],
    "RX locked": ["rx locked for editing"],
    "General Error": ["not working","error","ERROR:APP-IEU-241025","Issues","shortcuts missing","not working properly"],
    "Alert": ["alert","Critical","warning"],
    "Service Down": ["service unavailable"],
    "FRM Error": ["FRM","failure in the forms server"],
    "nonsense": ["poc"]
}

parent_categories = {
    "Stalling": "Latency",
    "Unresponsive": "Latency",
    "Frozen": "Latency",
    "Spinning": "Latency",
    "Slow": "Latency",
    "Close": "Crash",
    "Blank Screen": "Latency",
    "General Error": "Errors",
    "FRM Error": "Errors",
    "Service Down": "Errors",
    "Java": "Errors"
}


