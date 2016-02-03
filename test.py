#coding:utf-8  
import sys,os  
from PIL import Image,ImageDraw  
import pytesseract

  
#测试代码  
def main(image_path):  
    im=Image.open(image_path)
    # print "image info,",im.format,im.mode,im.size  
    (w,h)=im.size  
    R=0  
    G=0  
    B=0  
  
    for x in xrange(w):  
        for y in xrange(h):  
            pos=(x,y)  
            rgb=im.getpixel( pos )
            (r,g,b,l)=rgb  
            R=R+r  
            G=G+g  
            B=B+b  
  
    rate1=R*1000/(R+G+B)  
    rate2=G*1000/(R+G+B)  
    rate3=B*1000/(R+G+B)  
      
    for x in xrange(w):  
        for y in xrange(h):  
            pos=(x,y)  
            rgb=im.getpixel( pos )  
            (r,g,b,l)=rgb  
            n= r*rate1/1000 + g*rate2/1000 + b*rate3/1000  
            #print "n:",n  
            if n>=196:  
                im.putpixel( pos,(255,255,255))  
            else:  
                im.putpixel( pos,(0,0,0))
    return im
  
  
if __name__ == '__main__':  
    image = main("./test/1.png")
    image.save("result.jpg")
    # image = image.convert("L") 
    result = pytesseract.image_to_string(image)
    print result