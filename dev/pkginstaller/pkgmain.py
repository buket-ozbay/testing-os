import urequests
import os
import time
import ujson
def package_installer(cmd_arr):
    url = ""
    try:
        params = cmd_arr[2].split(":")
        url = "https://raw.githubusercontent.com/gooz-project/gooz_packages/main/"+params[0]+"/"+params[1]+".json"
    except:
        url = "https://raw.githubusercontent.com/gooz-project/gooz_packages/main/"+cmd_arr[2]+"/"+"default.json"
    print(url)
    response_url = urequests.get(url)
    response_text = response_url.text
    print("Package recipe has been taken")
    time.sleep(0.5)
    response = ujson.loads(response_text)
    os.chdir("/")
    os.mkdir("/app/"+response["name"])
    for codes in response["codes"]:
        with open("/app/"+str(response["name"])+"/"+str(codes["filename"]),"w+",encoding='utf-8') as f:
            codes["code"] = codes["code"].replace("pkglineflag","\n")
            f.write(str(codes["code"]))
    os.chdir("/dev/pkginstaller")
    with open("/dev/pkginstaller/pkgmanager.py","a+",encoding='utf-8') as f:
        response["managersnip"] = response["managersnip"].replace("pkglineflag","\n")
        f.write(response["managersnip"])
    print("Package has been installed")

def package_uninstall(cmd_arr):
    try:
        os.chdir("/app/"+cmd_arr[2])
        files = os.listdir()
        for i in files:
            os.remove(i)
        os.rmdir("/app/"+cmd_arr[2])
        print("Package has been deleted")
        
    except:
        print("Package not found")