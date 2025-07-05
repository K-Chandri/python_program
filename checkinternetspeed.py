import speedtest
d_speed = speedtest.Speedtest()
print(f'{d_speed.download() /8000000:.2f}mb')

up_speed = speedtest.Speedtest()
print(f'{up_speed.upload() /8000000:.2f}mb')
