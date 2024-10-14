import speedtest
import time

i=0
bedingung = 0

print("Testing internet speed...")

def test_internet_speed():
    try:
        st = speedtest.Speedtest()        

        # Perform the download speed test
        download_speed = st.download() / 1000000  # Convert to Mbps

        # Perform the upload speed test
        upload_speed = st.upload() / 1000000  # Convert to Mbps

        # Print the results
        print("Download Speed: {:.2f} Mbps".format(download_speed))
        print("Upload Speed: {:.2f} Mbps".format(upload_speed))

    except speedtest.SpeedtestException as e:
        print("An error occurred during the speed test:", str(e))


while bedingung == 0:   
    test_internet_speed()
    print("-----------",end="\n")
    time.sleep(1)
    i +=1
    if i >=10:
        break