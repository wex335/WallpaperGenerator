from PIL import Image
res = (5000,3000)
bg=Image.open('back.png')
bg_w, bg_h = bg.size
background = Image.new('RGB', res)
w, h = background.size
for i in range(0, w, bg_w):
    for j in range(0, h, bg_h):
        #bg = Image.eval(bg, lambda x: x+(i+j)/1000)
        background.paste(bg, (i, j))
print('bg inited')
import random
for i in range(3000):
    pim = Image.open(f'stickers/{random.randrange(1,61)}.png').convert("RGBA")
    grad = random.randrange(90,110)
    p = pim.rotate(random.randrange(-10,10)).resize((int(pim.width*grad/100),int(pim.height*grad/100)))
    px = random.randrange(int(-p.width/2),res[0])
    py = random.randrange(int(-p.height/2),res[1])
    background.paste(p,(px, py),p)
    print(i)
#background.show()
background.save('img.png')