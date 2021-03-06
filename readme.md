##Smart Keg API

####*GET*  
**`/v1/start_pour/<volume>/<user_id>/`**  
Begin a pour cycle. Once a pour cycle has started, it will shut off in the device once the specified pour volume has been reached.  

#####*Parameters*
**`volume`**: a volume to pour  
**`user_id`**: the ID of the user issuing the pour. See **`/v1/authenticate/`**

#####*Example Response*
```
{  
    "result": true
    "pour_id": 1
}  
```  
**`result`**: the success of the pour
**`pour_id`**: the id of the pour started

####*GET*
**`/v1/stop_pour/`**  
Stop the current pour cycle manually, i.e. close the solenoid. 
  
#####*Example Response*
```
{  
    "result": true  
}  
```  
**`result`**: the success of the stop

####*GET*
**`/v1/pour_status/<pour_id>/`**  
Get the status of the specified pour. If no pour is specified, the latest pour will be used.

#####*Parameters*
**`pour_id`**: the id of the pour to get the status of

#####*Example Response*
```
{
	"status": "Completed",
	"volume_expected": 32,
	"percentage": 5,
	"result": true,
	"volume_poured": "30"
}
```

**`result`**: the success of the action  
**`percentage`**: the percentage completion of the pour
**`status`**: the status of the pour
**`volume_expected`**: the volume expected in the pour
**`volume_poured`**: the volume poured 


####*GET*
**`/v1/authenticate/<sso>/`**  
Authenticate to the system as a specific user using the badge reader

#####*Parameters*
**`sso`**: the sso of the user we are authenticating as

#####*Example Response*
```
{
	"result": true,
	"id": 1
}
```

**`result`**: the success of authentication  
**`id`**: the id of the user we authenticated as

####*GET*
**`/v1/system_info/`**  
Fetch system status information as JSON

#####*Example Response*
```
{
	"health": {
		"keg": {
			"percentage": 100,
			"temperature": 50
		},
		"sensors": {
			"pressure_sensor": {
				"ps2": true,
				"ps0": true,
				"ps1": true
			},
			"flowmeter": true,
			"thermo": true
		},
		"c02": {
			"percentage": 100
		}
	},
	"result": true
}
```
**`result`**: the success of the system check  
**`health`**: a dictionary of system statuses, boolean values indicate on/off and integers indicate percentages

####*GET*
**`/v1/pour_history/`**  
Fetch the pour history

#####*Example Response*
```
{
	"pours": [{
		"status": "Completed",
		"timestamp": "123456783",
		"user_id": 1,
		"user_full_name":"Andrew Smiley",
		"pour_id": 1
	}, {
		"status": "Completed",
		"timestamp": "123456783",
		"user_id": 2,
		"user_full_name":"Andrew Smiley",
		"pour_id": 2
	}],
	"result": true
}
```

**`result`**: the success of fetch  
**`pours`**: a list of pours and their status, timestamp, user_id, full name and volume

####*GET*
**`/v1/user_photo/<user_id>`**  
Fetch the pour history

#####*Parameters*
**`user_id`**: the id of the user we wish to fetch a photo for

#####*Example Response*
![alt text](https://f4.bcbits.com/img/0003428886_10.jpg "Rum Ham")

This returns no json, only an image


####*GET*
**`/v1/user_info/<user_id>`**  
Fetch the specified user information based upon id passed

#####*Parameters*
**`user_id`**: the id of the user we wish to fetch information for

#####*Example Response*
```
{
	"sso": "212543871",
	"last_name": "Smiley",
	"result": true,
	"first_name": "Andrew"
}
```

**`result`**: the success of the user fetch  
**`last_name`**: the last name of the user  
**`first_name`**: the first name of the user
**`sso`**: the sso of the user


####*GET*
**`/v1/dt/overview/`**  
Fetch the Digital Twin information as JSON

#####*Example Response*
```
{
	"days_in_lines": 45,
	"days_in_keg": 3,
	"result": "true",
	"days_in_c02": 6
}
```
**`result`**: the success of the digital twin data generation  
**`days_in_lines`**: the number of days remaining until we need to replace the lines  
**`days_in_keg`**: the number of days remaining until we need to replace the keg  
**`days_in_c02`**: the number of days remaining until we need to replace the c02


####*GET*
**`/v1/dt/omt/`**  
Fetch the Digital Twin information as JSON

#####*Example Response*
```
{
	"omt_start": "6PM",
	"result": "true",
	"omt_end": "7AM"
}
```
**`result`**: the success of the digital twin optimal maintenance time range  
**`omt_start`**: the start of the optimal maintenance range  
**`omt_end`**: the end of the optimal maintenance range





