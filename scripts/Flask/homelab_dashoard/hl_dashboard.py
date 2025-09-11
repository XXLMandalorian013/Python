# region read me
# URL https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application
#endregion
# region script
# importing the Flask library and adding the render_template to combine .py + html.
from flask import Flask, render_template
# a var to let flask know where my application is.
web_page = Flask(__name__)
# python list with dictionary urls for the webpage.
urls = [
    {"name": "Firewall", "url": "https://192.168.1.2", "icon": "firewall.png"},
    {"name": "Pi-hole 1", "url": "http://192.168.1.3/admin", "icon": "pihole.png"},
    {"name": "Pi-hole 2", "url": "http://192.168.1.4/admin", "icon": "pihole.png"},
    {"name": "TrueNAS", "url": "https://192.168.1.5", "icon": "truenas.png"},
    {"name": "Proxmox", "url": "https://192.168.1.6:8006", "icon": "proxmox.png"},
]
# function that renders the library above.
@web_page.route("/")
def dashboard():
    return render_template("dashboard.html", urls=urls)
# starts the flash web server.
if __name__ == "__main__":
    web_page.run(debug=True, host="0.0.0.0")
#endregion