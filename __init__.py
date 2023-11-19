def run():
  from hype import Hype
  import asyncio
  import os
  from datetime import date
  from dotenv import load_dotenv
  import json

  load_dotenv()
  hype_instance = Hype()

  year = int(os.environ.get('YEAR'))
  month = int(os.environ.get('MONTH'))
  day = int(os.environ.get('DAY'))

  username = os.environ.get('HYPE_USR')
  password= os.environ.get('HYPE_PSW')
  birthdate = date(year, month, day)


  asyncio.run(hype_instance.login(username, password, birthdate))
  otp = input('Insert the code you recieved via SMS...')
  asyncio.run(hype_instance.otp2fa(otp))
  movements = asyncio.run(hype_instance.get_movements(99999))
  
  json_object = json.dumps(movements)
 
  with open("sample.json", "w") as outfile:
    outfile.write(json_object)


if __name__ == '__main__':
  run()

