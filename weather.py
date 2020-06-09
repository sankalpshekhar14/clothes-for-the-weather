import pyowm
from datetime import datetime, timedelta

#Function that provides the description
def get_descript(owm,a):

	#Get Weather details

	w=owm.weather_at_place(a)
	record=w.get_weather()
	temp=record.get_temperature()['temp_min']
	wind=record.get_wind()['speed']
	clouds=record.get_clouds()

	try:
		rain=record.get_rain()['1h']

	except KeyError:
		rain=0
	#The Description
	result="The overall description of the weather is as follows.\n"

	if clouds<20:
		result=result+"It should be sunny, so hats and sunglasses might be needed.\n"
	if wind>30:
		result=result+"There'll be wind, so a jacket might be useful.\n"
	elif wind>10:
		result=result+"There will be a light breeze, so long sleeves might be handy.\n"
	if temp<=273:
		result=result+"There will be extreme cold. A thick coat is necessary.\n"
	elif temp<283:
		result=result+"Cold weather expected. A jumper will be needed.\n"
	elif temp<293:
		result=result+"Pleasant weather. A light jumper might be useful.\n"
	else:
		result=result+"Normal summer clothing will be enough.\n"
	if rain==0:
		result=result+"It is not going to rain. So an umbrella is not necessary.\n"
	elif rain/3<2.5:
		result+="There will be light rain, consider carrying a hood or an umbrellla.\n"
	elif rain/3<7.6:
		result+="There will be moderate rain, an umbrella might be needed.\n"
	elif rain/3<50:
		result+="There will be heavy rain, an umbrella or a jacket is necessary.\n"
	elif rain/3>50:
		result+="There is a thunderstorm, avoid going outdoors.\n"
	#Generate Report
	report={'Location': a,
	'Temp':temp,
	'Clouds':clouds,
	'Wind': wind,
	'Rain': rain,
	'Date':datetime.now(),
	'Description':result
	}

	#Return the description and report
	return result,report



#Set API Key
API_KEY=''
owm = pyowm.OWM(API_KEY)



details=input("Enter the city you plan to visit\n")
#Function Call
result,report=get_descript(owm,details)
print(result)

choice=input("Do you want to save the suggestions?(Y/N)\n")

if(choice=='Y' or choice=='y'):
	file=open('report.txt','a')
	for tag in report:
		file.write(tag+' : '+str(report[tag])+'\n')
	file.close()