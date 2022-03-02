
paper = {
  1:{'path':'data/paper1.jpg','px':500,'py':420,'line':25,'perEnter':135,'header':{'px':450,'py':60,'perEnter':90},'date':{'px':2330,'py':180}}, #done

  2:{'path':'data/paper2.jpg','px':585,'py':390,'line':31,'perEnter':115,'header':{'px':460,'py':90,'perEnter':70},'date':{'px':2300,'py':210}}
    #done
}
font = {
  1:{'path':'data/font1.ttf', 'size':65, 'color':(49, 50, 50),'max':{1:86,2:80}},
  2:{'path':'data/font2.ttf', 'size':70, 'color':(42, 43, 43),'max':{1:97,2:92}}
}

class BotNulis:
  def __init__(self,text,indexPaper,indexFont,header,date):
    self.text = text
    self.papernumber = indexPaper
    self.nomerFont = indexFont
    self.mpaper = paper[indexPaper]
    self.pfont = font[indexFont]
    self.header =header
    self.date = date

  def start(self):
    self.paper = Image.open(self.mpaper['path'])
    self.draw = ImageDraw.Draw(self.paper)
    self.myfont = ImageFont.truetype(self.pfont['path'],self.pfont['size'])
    return self.prosesText()

  def prosesText(self):
    splitEnter = self.text.split('\n')
    numberEnter = len(splitEnter)
    if numberEnter>self.mpaper['line']:
      response = {'error':True,'msg':'Excess row count, your row: '+str(numberenter)+'. While the max line of this paper: '+str(self.mpaper['line'])}
      return response
    else:
      self.textPerLine = []
      maxKarakter = self.pfont['max'][int(self.papernumber)]
      for line in splitEnter:
        longline = len(line)
        while longline>maxKarakter:
          self.textPerLine.append(line[:maxKarakter])
          line = line[maxKarakter:]
          longline-=maxKarakter
        else:
          self.textPerLine.append(line)

      if len(self.textPerLine)>self.mpaper['line']:
        return {'error':True,'msg':'Excess row count, your row: '+str(numberenter)+'. While the max line of this paper: '+str(self.mpaper['line'])}

      return self.nulis()


  def nulis(self):
    if self.header != '':
      px = self.mpaper['header']['px']
      py = self.mpaper['header']['py']
      splitHeader = self.header.split('\n')
      for line in splitHeader:
        self.draw.text((px, py), line, font=self.myfont, fill = self.pfont['color'])
        py += self.mpaper['header']['perEnter']

    if self.date != '':
      px = self.mpaper['date']['px']
      py = self.mpaper['date']['py']
      self.draw.text((px, py), self.date, font=self.myfont, fill = self.pfont['color'])

    px = self.mpaper['px']
    py = self.mpaper['py']

    for text in self.textPerLine:
      self.draw.text((px, py), text, font=self.myfont, fill = self.pfont['color'])
      py+=self.mpaper['perEnter']

    self.location = 'results/'+waktuFile+'-yuu-nulis.jpg'
    self.paper = self.paper.resize((1560,2080))
    self.paper.save(self.location)
    return self.upload()

  def upload(self):
    url = 'https://api.imgbb.com/1/upload'
    files = {'image': open(self.location, 'rb')}
    data = {
      'key':'16d491691c9c5976c122a0bcc344346c'
      }
    response = requests.request('POST',url,data=data,files=files)
    result = response.json()
    self.urlResult = result['data']['url']
    os.remove(self.location)
    return {'error':False,'file':self.urlResult,'msg':'Muhehehehe -yuu-nulis'}
