import boto3
from botocore.exceptions import ClientError
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

from datetime import datetime
import stripe

# Create your views here.

def sendEmail(request):

	if request.method == 'POST':
		SENDER = "<infosrdi@vesselkaconsult.com>"

		# Replace recipient@example.com with a "To" address. If your account
		# is still in the sandbox, this address must be verified.
		RECIPIENT = "iveri.g.56@gmail.com"

		# Specify a configuration set. If you do not want to use a configuration
		# set, comment the following variable, and the
		# ConfigurationSetName=CONFIGURATION_SET argument below.
		# CONFIGURATION_SET = "ConfigSet"

		# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
		AWS_REGION = "eu-west-1"

		# The subject line for the email.
		SUBJECT = "booking request"




		# The character encoding for the email.
		CHARSET = "UTF-8"

		# Create a new SES resource and specify a region.
		client = boto3.client('ses', region_name=AWS_REGION)

		# Try to send the email. 


		try:
			try:
			
				firstName = "" + request.POST['firstName']
			except:
				firstName = "" 
			try:
			
				lastName = "" + request.POST['surname']
			except:
				lastName = ""
			try:
			
				email = "" + request.POST['email']
			except:
				email = "" 
			try:
			
				phone_number = "" + request.POST['phonenumber']
			except:
				phone_number = "" 
			try:
			
				arrive = "" + request.POST['firstdate']
			except:
				arrive = "" 

				
			try:
			
				country = "" + request.POST['country']
			except:
				country = ""

				
			try:
			
				country_code = "" + request.POST['countryCode']
			except:
				country_code = ""

				
			try:
			
				departure = "" + request.POST['seconddate']
			except:
				departure = "" 

				
			try:
			
				guests = "" + request.POST['guests_number']
			except:
				guests = ""

				
			try:
			
				accomodation_type = "" + request.POST['accomodation_type']
			except:
				accomodation_type = "default"

				
			try:
			
				veg = "" + request.POST['match-with-pairs']
			except:
				veg = "false"

				
			try:
			
				transportation = "" + request.POST['match-with-pairs2']
			except:
				transportation = "false"

				
			try:
			
				accomodation_and_breakfast = "" + request.POST['accomodation_and_breakfast']
			except:
				accomodation_and_breakfast = ""

				
			try:
			
				popup_tour_price = "" + request.POST['popup_tour_price']
			except:
				popup_tour_price = ""

				
			try:
			
				administration_fee_price = "" + request.POST['administration_fee_price']
			except:
				administration_fee_price = ""

				
			try:
			
				community_fund_price = "" + request.POST['community_fund_price']
			except:
				community_fund_price = ""

				
			try:
			
				popup_total_price = "" + request.POST['popup_total_price']
			except:
				popup_total_price = ""

			BODY_TEXT = (
							"firstName - {0} \n"
							"lastName - {1} \n"
							"email - {2} \n"
							"country - {3} \n"
							"country code - {4} \n"
							"phone number - {5} \n"
							"arrive - {6} \n"
							"departure - {7} \n"
							"guests - {8} \n"
							"accomodation_type - {9} \n"
							"vegetarian - {10} \n"
							"transportation - {11} \n\n\n"
							"accomodation and breakfast - {12} \n"
							"tour price - {13} \n"
							"administration fee - {14} \n"
							"communit fund - {15} \n"
							"total price - {16} \n"
					).format(firstName,lastName,email,country,country_code,phone_number,arrive,departure,guests,accomodation_type,veg,transportation,accomodation_and_breakfast,popup_tour_price,administration_fee_price,community_fund_price,popup_total_price)
			firstdate = request.POST['firstdate']


			try:
				totalPrice =int(float("{0:.2f}".format( float( request.POST['totalPrice']))) * 100)
			except:
				return render(request, 'accommodation/error.html')
			d1 = datetime.strptime(firstdate, '%Y-%m-%d')
			d2 = datetime.today().strftime('%Y-%m-%d')
			d3 = datetime.strptime(d2, '%Y-%m-%d')
		except:
			return render(request, 'accommodation/error.html')

		if abs((d1 - d3).days) < 11 :

			stripe.api_key = "sk_test_JdQREr7gPSnHRLieluCKmwnv00slD2xOlp"

			checkout_session = stripe.checkout.Session.create(
			success_url="https://example.com/success",
			cancel_url="https://example.com/cancel",
			payment_method_types=["card"],
			line_items=[
				{
				"name": "room",
				"description": "Comfortable ",
				"amount": totalPrice ,
				"currency": "usd",
				"quantity": 1,
				},
			],
			)
	

			context= {
			'CHECKOUT_SESSION_ID': checkout_session['id'],
			}
		


			return render(request, 'accommodation/pay.html', context)

		else:

			try:
				# Provide the contents of the email.
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
					# If you are not using a configuration set, comment or delete the
					# following line
					# ConfigurationSetName=CONFIGURATION_SET,
				)
			# Display an error if something goes wrong.
			except ClientError as e:
				print(e.response['Error']['Message'])
				return render(request, 'accommodation/error.html')
			else:
				firstName = request.POST['firstName']

				name = {
				'firstName': firstName,
				}
		
				
				print("Email sent! Message ID:"),
				print(response['MessageId'])
				return render(request, 'accommodation/success.html',name)
