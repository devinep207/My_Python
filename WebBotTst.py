#Patrick Devine
#CS in action


from webbot import Browser
web = Browser()
web.go_to('liveme.com')
web.click('Register')
web.click('Enter your phone number')
web.type('7777777777' )
web.click('Password should be 6~20 characters')
web.type('NeverGonnaGetIt' )
web.click('Enter verify code')
web.type('5555555' )


#I fixed this code and got it working after installing anaconda
#This automates the registration for an account for site
