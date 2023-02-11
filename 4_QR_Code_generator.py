import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=xTLK0iHLxFs&list=PLsXdBvuJ5ox7U8HipGaQoS95fFcIhKRRS&index=1")
img.save("spokenguru.png")