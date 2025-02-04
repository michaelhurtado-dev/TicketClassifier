import json
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

#json data
data = {
  "tickets":[
    {
        "in_id": "INC41363470",
        "description": "IRIS (Integrated Rx Information System) -unable to login to iris being onleave. inactive access",
        "action": "i just came back from maternity leave and i cant access iris",
        "open_time": "2025-02-03T17:17:55.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41354348",
        "description": "IRIS - Unable To Login",
        "action": "I'm trying to get in to IRIS but it's telling me my password is incorrect; I tried every password I could think of.",
        "open_time": "2025-02-03T13:13:04.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41357741",
        "description": "FLW - IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "I am not able to get in to IRIS. It did let me change the password which I did but still not working.",
        "open_time": "2025-02-03T14:54:12.000Z",
        "tags": [
            [
                "User Login",
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41361957",
        "description": "FLW-IRIS (Integrated Rx Information System)-Enquiry on member credit card info error",
        "action": "I have a question for you. I'm trying to assist a member. She's trying to make payments online but she getting she's getting error messages.",
        "open_time": "2025-02-03T16:36:39.000Z",
        "tags": [
            [
                "Payment"
            ]
        ]
    },
    {
        "in_id": "INC41356850",
        "description": "IRIS - Unable to reset the password",
        "action": "My iris password stating I need to update and it will not allow me to enter password",
        "open_time": "2025-02-03T14:32:32.000Z",
        "tags": [
            [
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41356597",
        "description": "Need HASH value cleared for ERx attached to wrong patient",
        "action": "Please clear the HASH value for INCORRECT account -  #427386574 \r\n\r\nCORRECT account #474730282",
        "open_time": "2025-02-03T14:25:47.000Z",
        "tags": [
            "?"
        ]
    },
    {
        "in_id": "INC41360675",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "IRIS - unable to login",
        "open_time": "2025-02-03T16:04:58.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41358998",
        "description": "IRIS - . Please assign to Babu, Pradhamasetti R. MSA ORACLE EBS (RXS) \u2013 SPT\"",
        "action": "\"Refill Smoothing 2/18/2025 to 2/21/2025 Please see attached doc for additional details. Please assign to Babu, Pradhamasetti R. MSA ORACLE EBS (RXS) \u2013 SPT\"",
        "open_time": "2025-02-03T15:22:22.000Z",
        "tags": [
            [
                "Data Fix"
            ]
        ]
    },
    {
        "in_id": "INC41363703",
        "description": "IRIS not responding, crashing",
        "action": "My supervisor told me to call because my iris is being weird. I guess like reboot it every other 3 calls as far as like spinning or it loads for like the longest time and then there's an error message and I have to close out with task manager to get it to come back up and do that a couple of times this week so don't need to call.",
        "open_time": "2025-02-03T17:24:55.000Z",
        "tags": [
            [
                "General Error"
            ]
        ]
    },
    {
        "in_id": "INC41351833",
        "description": "Please assign to IRIS-Pharmacy Central Non Prod",
        "action": "Please assign to IRIS-Pharmacy Central Non Prod\r\nFor TS04 env, while raising 3310 eRx Refill request, status is coming as with status as \"Comm Fail-Retry Pending\"\r\n\r\n\r\nProduct entered by customer:",
        "open_time": "2025-02-03T07:05:57.000Z",
        "tags": [
            "?"
        ]
    },
    {
        "in_id": "INC41354714",
        "description": "IRIS (Integrated Rx Information System) - . the iris is asking for a new password",
        "action": "I am trying to log in to everything and .. the iris is asking for a new password",
        "open_time": "2025-02-03T13:26:57.000Z",
        "tags": [
            [
                "nonsense",
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41353524",
        "description": "ORx Pharmacy Control System (Orlando) - Shipped orders not closed in wms iris",
        "action": "shipped orders not closed in wms iris assign to ORx_pcs_OV_SPT",
        "open_time": "2025-02-03T12:12:06.000Z",
        "tags": [
            [
                "Order Issue"
            ]
        ]
    },
    {
        "in_id": "INC41356279",
        "description": "IRIS (Integrated Rx Information System) - unable to login",
        "action": "I'm not able to login to IRIS",
        "open_time": "2025-02-03T14:18:07.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41354468",
        "description": "KY950 - IRIS Application login issue",
        "action": "IRIS Application login issue",
        "open_time": "2025-02-03T13:17:38.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41359419",
        "description": "iris launch mac",
        "action": "My current access to IRIS system is no longer working. Seeking asssstance to get access to perform work responsibilities",
        "open_time": "2025-02-03T15:32:05.000Z",
        "tags": [
            [
                "Launch Issues"
            ]
        ]
    },
    {
        "in_id": "INC41356578",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "training sup, contract with optumrx. have the ms id and pw and works fine. need to reset pw",
        "open_time": "2025-02-03T14:25:05.000Z",
        "tags": [
            [
                "User Login",
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41356750",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "IRIS login issue",
        "open_time": "2025-02-03T14:30:16.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41358345",
        "description": "Login to Java",
        "action": "Login to Java",
        "open_time": "2025-02-03T15:08:20.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41360973",
        "description": "IRIS (Integrated Rx Information System) - Shortcuts are missing from IRIS dashboard",
        "action": "IRIS - Shortcuts are missing from IRIS dashboard",
        "open_time": "2025-02-03T16:12:07.000Z",
        "tags": [
            "?"
        ]
    },
    {
        "in_id": "INC41356106",
        "description": "Selected Issue: IRIS",
        "action": "IRIS will not allow me to reset my password",
        "open_time": "2025-02-03T14:13:23.000Z",
        "tags": [
            [
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41359434",
        "description": "IRIS - Unable to launch this application",
        "action": "I am not able to access IRIS .couldnt put in notes and unable to open",
        "open_time": "2025-02-03T15:32:22.000Z",
        "tags": [
            [
                "Launch Issues"
            ]
        ]
    },
    {
        "in_id": "INC41355414",
        "description": "IRIS - cannot sign in for a week",
        "action": "I HAVE BEEN TRYING TO SIGN INTO IRIS FOR A WEEK NOW MY SUP SAYS I SHOULD STILL HAVE ACCESS BUT SYSTEM PROMPT ME TO CHANGE MY PASSWORD IT WORKED ONCE BUT I CANT SIGN IN",
        "open_time": "2025-02-03T13:51:40.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41357252",
        "description": "Kafka Certificate Renewal",
        "action": "The kafka client certificate orx-pharmacf785fa9fd4b33b55 (rg-pharmacy-central-kafka-prod-60fa261/hcc-dataplatform-certificate-v1/orx-pharmacf785fa9fd4b33b55) has been automatically renewed as it is less than 60 days from the expiration.\nYour new certificate will expire on Tue, 03 Feb 2026 14:41:15 UTC.\nThe new certificate download information has been sent to: hieu.le@optum.com, kevin.kinder@optum.com, prashant.mangidkar@optum.com, roshan_chirayil@optum.com, satya.chundru@optum.com, somasekhar_munupally@optum.com, sowmya_surietti@optum.com.\nA renewal email and INC will be sent around Thu, 04 Dec 2025 18:41:15 UTC.\nPlease update all uses of this certificate immediately with the newly sent certificate to avoid any expiration resulting in downtime for your application(s).",
        "open_time": "2025-02-03T14:42:17.000Z",
        "tags": [
            "?"
        ]
    },
    {
        "in_id": "INC41353986",
        "description": "IRIS (Integrated Rx Information System) - Unable to receive email to receive password.",
        "action": "Iris password need to be updated.",
        "open_time": "2025-02-03T12:51:23.000Z",
        "tags": [
            [
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41358786",
        "description": "IRIS (Integrated Rx Information System) - unable to login",
        "action": "I am unable to login to IRIS",
        "open_time": "2025-02-03T15:17:42.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41356181",
        "description": "When trying to log into IRIS this morning it asked me to change my password.  I've tried changing it multiple times but it keeps giving me the error message: Pa",
        "action": "When trying to log into IRIS this morning it asked me to change my password.  I've tried changing it multiple times but it keeps giving me the error message: Password must not contain repeating characters, but I am NOT repeating characters.",
        "open_time": "2025-02-03T14:15:12.000Z",
        "tags": [
            [
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41359389",
        "description": "Selected Issue: IRIS: NO RESPONSE",
        "action": "IRIS FREEZE WHEN DOING HFF",
        "open_time": "2025-02-03T15:31:24.000Z",
        "tags": [
            [
                "General Error"
            ]
        ]
    },
    {
        "in_id": "INC41360292",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "I need my IRIS reset the password",
        "open_time": "2025-02-03T15:54:08.000Z",
        "tags": [
            [
                "User Login",
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41360852",
        "description": "Selected Issue: IRIS",
        "action": "i am experiencing delays in both iris and a/c. keeps getting forzen",
        "open_time": "2025-02-03T16:09:37.000Z",
        "tags": [
            "?"
        ]
    },
    {
        "in_id": "INC41358801",
        "description": "PB - Orders Open in IRIS",
        "action": "HELLO- Please assist on all following orders to close in IRIS \r\nOrder# 778545783-4  Tracking# 1ZC6R5104404464326 (Delivered)  --  done\r\nOrder# 776518590-1  Tracking# 1ZC6R5101304464741 (Delivered)  --  done\r\nOrder# 777424090-3  Tracking# 9270190350467716830862 (In Transit)  --  done\r\nOrder# 777442362-3  Tracking# 9234690350467731825488 (Delivered)  --  done\r\nOrder# 777151641-2  Tracking# 1ZC6R5104404467494 (Delivered)  --  done\r\nOrder# 777857910-1  Tracking# 1ZC6R5124400915440 (Delivered)  --  done\r\nOrder# 778808458-1  Tracking# 9261290350467717088704 (Processed)  --  done\r\nOrder# 778826785-1  Tracking# 1ZC6R5100104490815 (Processed)  --  done\r\nOrder# 779166050-1  Tracking# 1ZC6R5100104495543 (Processed)  --  done",
        "open_time": "2025-02-03T15:17:52.000Z",
        "tags": [
            [
                "Order Issue"
            ]
        ]
    },
    {
        "in_id": "INC41363513",
        "description": "IRIS password issue",
        "action": "Unable to login in was instructed to change password and will not accept",
        "open_time": "2025-02-03T17:19:26.000Z",
        "tags": [
            [
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41355024",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "So ive been reassignment for 4 months and so i cant get into iris or genesys. i dont know if this gets deleted . Im using thoses systems. well I havent logged in since october so it says contact your administrator. I havent had to to use those to accept occations.",
        "open_time": "2025-02-03T13:39:00.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41359822",
        "description": "IRIS (Integrated Rx Information System) - Launch Issues",
        "action": "I am unable to login to IRIS, I changed my password earlier, now it's not allowing me",
        "open_time": "2025-02-03T15:41:41.000Z",
        "tags": [
            [
                "Launch Issues"
            ]
        ]
    },
    {
        "in_id": "INC41356200",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "Unable to login to Oracle",
        "open_time": "2025-02-03T14:15:45.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41362227",
        "description": "IRIS - unable to log in",
        "action": "im having trouble getting into citrix  showing my password is incorrect \r\n\" 2nd concern - unable to log in to IRIS",
        "open_time": "2025-02-03T16:43:12.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41362365",
        "description": "Selected Issue: IRIS",
        "action": "PROMTED TO CHANGE PASSWORD IT KEEPS GIIVING AN ERROR SAID IT ACCEPTED ON PASSWORD WHEN I TRIED TO LOGIN  IT DID NOT ACCEPT IT AND NOT TAKING ANY PASSWORDS THAT I TRY TO USE THAT MEET THE CRITERIA",
        "open_time": "2025-02-03T16:47:25.000Z",
        "tags": [
            [
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41364010",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "I cannot login in IRIS",
        "open_time": "2025-02-03T17:33:57.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41355845",
        "description": "IRIS - cannot sign in for a week",
        "action": "I HAVE BEEN TRYING TO SIGN INTO IRIS FOR A WEEK NOW MY SUP SAYS I SHOULD STILL HAVE ACCESS BUT SYSTEM PROMPT ME TO CHANGE MY PASSWORD IT WORKED ONCE BUT I CANT SIGN IN",
        "open_time": "2025-02-03T14:05:46.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41362614",
        "description": "IRIS (Integrated Rx Information System) - Launch Issues",
        "action": "Hi I I have to enter my systems through Genesis and I was trying to get into.",
        "open_time": "2025-02-03T16:54:26.000Z",
        "tags": [
            [
                "Launch Issues"
            ]
        ]
    },
    {
        "in_id": "INC41363973",
        "description": "IRIS (Integrated Rx Information System) - Launch Issues",
        "action": "having trouble with iris, every time I have a call, need to have reversal in the claim it stuck and freeze, to use it need to force close when I reopen it works",
        "open_time": "2025-02-03T17:32:43.000Z",
        "tags": [
            [
                "Launch Issues"
            ]
        ]
    },
    {
        "in_id": "INC41355914",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "I am unable to login to IRIS my password didn't push through.",
        "open_time": "2025-02-03T14:07:50.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41358410",
        "description": "Selected Issue: OMNI Genesys (WWE)",
        "action": "Submitting ticket request due to outage time being over 10 minutes: System froze and Genesys call error where call details and call would not release from system. restarted PC - VPN timeout causing delay rejoining back online.",
        "open_time": "2025-02-03T15:09:36.000Z",
        "tags": [
            [
                "User Requests"
            ]
        ]
    },
    {
        "in_id": "INC41361317",
        "description": "Selected Issue: IRIS",
        "action": "hff iris freeze",
        "open_time": "2025-02-03T16:20:07.000Z",
        "tags": [
            [
                "Latency"
            ]
        ]
    },
    {
        "in_id": "INC41360543",
        "description": "FLW - IRIS (Integrated Rx Information System) - Freezing",
        "action": "I'm having an issue with my IRIS system",
        "open_time": "2025-02-03T16:01:30.000Z",
        "tags": [
            [
                "Latency"
            ]
        ]
    },
    {
        "in_id": "INC41359989",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "I want to reset IRIS password.",
        "open_time": "2025-02-03T15:46:25.000Z",
        "tags": [
            [
                "User Login",
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41356967",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "I am unable to log in and unable to reset password",
        "open_time": "2025-02-03T14:35:33.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41353280",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "I tried to reset my password unable to login...",
        "open_time": "2025-02-03T11:41:20.000Z",
        "tags": [
            [
                "User Login",
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41356291",
        "description": "IRIS (Integrated Rx Information System) - IRIS - unable to reset my password.",
        "action": "IRIS - unable to reset my password.",
        "open_time": "2025-02-03T14:18:29.000Z",
        "tags": [
            [
                "Password"
            ]
        ]
    },
    {
        "in_id": "INC41352824",
        "description": "Gryphon First Run for 5000 records transfer",
        "action": "Update Alert 301 query to run Gryphon First run for 5000 records.\r\n\r\nRun the Request Set to transfer files to Gryphon\r\nRequest Set:  \r\nParameters: \r\nGryphon Reassigned Outbound\r\nGryphon Litigators Outbound",
        "open_time": "2025-02-03T10:30:58.000Z",
        "tags": [
            "?"
        ]
    },
    {
        "in_id": "INC41353257",
        "description": "IRIS (Integrated Rx Information System) - Unable to Login",
        "action": "I am unable to login IRIS",
        "open_time": "2025-02-03T11:37:20.000Z",
        "tags": [
            [
                "User Login"
            ]
        ]
    },
    {
        "in_id": "INC41360307",
        "description": "Need to have 'Cag Maintenance responsibility' resposibility in DV02",
        "action": "Need to have 'Cag Maintenance responsibility' resposibility in DV02 please\r\n\r\nMSID: horella\r\nEMP ID: 002094481",
        "open_time": "2025-02-03T15:54:36.000Z",
        "tags": [
            [
                "User Requests"
            ]
        ]
    }
]

}
  

# Parse JSON data
parsed_data = data["tickets"]

# Initialize a dictionary to store tag counts over time
tag_counts = defaultdict(lambda: defaultdict(int))

# Process each entry in the JSON data
for entry in parsed_data:
    open_time = datetime.strptime(entry["open_time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    hour_str = open_time.strftime("%Y-%m-%d %H:00")
    
    for tag_list in entry["tags"]:
        for tag in tag_list:
            tag_counts[hour_str][tag] += 1

# Prepare data for plotting
hours = sorted(tag_counts.keys())
all_tags = set(tag for hour in hours for tag in tag_counts[hour].keys())

# Function to plot the graph with selected tags
def plot_selected_tags(selected_tags):
    plt.figure(figsize=(12, 8))
    color_cycle = plt.cm.tab20.colors
    line_styles = ['-', '--', '-.',':']
    
    for i, tag in enumerate(selected_tags):
        counts = [tag_counts[hour].get(tag, 0) for hour in hours]
        plt.plot(hours, counts, label=tag, color=color_cycle[i % len(color_cycle)], linestyle=line_styles[i % len(line_styles)])
        for j, count in enumerate(counts):
            if count > 0:
                plt.text(hours[j], count, str(count), fontsize=8)
    
    # Customize the plot
    plt.xlabel("Hour")
    plt.ylabel("Count")
    plt.title("Incident tickets by Hour")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Show the plot
    plt.show()

# Example usage: Select tags to include in the graph
selected_tags = ["Service Down", "General Error", "Order Issue","Launch Issues","User Login","Latency","Crash","Password"]
plot_selected_tags(selected_tags)