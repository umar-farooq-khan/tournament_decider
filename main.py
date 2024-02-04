import re
import json
import easyocr
import cv2
import glob
import os
bluedataheader=[]
reddatacol1=[]
reddataheader=[]
bluedata=[]
reddata=[]

playername=[]
def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def nowdoocr(crop1_1, crop1_2):
    crop1_1result = reader.readtext(crop1_1, detail=0)
    crop1_2result = reader.readtext(crop1_2, detail=0)
    try:
        crop1_2result[0].remove('P')
    except ValueError:
        pass
    try:
        crop1_1result[0].remove('MVP')
    except ValueError:
        pass
    try:
        crop1_2result[0].remove('MVP')
    except ValueError:
        pass
    try:
        crop1_1result[0].remove('MATCH DETAILS')
    except ValueError:
        pass
    try:
        crop1_1result[0].remove('DEFEAT')
    except ValueError:
        pass
    try:
        crop1_1result[0].remove('DETAIL REPORT')
    except ValueError:
        pass
    try:
        crop1_1result[0].remove('VICTORY')
    except ValueError:
        pass
    try:
        while True:
            crop1_1result[0].remove('150')
    except ValueError:
        pass
    try:
        crop1_1result[0].remove('SHARE')
    except ValueError:
        pass
    try:
        crop1_1result[0].remove('gaMeRS')
    except ValueError:
        pass

    values = crop1_1result[0]
    values1_2 = crop1_2result[0]

    # #print('Raw Value', values)
    ##print('Raw Value for data column', values1_2)

    scoremap = values[0]
    modemap = values[1]
    if ('2' in values):
        pl2 = int(values.index('2')) - 1
        playername.append(values[pl2])
    if ('3' in values):
        pl3 = int(values.index('3')) - 1
        playername.append(values[pl3])
    if ('4' in values):
        pl4 = int(values.index('4')) - 1
        playername.append(values[pl4])
    if ('5' in values):
        pl5 = int(values.index('5')) - 1
        playername.append(values[pl5])
    else:
        print('two 3 not found in it')

    #print('Scoremap: ', scoremap)
    #print('Modemap: ', modemap)
    #print('player name: ', playername)
    bluedata.append(playername)
    #print('bluedata list now became: ', bluedata)
    for i in range(0, 5):
         if(len(values1_2[i])>3):
                 pattern = re.compile("[A-Za-z]\S+")
                 if pattern.fullmatch(values1_2[i].strip()) is not None:
                     #print("Found match: " + values1_2[i])
                     bluedataheader.append(values1_2[i])
                 else:
                     pass

    headerlen=len(bluedataheader)
    chunk_size = headerlen
    listofdata=list(split(values1_2, chunk_size))
    for i in range(0, len(listofdata)):
        bluedatacol1.append(listofdata[i])
        tableheader.append(bluedataheader)
    #print('headers/column names', bluedataheader)
    # for i in range(1,len(bluedatacol1)):
    #     bluedata.append(bluedatacol1[i])
        #print('row'+ str(i)+  '--',bluedatacol1[i])
    #

    #print('bluedatacol1 here')
    #print(bluedatacol1)
    bluedata.append(bluedatacol1[1: len(bluedatacol1)])
    #print('bluedata now became after putting cols too: ')
    #print(bluedata)
    aList = [
        {'Score': scoremap,
            'Modemap': modemap,
              'TableHeader': bluedataheader,
             'Bluedata': bluedata
         }
    ]

    jsonStr = json.dumps(aList)
    #print(jsonStr)
    bluedata.clear()
    bluedatacol1.clear()
    bluedataheader.clear()
    playername.clear()
    tableheader.clear()
    return jsonStr


allimages=glob.glob(r'C:\Users\umaRf\Downloads\New folder (2)\*')
#other file than images.
#print(allimages)
reader = easyocr.Reader(['en'])
crop1_result=[]
crop2_result=[]
tableheader=[]
bluedatacol1=[]
bluedatacol2=[]
bluedatacol3=[]
bluedatacol3=[]
bluedatacol4=[]
bluedatacol5=[]
i=0
lenn=len(allimages)


def ocrpage2(jsonobj, crop2_1, crop2_2):
    crop2_1result = reader.readtext(crop2_1, detail=0)
    crop2_2result = reader.readtext(crop2_2, detail=0)
    result= crop2_1result[0]
    result2_2= crop2_2result[0]
    try:
        while True:
            result.remove('150')
    except ValueError:
        pass

    try:
        result.remove('MVP')
    except ValueError:
        pass

    try:
        while True:
            result2_2.remove('150')
    except ValueError:
        pass

    try:
        result2_2.remove('MVP')
    except ValueError:
        pass


    # indexx= result2_2.index('PLAYER')
    # print(indexx)
    # result2_2=result2_2[indexx: len(result2_2)]
    try:
        while True:
            result.remove('150')
    except ValueError:
        pass

    try:
        result.remove('MVP')
    except ValueError:
        pass

    #print(result)

    for i in range(0, len(result)):
        if(result[i]== 'PLAYER'):
            playername.append(result[i+1])
            #print('player name added', result[i+1])

    if ('2' in result):
        pl2 = int(result.index('2')) - 1
        playername.append(result[pl2])
    if ('3' in result):
        pl3 = int(result.index('3')) - 1
        playername.append(result[pl3])
    if ('4' in result):
        pl4 = int(result.index('4')) - 1
        playername.append(result[pl4])
    if ('5' in result):
        pl5 = int(result.index('5')) - 1
        playername.append(result[pl5])
    else:
        print('two 3 not found in it')
    reddata.append(playername)
    #print('player name: ', playername)
    #print('Raw data page2_2', result2_2)
    try:
        for i in range(0, 10):
            if (len(result2_2[i]) > 3):
                pattern = re.compile("[A-Za-z]\S+")
                if pattern.fullmatch(result2_2[i].strip()) is not None:
                    # print("Found match: " + values1_2[i])
                    bluedataheader.append(result2_2[i])
                else:
                    pass

        headerlen=len(bluedataheader)
        chunk_size = headerlen
        listofdata=list(split(result2_2, chunk_size))
        for i in range(0, len(listofdata)):
            bluedatacol1.append(listofdata[i])
        #print('headers/column names', bluedataheader)
        #for i in range(1,len(bluedatacol1)):
            #reddata.append(bluedatacol1[i])
            #print('row'+ str(i)+  '--',bluedatacol1[i])
    except IndexError:
        pass

    reddata.append(bluedatacol1[1:len(bluedatacol1)])
    #print('red data after adding row data:')
    #print('redata including pplayer name')
    #print(reddata)
    #print('complete red dat')
    #print(reddata)
    bList = [
        {
            'Reddata': reddata
        }
    ]

    jsonStr = json.dumps(bList)
    print(jsonobj+jsonStr)

    reddatacol1.clear()
    bluedatacol1.clear()
    bluedataheader.clear()
    reddataheader.clear()

    reddata.clear()
    playername.clear()





for img in allimages:
        tableheader.clear()
        image = cv2.imread(img)
        #page1
        rows1, cols1, _ = image.shape
        crop1=image[0:int((rows1)),     0: int((cols1)/2)]
        crop2=image[0: int((rows1)),     int((cols1)/2): int(cols1)]
        rows1, cols1, _ = crop1.shape
        crop1_1= crop1[0:int((rows1)),     0: int((cols1)/2.3)]
        crop1_2= crop1[int((rows1)/8):int((rows1)),    int((cols1)/2.3): int((cols1))]

        #page 2
        rows1, cols1, _ = crop2.shape
        crop2_1= crop2[0:int((rows1)),     0: int((cols1)/2.3)]
        crop2_2= crop2[int((rows1)/7):int((rows1)),   int((cols1)/2.3) : int((cols1))]
        os.chdir(r"C:\Users\umaRf\OneDrive\Desktop\cropped")
        filename = str(img)
        #cv2.imwrite(filename +'cropped' +'.png', crop2_2)
        #cv2.imwrite(filename +'2_2' +'.png', crop2_2)
        #cv2.imwrite(img+'_crop2.png', crop2)
        #print(img)

        jsonobj=nowdoocr(crop1_1, crop1_2)
        ocrpage2(jsonobj, crop2_1,crop2_2)
        #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

