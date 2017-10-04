from datetime import *

today = date.today() # today's date

# Other Deadlines:
#   KEY: # = to do; ## = done

##   A&M: October 15
##   GT: October 15
##   UVA: November 1
##   Michigan: November 1
##   Boulder: November 15
##   UDub: November 15
##   UT: December 1
##   Vandy: January 1

##   USAFA: November 1
##   USNA: January 31
#   USMA: ?
##   AFROTC: January 12
#   NROTC: ?

##################################################

cornyn_deadline = date(2017,10,6) # Cornyn's deadline
cornyn_diff = cornyn_deadline - today # days until Cornyn's deadline

cruz_deadline = date(2017,10,6) # Cruz's dealine
cruz_diff = cruz_deadline - today # days until Cruz's dealine

williams_deadline = date(2017,10,18) # Williams' deadline
williams_diff = williams_deadline - today # days until Williams' deadline

pence_deadline = date(2018,01,31) # Pence's deadline
pence_diff = pence_deadline - today # days until Pence's deadline

###################################################

af_deadline = date(2017,11,01) # USAFA deadline
af_diff = af_deadline - today # days until USAFA deadline

navy_deadline = date(2018,01,31) # USNA deadline
navy_diff = navy_deadline - today # days until USNA deadline

#army_deadline = date(??,??,??) # USMA deadline
#army_diff = army_deadline - today # days until USMA deadline

###################################################

afrotc_deadline = date(2018,01,12) # AFROTC deadline
afrotc_diff = afrotc_deadline - today # days until AFROTC deadline

###################################################

tamu_deadline = date(2017,10,15) # TAMU deadline
tamu_diff = tamu_deadline - today # days until TAMU deadline

gt_deadline = date(2017,10,15) # GT deadline
gt_diff = gt_deadline - today # days until GT deadline

uva_deadline = date(2017,11,01) # UVA deadline
uva_diff = uva_deadline - today # days until UVA deadline

um_deadline = date(2017,11,01) # Michigan deadline
um_diff = um_deadline - today # days until Michigan deadline

cu_deadline = date(2017,11,15) # Boulder deadline
cu_diff = cu_deadline - today # days until Boulder deadline

udub_deadline = date(2017,11,15) # UDub deadline
udub_diff = udub_deadline - today # days until UDub deadline

ut_deadline = date(2017,12,01) # UT deadline
ut_diff = ut_deadline - today # days until UT deadline

vandy_deadline = date(2018,01,01) # Vandy deadline
vandy_diff = vandy_deadline - today # days until Vandy deadline

###################################################

print "Today's Date:",today
print " "
print "NOMINATIONS:"
print "You have",cornyn_diff.days,"days to complete Senator Cornyn's Application."
print "You have",cruz_diff.days,"days to compelte Senator Cruz's Application."
print "You have",williams_diff.days,"days to complete Congressman Williams' Application."
print "You have",pence_diff.days,"days to complete Vice President Pence's Application."
print " "
print "SERVICE ACADEMIES:"
print "You have",af_diff.days,"days to complete your USAFA Application."
print "You have",navy_diff.days,"days to complete your USNA Application."
print " "
print "ROTC SCHOLARSHIPS:"
print "You have",afrotc_diff.days,"days to complete your AFROTC Application."
print " "
print "TRADITIONAL UNIVERSITIES:"
print "You have",tamu_diff.days,"days to complete your Texas A&M Application."
print "You have",gt_diff.days,"days to complete your Georgia Tech Applciation."
print "You have",uva_diff.days,"days to complete your University of Virginia Application."
print "You have",um_diff.days,"days to complete your University of Michigan Application."
print "You have",cu_diff.days,"days to complete your Univeristy of Colorado Boulder Application."
print "You have",udub_diff.days,"days to complete your University of Washington Application."
print "You have",ut_diff.days,"days to complete your University of Texas Application."
print "You have",vandy_diff.days,"days to complete your Vanderbilt University Application."
