import os
import boto3
from botocore.exceptions import ClientError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

import json
import urllib

def firebase_messaging_sw_js(request):
    filename = '/static/well-known/pki-validation/89C8C03A5E8FD44929A39F310B599CAB.txt'
    f = open(os.path.abspath("travelbsst") + filename, 'rb')
    
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")


def contactUsRequest(request):
    
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': '6Lc5AaYZAAAAAMR2ChUelZ9y952g05psAOcfFaXC',
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:
            SENDER = "<infosrdi@vesselkaconsult.com>"

            RECIPIENT = "infosrdi@vesselkaconsult.com"

            # CONFIGURATION_SET = "ConfigSet"

            AWS_REGION = "eu-west-1"

            SUBJECT = "Contact Us"
            try:
            
                name = "" + request.POST['name']
            except:
                name = "" 
            try:
            
                email = "" + request.POST['email']
            except:
                email = ""
            try:
            
                subject = "" + request.POST['subject']
            except:
                subject = "" 
            try:
            
                message = "" + request.POST['message']
            except:
                message = ""
                

            BODY_TEXT = (
                            "name - {0} \n"
                            "email - {1} \n"
                            "subject - {2} \n"
                            "message - {3} \n"
                    ).format(name,email,subject,message)
                            
            CHARSET = "UTF-8"

            client = boto3.client('ses',region_name=AWS_REGION)
            
            try:
                response = client.send_email(
                    Destination={
                        'ToAddresses': [
                            RECIPIENT,
                        ],
                    },
                    Message={
                        'Body': {
                            'Text': {
                                'Charset': CHARSET,
                                'Data': BODY_TEXT,
                            },
                        },
                        'Subject': {
                            'Charset': CHARSET,
                            'Data': SUBJECT,
                        },
                    },
                    Source=SENDER,
                    # ConfigurationSetName=CONFIGURATION_SET,
                )
                
                return redirect('/')

            except ClientError as e:
                name = {
                    'firstName': e.response['Error']['Message'],
                    }
                return render(request, 'accommodation/error.html')


        else:
            return redirect('/')

    
def joinUsRequest(request):

    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': '6Lc5AaYZAAAAAMR2ChUelZ9y952g05psAOcfFaXC',
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:       
            try:
            
                email = request.POST['emails']
            except:
                email = "infosrdi@vesselkaconsult.com"

            SENDER = "Sender Name <infosrdi@vesselkaconsult.com>"

            RECIPIENT = "{}".format(email)


            # CONFIGURATION_SET = "ConfigSet"

            AWS_REGION = "eu-west-1"

            SUBJECT = "Join Us Request"
            try:
            
                country = "" + request.POST['country']
            except:
                country = "" 
            try:
            
                community_name = "" + request.POST['community_name']
            except:
                community_name = ""
            try:
            
                fullname = "" + request.POST['fullname']
            except:
                fullname = "" 
            try:
            
                address = "" + request.POST['address']
            except:
                address = "" 
            try:
            
                email = "" + request.POST['email']
            except:
                email = "" 

                
            try:
            
                organisation_name = "" + request.POST['organisation_name']
            except:
                organisation_name = ""

                
            try:
            
                organisation_address = "" + request.POST['organisation_address']
            except:
                organisation_address = ""

                
            try:
            
                organisation_type = "" + request.POST['organisation_type']
            except:
                organisation_type = "" 

                
            try:
            
                organisation_website = "" + request.POST['organisation_website']
            except:
                organisation_website = ""

                
            try:
            
                organisation_email = "" + request.POST['organisation_email']
            except:
                organisation_email = ""

                
            try:
            
                description = "" + request.POST['description']
            except:
                description = ""

                
            try:
            
                description_community = "" + request.POST['description_community']
            except:
                description_community = ""

                
            try:
            
                description_suploc = "" + request.POST['description_suploc']
            except:
                description_suploc = ""

                
            try:
            
                description_wilflide = "" + request.POST['description_wilflide']
            except:
                description_wilflide = ""

                
            try:
            
                description_trad = "" + request.POST['description_trad']
            except:
                description_trad = ""

                
            try:
            
                organisation_booking_contact = "" + request.POST['organisation_booking_contact']
            except:
                organisation_booking_contact = ""

                
            try:
            
                organisation_email_address = "" + request.POST['organisation_email_address']
            except:
                organisation_email_address = ""

                
            try:
            
                organisation_phone = "" + request.POST['organisation_phone']
            except:
                organisation_phone = ""

                
            try:
            
                organisation_language = "" + request.POST['organisation_language']
            except:
                organisation_language = ""

            BODY_TEXT = (
                            "country - {0} \n"
                            "community_name - {1} \n"
                            "fullname - {2} \n"
                            "address - {3} \n"
                            "email - {4} \n"
                            "organisation_name - {5} \n"
                            "organisation_address - {6} \n"
                            "organisation_type - {7} \n"
                            "organisation_website - {8} \n"
                            "organisation_email - {9} \n\n\n\n"
                            "description - {10} \n"
                            "description_community - {11} \n"
                            "description_suploc - {12} \n"
                            "description_wilflide - {13} \n"
                            "description_trad - {14} \n\n\n\n"
                            "organisation_booking_contact - {15} \n"
                            "organisation_email_address - {16} \n"
                            "organisation_phone - {17} \n"
                            "organisation_language - {18} \n"
                    ).format(country,community_name,fullname,address,email,organisation_name,organisation_address,organisation_type,organisation_website,organisation_email,description,description_community,description_suploc,description_wilflide,description_trad,organisation_booking_contact,organisation_email_address,organisation_phone,organisation_language)          
            CHARSET = "UTF-8"

            client = boto3.client('ses',region_name=AWS_REGION)

            try:
                response = client.send_email(
                    Destination={
                        'ToAddresses': [
                            RECIPIENT,
                        ],
                    },
                    Message={
                        'Body': {
                            'Text': {
                                'Charset': CHARSET,
                                'Data': BODY_TEXT,
                            },
                        },
                        'Subject': {
                            'Charset': CHARSET,
                            'Data': SUBJECT,
                        },
                    },
                    Source=SENDER,
                    # ConfigurationSetName=CONFIGURATION_SET,
                )
            except ClientError as e:
                name = {
                    'firstName': e.response['Error']['Message'],
                    }
                return render(request, 'accommodation/error.html')
            else:
                print("Email sent! Message ID:"),
                return redirect('/')
        else:
            return redirect('/')


