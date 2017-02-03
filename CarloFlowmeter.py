# SAMPLE_DELAY = 10.0
# next_sample = time.time() + SAMPLE_DELAY
# avg_flow = None
# SMOOTHING = 0.9
# pulses = 0
# last_pin_state = False
#
# #main loop
# while True:
# 	#Set Current Time
# 	currentTime = time.time()
# 	#Check if GPIO pin 22 is True and was previously False i.e. rising edge of pulse
# 	pin_state = GPIO.input(22)
# 	if pin_state and not last_pin_state:
# 		pulses += 1
# 	last_pin_state = pin_state
# 	if currentTime > next_sample:
#     	# check this isn't first time when avg_flow == None
# 		if avg_flow == None:
#       			avg_flow = pulses / SAMPLE_DELAY
# 		else:
# 			if (abs((pulses - avg_flow)/avg_flow) > 0.1):
# 				#send_email('emailaddress')
# 			avg_flow = pulses / SAMPLE_DELAY * SMOOTHING + avg_flow * (1.0 - SMOOTHING)
# 			print avg_flow
# 		pulses = 0
# 		next_sample = currentTime + SAMPLE_DELAY
# 	time.sleep(0.1)
#
# #################
# #PS for completeness
# # non-exponential moving avg using lists in python
# avg_list = None
# ..
#   if not avg_list:
#     avg_list = [pulses for i in range(5)]
#   avg_list = avg_list[1:] + [pulses]
#   avg_flow = sum(avg_list) / 5.0
#
