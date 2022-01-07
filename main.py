import requests

token = input("[>>] Input Token : ")

def check():
    headers = {
        "Content-Type": "application/json",
        "authorization": token
    }
    r = requests.get("https://discord.com/api/v6/users/@me", headers=headers)
    data = r.json()
    if r.status_code == 401:
        print("[>>] Invalid token")
        input()
    else:
        print(f"""
==================================================
User ID       : {data["id"]}
Username      : {data["username"]}
Avatar        : {data["avatar"]}
Discriminator : {data["discriminator"]}
Public Flags  : {data["public_flags"]}
Flags         : {data["flags"]}
Banner        : {data["banner"]}
Banner Color  : {data["banner_color"]}
Acent Color   : {data["accent_color"]}
User Bio      : {data["bio"]}
Locale        : {data["locale"]}
NSFW Allowed  : {data["nsfw_allowed"]}
MFA / 2FA     : {data["mfa_enabled"]}
Email         : {data["email"]}
Phone Number  : {data["phone"]}
==================================================""")
        input("[>>] Press 'Enter' to exit")

check()
