from string import Template

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

def generate(data):
    print("\n\n\n")
    print(data)

    email = ""
    name = ""
    call_mentor = ""
    services = []

    details = "\n".join(services) # service list

    email_content = template_main.substitute(
        email = email,
        name = name,
        c_mentor = call_mentor,
        details = details,
        sender = "Eamonn"
    )

    return email_content


with open('raw_data.txt', 'r') as f:
    line = f.readline().strip()
    data = line.split('\t')

print(generate(data))