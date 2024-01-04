from __appsignal__ import appsignal
appsignal.start()
print("STARTING APP SIGNAL!")

from project import create_app

app = create_app()