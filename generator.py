from string import Template
import json

template_main = Template("""
email:$email

Hi $name!
                          
Thank you so much for talking with $c_mentor last week for Start@UNSW Check-in Calls. I hope you found the call useful and thank you for sharing with them that you'd appreciate some support for your uni life.

I am $c_mentor's colleague, and I am sending this email to follow-up with you on your call to make sure we can get you the support you need, we understand that it can be difficult finding all the various services available.

$details

I hope you can get in touch with them and receive any support you need.  

If there is any other way I can help support you, please let me know!

Cheers,  

$sender

""")

def excelList(filename):
    with open(filename, 'r') as f:
        line = f.readline().strip()
        data = line.split('\t')

    #print(data)
    #print('\n\n')
    return data

def capitalName(string):
    words = string.split()

    if len(words) != 0:
        return words[0].capitalize()
    
def support(data):
    service_set = set()
    for key, value in data.items():
        if ('Ref. Services' in key) and value:
            print(key + value + '\n')

            service_set.update(value.split(', '))

    return service_set

def generate(data):
    #print(data)

    with open("config.json", "r") as config:
        config_data = json.load(config)

    email = data["Email"]
    name = capitalName(data["First Name"])

    call_mentor = capitalName(data["Ambassador Name"])

    services = list(support(data))
    print(services)

    details = "\n".join(services) # service list

    email_content = template_main.substitute(
        email = email,
        name = name,
        c_mentor = call_mentor,
        details = details,
        sender = config_data["Sendername"]
    )

    return email_content



call_file = excelList("surveyFormat.txt")
student_data = excelList("raw_data.txt")

if (len(call_file) != len(student_data)):   # basic error handling
    raise Exception("list length does not match")

dataset = {key:value for key, value in list(zip(call_file, student_data))}

email = generate(dataset)
#print(email)