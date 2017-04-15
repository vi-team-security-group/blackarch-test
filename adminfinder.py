#/usr/bin/python
# This was written for educational purpose only. Use it at your own risk.
# Author will be not responsible for any damage!
# !!! Special greetz for my friends Vi Team !!!
# !!! Special thanx for Vi team and rsauron who inspired me !!! 
###########################################################################

#################################################################### 
#                                                                  #
#   __   __   __        ______   ______     ______     __    __    #
#  /\ \ / /  /\ \      /\__  _\ /\  ___\   /\  __ \   /\ "-./  \   #
#  \ \ \'/   \ \ \     \/_/\ \/ \ \  __\   \ \  __ \  \ \ \-./\ \  #
#   \ \__|    \ \_\       \ \_\  \ \_____\  \ \_\ \_\  \ \_\ \ \_\ #
#    \/_/      \/_/        \/_/   \/_____/   \/_/\/_/   \/_/  \/_/ #
#                                                                  #
####################################################################
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
#  Based on Web admin locator by  Master Vi    #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #
#                                              #       
#                                              #
#                                              #
################################################



import sys, os, time, httplib

if sys.platform == 'linux' or sys.platform == 'linux2':
	clearing = 'clear'
else:
	clearing = 'cls'
os.system(clearing)


if len(sys.argv) != 2:
	print "\n|---------------------------------------------------------------|"
        print "| mastervi@mail.bg                                                |"
        print "|   04/2017     Admin login finder     v2.1                       |"
	print "| Help: adminfinder.py -h                                         |"
	print "|                                                                 |"
        print "|---------------------------------------------------------------|\n"
	sys.exit(1)
	
for arg in sys.argv:
	if arg == '-h':
		print "\n|-------------------------------------------------------------------------------|"
                print "| mastervi@mail.bg                                                                |"
                print "|   04/2017      Admin login finder     v2.1                                      |"
                print "| Usage: adminfinder.py www.site.com                                              |"
	        print "| Example: adminfinder.py site.com                                                |"
	        print "| Visit  https://github.com/vi-team-security-group/blackarch-test                 |"
                print "|-------------------------------------------------------------------------------|\n"
		sys.exit(1)
	
	

site = sys.argv[1].replace("http://","").rsplit("/",1)[0] 
site = site.lower()

admin_path = ['admin.php','admin/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php','joomla/administrator','login.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html','admin/controlpanel.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html','admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php','administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php','bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','modelsearch/login.php','moderator.php','moderator/login.php','moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html','webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html','administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html','panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','adminarea/index.php','adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']


print "\n|---------------------------------------------------------------|"
print "| mastervi@mail.bg                                                |"
print "|   03/2009      Admin login finder     v2.1                      |"
print "| Visit https://github.com/vi-team-security-group/blackarch-test  |"
print "|---------------------------------------------------------------|\n"
print "\n[-] %s" % time.strftime("%X")
		
print "[+] Target:",site
print "[+] Checking paths..."
print


try:
	for admin in admin_path:
		admin = admin.replace("\n","")
		admin = "/" + admin
		connection = httplib.HTTPConnection(site)
		connection.request("GET",admin)
		response = connection.getresponse()
		print "%s %s %s" % (admin, response.status, response.reason)
except(KeyboardInterrupt,SystemExit):
		raise
except:
		pass
