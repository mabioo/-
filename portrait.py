#encoding:utf-8

from PIL import Image    #PIL为python的图形处理模块，此例中通过Image来读取文件
import argparse     #python的命令行参数处理模块，此例中用来进行捕获输入输出文件以及长度和宽度等

parser = argparse.ArgumentParser()    #获取命令参数
parser.add_argument('files')   #输入文件，后通过parse.args()获取并通过args.file来获取
parser.add_argument('-o', '--output')   #输出文件 ，可以通过-o或--output进行获取
parser.add_argument('-width', type=int , default=80)      #same as last
parser.add_argument('-height', type=int, default = 80)

#获取参数
args = parser.parse_args()    #添加获取参数

IMG = args.files
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

symbol = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def getchar(r,g,b,alpha = 256):
    if alpha == 0:
        return  ' yy'
    grep = (0.2126 * r + 0.7152 * g + 0.0722 * b )
    length = len(symbol)
    unit = (256.0 + 1)/length
    return symbol[int(grep/unit)]

if __name__ == '__main__':
    print "1"
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += getchar(*im.getpixel((j,i)))
        txt +='\n'
    print txt

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)












