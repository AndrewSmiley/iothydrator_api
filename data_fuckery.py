__author__ = 'andrewsmiley'
import datetime
#let's create some fuggin datapoints
#d = datetime.datetime(2009, 10, 5, 18, 00)
#>>> print d.year, d.month, d.day, d.hour, d.second

#start on monday
# current_time = datetime.datetime(2017,1,30,0,0,0)?





dps = [0,100,16,0,0,120,32,0,16,254,64,0,16,300,64,0,54,100]
total_keg= 1984
print "total ounces consumed: %s" %(sum(dps))
print "Ounces Per Hour %s" %(sum(dps)/(len(dps)*8))
oph = (sum(dps)/(len(dps)*8))
delta = total_keg-sum(dps)
print "hours to keg empty %s (%s day(s))"%(int(round(delta/oph)), int(round(delta/oph/24)))







