import speedtest
import datetime
import numpy as np
import datetime
from time import time



def perform_speed_test():
   try:
      st = speedtest.Speedtest()
      servers = st.get_best_server()
      download_speed = st.download() / 1000000  # Convert to Mbps
      upload_speed = st.upload() / 1000000  # Convert to Mbps

   except:     # For the cases where there is no internet connection
      download_speed = 0
      upload_speed = 0
      time.sleep(10)
   return download_speed, upload_speed




if __name__ == "__main__":
	res = []
	try:
            while True: 
                  now = datetime.datetime.now()
                  download_speed, upload_speed = perform_speed_test()
                  res.append([str(now.replace(microsecond=0)),round(download_speed,3),round(upload_speed,3)])
                  print(res)
	except KeyboardInterrupt:
            np.array(res).dump(open('perfomanceTest.npy', 'wb'))
            pass
