def addCoursePayload():

    body = {
        "Subscriber ID": "Naga",
        "Course" : "Java Script",
        "Course_Fee": "$500",
        "Subscription_Start_Date" : "12-05-2024",
        "Subscription_End_Date": "31-05-2024"
    }

    return body
#Selenium WebDriver 4 With Java,15
print(addCoursePayload())

