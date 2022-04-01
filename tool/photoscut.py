shang = int(input('请输入上剪裁像素: '))
xia = int(input('请输入下剪裁像素: '))
zuo = int(input('请输入左剪裁像素: '))
you = int(input('请输入右剪裁像素: '))
print('将把图片剪裁为: 横向'+str(zuo)+'~'+str(you)+' 纵向'+str(shang)+'~'+str(xia))
filesnames = os.listdir('.')
for name in filesnames:
    try:
        img = Image.open(name)
        cropped = img.crop((zuo, shang, you, xia))
        cropped.save("cut-{}".format(name))
    except:
        pass
