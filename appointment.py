# code to calculate the departure time for the user to arrive in time to the appointment.

appointment = int(input("What time is the appointment for? "))
hours = int(input("How many hours will it take? "))
traveltime = int(input("How long is the journey? "))

departure = appointment - traveltime
endtime = appointment + hours

appoint_str = str(appointment)
hours_str = str(hours)
depart_str = str(departure)
end_str = str(endtime)

output = "Your appointment is at " + appoint_str + " and will take " + hours_str + " hours. You should set off at " + depart_str + " it should be done by " + end_str

print
