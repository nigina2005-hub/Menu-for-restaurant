from tkinter import *
from tkinter import ttk
'''root1=Tk()
root1.overrideredirect(1)
root1.state('zoomed')
root1.title('Меню')
root1.iconbitmap(default='foto1.ico')
#root1.geometry('1350x800')
root1['bg']='white'
python_logo=PhotoImage(file='foto.png')
lb=ttk.Label(image=python_logo)
lb.place(x=400,y=80)

#et={'et11':0,'et12':0,'et13':0,'et14':0,'et15':0,'et16':0,'et17':0,'et18':0,'et21':0,'et22':0,'et23':0,'et24':0,'et25':0,'et26':0,'et27':0,'et28':0,'et31':0,'et32':0,'et33':0,'et34':0,'et35':0,'et36':0,'et37':0,'et38':0,'et41':0,'et42':0,'et43':0,'et44':0,'et45':0,'et46':0,'et47':0,'et48':0,'et51':0,'et52':0,'et53':0,'et54':0,'et55':0,'et56':0,'et57':0,'et58':0,'et61':0,'et62':0,'et63':0,'et64':0,'et65':0,'et66':0,'et67':0,'et68':0,'et71':0,'et72':0,'et73':0,'et74':0,'et75':0,'et76':0,'et77':0,'et78':0,'et81':0,,'et82':0,'et83':0,'et84':0,'et85':0,'et86':0,'et87':0,'et88':0,'et91':0,'et92':0,'et93':0,'et94':0,'et95':0,'et96':0,'et97':0,'et98':0,'et101':0,'et102':0,'et103':0,'et104':0,'et105':0,'et106':0,'et107':0,'et108':0,'et111':0,'et112':0,'et113':0,'et114':0,'et115':0,'et116':0,'et117':0,'et118':0,'et121':0,'et122':0,'et123':0,'et124':0,'et125':0,'et126':0,'et127':0,'et128':0,'et131':0,'et132':0,'et133':0,'et134':0,'et135':0,'et136':0,'et137':0,'et138':0}
#print(et['et11'])
def viyti():
    #root.destroy()
    root1.destroy()
bn1 = Button(root1, text='Выйти', command=viyti, bg="cyan", font=("Times New Roman", 13, 'bold'), width=15, height=2)
bn1.place(x=1150, y=220)'''





def menu():
    global nig

    #root1.withdraw()
    root=Tk()
    root.overrideredirect(1)
    root.state('zoomed')
    root.title('Меню')
    root.iconbitmap(default='foto1.ico')
    root.geometry('1350x800')
    root['bg'] = 'white'
    '''with open('menu_basa.txt','a') as file:
            print(' Основное_блюдо\n'+' Цена_блюдо\n'+' Салаты\n'+' Цена_салатов\n'+' Десерты\n'+' Цена_десертов\n'+' Напитки\n'+' Цена_напитков ',file=file)
            print('dx\n'+str(1200)+'\n'+'dy\n'+str(100),file=file)'''
    nig = {'et11': 0, 'et12': 0, 'et13': 0, 'et14': 0, 'et15': 0, 'et16': 0, 'et17': 0, 'et18': 0, 'et21': 0, 'et22': 0,
          'et23': 0, 'et24': 0, 'et25': 0, 'et26': 0, 'et27': 0, 'et28': 0, 'et31': 0, 'et32': 0, 'et33': 0, 'et34': 0,
          'et35': 0, 'et36': 0, 'et37': 0, 'et38': 0, 'et41': 0, 'et42': 0, 'et43': 0, 'et44': 0, 'et45': 0, 'et46': 0,
          'et47': 0, 'et48': 0, 'et51': 0, 'et52': 0, 'et53': 0, 'et54': 0, 'et55': 0, 'et56': 0, 'et57': 0, 'et58': 0,
          'et61': 0, 'et62': 0, 'et63': 0, 'et64': 0, 'et65': 0, 'et66': 0, 'et67': 0, 'et68': 0, 'et71': 0, 'et72': 0,
          'et73': 0, 'et74': 0, 'et75': 0, 'et76': 0, 'et77': 0, 'et78': 0,'et81': 0, 'et82':0, 'et83': 0, 'et84': 0,
          'et85': 0, 'et86': 0, 'et87': 0, 'et88': 0, 'et91': 0, 'et92': 0, 'et93': 0, 'et94': 0, 'et95': 0, 'et96': 0,
          'et97': 0, 'et98': 0, 'et101': 0, 'et102': 0, 'et103': 0, 'et104': 0, 'et105': 0, 'et106': 0, 'et107': 0,
          'et108': 0, 'et111': 0, 'et112': 0, 'et113': 0, 'et114': 0, 'et115': 0, 'et116': 0, 'et117': 0, 'et118': 0,
          'et121': 0, 'et122': 0, 'et123': 0, 'et124': 0, 'et125': 0, 'et126': 0, 'et127': 0, 'et128': 0, 'et131': 0,
          'et132': 0, 'et133': 0, 'et134': 0, 'et135': 0, 'et136': 0, 'et137': 0, 'et138': 0}

    with open('menu_basa.txt', 'r') as file:
        st1 = file.readlines()
    nig['et11']=st1[8]
    nig['et12']=st1[9]
    nig['et13']=st1[10]
    nig['et14']=st1[11]
    nig['et15']=st1[12]
    nig['et16']=st1[13]
    nig['et17']=st1[14]
    nig['et18']=st1[15]

    nig['et21']=st1[16]
    nig['et22']=st1[17]
    nig['et23']=st1[18]
    nig['et24']=st1[19]
    nig['et25']=st1[20]
    nig['et26']=st1[21]
    nig['et27']=st1[22]
    nig['et28']=st1[23]

    nig['et31']=st1[24]
    nig['et32']=st1[25]
    nig['et33']=st1[26]
    nig['et34']=st1[27]
    nig['et35']=st1[28]
    nig['et36']=st1[29]
    nig['et37']=st1[30]
    nig['et38']=st1[31]

    nig['et41']=st1[32]
    nig['et42']=st1[33]
    nig['et43']=st1[34]
    nig['et44']=st1[35]
    nig['et45']=st1[36]
    nig['et46']=st1[37]
    nig['et47']=st1[38]
    nig['et48']=st1[39]

    nig['et51']=st1[40]
    nig['et52']=st1[41]
    nig['et53']=st1[42]
    nig['et54']=st1[43]
    nig['et55']=st1[44]
    nig['et56']=st1[45]
    nig['et57']=st1[46]
    nig['et58']=st1[47]

    nig['et61']=st1[48]
    nig['et62']=st1[49]
    nig['et63']=st1[50]
    nig['et64']=st1[51]
    nig['et65']=st1[52]
    nig['et66']=st1[53]
    nig['et67']=st1[54]
    nig['et68']=st1[55]

    nig['et71']=st1[56]
    nig['et72']=st1[57]
    nig['et73']=st1[58]
    nig['et74']=st1[59]
    nig['et75']=st1[60]
    nig['et76']=st1[61]
    nig['et77']=st1[62]
    nig['et78']=st1[63]

    nig['et81']=st1[64]
    nig['et82']=st1[65]
    nig['et83']=st1[66]
    nig['et84']=st1[67]
    nig['et85']=st1[68]
    nig['et86']=st1[69]
    nig['et87']=st1[70]
    nig['et88']=st1[71]

    nig['et91']=st1[72]
    nig['et92']=st1[73]
    nig['et93']=st1[74]
    nig['et94']=st1[75]
    nig['et95']=st1[76]
    nig['et96']=st1[77]
    nig['et97']=st1[78]
    nig['et98']=st1[79]

    nig['et101']=st1[80]
    nig['et102']=st1[81]
    nig['et103']=st1[82]
    nig['et104']=st1[83]
    nig['et105']=st1[84]
    nig['et106']=st1[85]
    nig['et107']=st1[86]
    nig['et108']=st1[87]

    nig['et111']=st1[88]
    nig['et112']=st1[89]
    nig['et113']=st1[90]
    nig['et114']=st1[91]
    nig['et115']=st1[92]
    nig['et116']=st1[93]
    nig['et117']=st1[94]
    nig['et118']=st1[95]

    nig['et121']=st1[96]
    nig['et122']=st1[97]
    nig['et123']=st1[98]
    nig['et124']=st1[99]
    nig['et125']=st1[100]
    nig['et126']=st1[101]
    nig['et127']=st1[102]
    nig['et128']=st1[103]

    nig['et131']=st1[104]
    nig['et132']=st1[105]
    nig['et133']=st1[106]
    nig['et134']=st1[107]
    nig['et135']=st1[108]
    nig['et136']=st1[109]
    nig['et137']=st1[110]
    nig['et138']=st1[111]

    lb1 = ttk.Label(root, text=st1[0], width=15, font=('Time New Roman', 14), background='cyan' )
    lb1.place(x=10, y=50)
    lb2 = ttk.Label(root, text=st1[1], width=15, font=('Time New Roman', 14), background='cyan' )
    lb2.place(x=180, y=50)
    lb3 = ttk.Label(root, text=st1[2], width=15, font=('Time New Roman', 14), background='cyan' )
    lb3.place(x=350, y=50)
    lb4 = ttk.Label(root, text=st1[3], width=15, font=('Time New Roman', 14), background='cyan' )
    lb4.place(x=520, y=50)
    lb5 = ttk.Label(root, text=st1[4], width=15, font=('Time New Roman', 14), background='cyan' )
    lb5.place(x=690, y=50)
    lb6 = ttk.Label(root, text=st1[5], width=15, font=('Time New Roman', 14), background='cyan' )
    lb6.place(x=860, y=50)
    lb7 = ttk.Label(root, text=st1[6], width=15, font=('Time New Roman', 14), background='cyan' )
    lb7.place(x=1030, y=50)
    lb8 = ttk.Label(root, text=st1[7], width=15, font=('Time New Roman', 14), background='cyan' )
    lb8.place(x=1200, y=50)

    v11 = StringVar()
    v11.set(nig['et11'])
    et11=Entry(root, width=27, background='yellow',textvariable=v11)
    et11.place(x=10,y=100)
    y1 = ttk.Label(root, text='001', width=4, font=('Time New Roman', 12), background='cyan' )
    y1.place(x=10, y=119)
    v12 = StringVar()
    v12.set(nig['et12'])
    et12=Entry(root, width=27, background='red',textvariable=v12)
    et12.place(x=180,y=100)
    v13 = StringVar()
    v13.set(nig['et13'])
    et13=Entry(root, width=27, background='yellow',textvariable=v13)
    et13.place(x=350,y=100)
    y14 = ttk.Label(root, text='014', width=4, font=('Time New Roman', 12), background='cyan' )
    y14.place(x=350, y=119)
    v14 = StringVar()
    v14.set(nig['et14'])
    et14=Entry(root, width=27, background='red',textvariable=v14)
    et14.place(x=520,y=100)
    v15 = StringVar()
    v15.set(nig['et15'])
    et15=Entry(root, width=27, background='yellow',textvariable=v15)
    et15.place(x=690,y=100)
    y27 = ttk.Label(root, text='027', width=4, font=('Time New Roman', 12), background='cyan' )
    y27.place(x=690, y=119)
    v16 = StringVar()
    v16.set(nig['et16'])
    et16=Entry(root, width=27, background='red',textvariable=v16)
    et16.place(x=860,y=100)
    v17 = StringVar()
    v17.set(nig['et17'])
    et17=Entry(root, width=27, background='yellow',textvariable=v17)
    et17.place(x=1030,y=100)
    y40 = ttk.Label(root, text='040', width=4, font=('Time New Roman', 12), background='cyan' )
    y40.place(x=1030, y=119)
    v18 = StringVar()
    v18.set(nig['et18'])
    et18=Entry(root, width=27, background='red',textvariable=v18)
    et18.place(x=1200,y=100)

    v21 = StringVar()
    v21.set(nig['et21'])
    et21=Entry(root, width=27, background='yellow',textvariable=v21)
    et21.place(x=10,y=150)
    y2 = ttk.Label(root, text='002', width=4, font=('Time New Roman', 12), background='cyan' )
    y2.place(x=10, y=169)
    v22 = StringVar()
    v22.set(nig['et22'])
    et22=Entry(root, width=27, background='red',textvariable=v22)
    et22.place(x=180,y=150)
    v23 = StringVar()
    v23.set(nig['et23'])
    et23=Entry(root, width=27, background='yellow',textvariable=v23)
    et23.place(x=350,y=150)
    y15 = ttk.Label(root, text='015', width=4, font=('Time New Roman', 12), background='cyan' )
    y15.place(x=350, y=169)
    v24 = StringVar()
    v24.set(nig['et24'])
    et24=Entry(root, width=27, background='red',textvariable=v24)
    et24.place(x=520,y=150)
    v25 = StringVar()
    v25.set(nig['et25'])
    et25=Entry(root, width=27, background='yellow',textvariable=v25)
    et25.place(x=690,y=150)
    y28 = ttk.Label(root, text='028', width=4, font=('Time New Roman', 12), background='cyan' )
    y28.place(x=690, y=169)
    v26 = StringVar()
    v26.set(nig['et26'])
    et26=Entry(root, width=27, background='red',textvariable=v26)
    et26.place(x=860,y=150)
    v27 = StringVar()
    v27.set(nig['et27'])
    et27=Entry(root, width=27, background='yellow',textvariable=v27)
    et27.place(x=1030,y=150)
    y41 = ttk.Label(root, text='041', width=4, font=('Time New Roman', 12), background='cyan' )
    y41.place(x=1030, y=169)
    v28 = StringVar()
    v28.set(nig['et28'])
    et28=Entry(root, width=27, background='red',textvariable=v28)
    et28.place(x=1200,y=150)

    v31 = StringVar()
    v31.set(nig['et31'])
    et31=Entry(root, width=27, background='yellow',textvariable=v31)
    et31.place(x=10,y=200)
    y3 = ttk.Label(root, text='003', width=4, font=('Time New Roman', 12), background='cyan' )
    y3.place(x=10, y=219)
    v32 = StringVar()
    v32.set(nig['et32'])
    et32=Entry(root, width=27, background='red',textvariable=v32)
    et32.place(x=180,y=200)
    v33 = StringVar()
    v33.set(nig['et33'])
    et33=Entry(root, width=27, background='yellow',textvariable=v33)
    et33.place(x=350,y=200)
    y16 = ttk.Label(root, text='016', width=4, font=('Time New Roman', 12), background='cyan' )
    y16.place(x=350, y=219)
    v34 = StringVar()
    v34.set(nig['et34'])
    et34=Entry(root, width=27, background='red',textvariable=v34)
    et34.place(x=520,y=200)
    v35 = StringVar()
    v35.set(nig['et35'])
    et35=Entry(root, width=27, background='yellow',textvariable=v35)
    et35.place(x=690,y=200)
    y29 = ttk.Label(root, text='029', width=4, font=('Time New Roman', 12), background='cyan' )
    y29.place(x=690, y=219)
    v36 = StringVar()
    v36.set(nig['et36'])
    et36=Entry(root, width=27, background='red',textvariable=v36)
    et36.place(x=860,y=200)
    v37 = StringVar()
    v37.set(nig['et37'])
    et37=Entry(root, width=27, background='yellow',textvariable=v37)
    et37.place(x=1030,y=200)
    y42 = ttk.Label(root, text='042', width=4, font=('Time New Roman', 12), background='cyan' )
    y42.place(x=1030, y=219)
    v38 = StringVar()
    v38.set(nig['et38'])
    et38=Entry(root, width=27, background='red',textvariable=v38)
    et38.place(x=1200,y=200)

    v41 = StringVar()
    v41.set(nig['et41'])
    et41=Entry(root, width=27, background='yellow',textvariable=v41)
    et41.place(x=10,y=250)
    y4 = ttk.Label(root, text='004', width=4, font=('Time New Roman', 12), background='cyan' )
    y4.place(x=10, y=269)
    v42 = StringVar()
    v42.set(nig['et42'])
    et42=Entry(root, width=27, background='red',textvariable=v42)
    et42.place(x=180,y=250)
    v43 = StringVar()
    v43.set(nig['et43'])
    et43=Entry(root, width=27, background='yellow',textvariable=v43)
    et43.place(x=350,y=250)
    y17 = ttk.Label(root, text='017', width=4, font=('Time New Roman', 12), background='cyan' )
    y17.place(x=350, y=269)
    v44 = StringVar()
    v44.set(nig['et44'])
    et44=Entry(root, width=27, background='red',textvariable=v44)
    et44.place(x=520,y=250)
    v45 = StringVar()
    v45.set(nig['et45'])
    et45=Entry(root, width=27, background='yellow',textvariable=v45)
    et45.place(x=690,y=250)
    y30 = ttk.Label(root, text='030', width=4, font=('Time New Roman', 12), background='cyan' )
    y30.place(x=690, y=269)
    v46 = StringVar()
    v46.set(nig['et46'])
    et46=Entry(root, width=27, background='red',textvariable=v46)
    et46.place(x=860,y=250)
    v47 = StringVar()
    v47.set(nig['et47'])
    et47=Entry(root, width=27, background='yellow',textvariable=v47)
    et47.place(x=1030,y=250)
    y43 = ttk.Label(root, text='043', width=4, font=('Time New Roman', 12), background='cyan' )
    y43.place(x=1030, y=269)
    v48 = StringVar()
    v48.set(nig['et48'])
    et48=Entry(root, width=27, background='red',textvariable=v48)
    et48.place(x=1200,y=250)

    v51 = StringVar()
    v51.set(nig['et51'])
    et51=Entry(root, width=27, background='yellow',textvariable=v51)
    et51.place(x=10,y=300)
    y5 = ttk.Label(root, text='005', width=4, font=('Time New Roman', 12), background='cyan' )
    y5.place(x=10, y=319)
    v52 = StringVar()
    v52.set(nig['et52'])
    et52=Entry(root, width=27, background='red',textvariable=v52)
    et52.place(x=180,y=300)
    v53 = StringVar()
    v53.set(nig['et53'])
    et53=Entry(root, width=27, background='yellow',textvariable=v53)
    et53.place(x=350,y=300)
    y18 = ttk.Label(root, text='018', width=4, font=('Time New Roman', 12), background='cyan' )
    y18.place(x=350, y=319)
    v54 = StringVar()
    v54.set(nig['et54'])
    et54=Entry(root, width=27, background='red',textvariable=v54)
    et54.place(x=520,y=300)
    v55 = StringVar()
    v55.set(nig['et55'])
    et55=Entry(root, width=27, background='yellow',textvariable=v55)
    et55.place(x=690,y=300)
    y31 = ttk.Label(root, text='031', width=4, font=('Time New Roman', 12), background='cyan' )
    y31.place(x=690, y=319)
    v56 = StringVar()
    v56.set(nig['et56'])
    et56=Entry(root, width=27, background='red',textvariable=v56)
    et56.place(x=860,y=300)
    v57 = StringVar()
    v57.set(nig['et57'])
    et57=Entry(root, width=27, background='yellow',textvariable=v57)
    et57.place(x=1030,y=300)
    y44 = ttk.Label(root, text='044', width=4, font=('Time New Roman', 12), background='cyan' )
    y44.place(x=1030, y=319)
    v58 = StringVar()
    v58.set(nig['et58'])
    et58=Entry(root, width=27, background='red',textvariable=v58)
    et58.place(x=1200,y=300)

    v61 = StringVar()
    v61.set(nig['et61'])
    et61=Entry(root, width=27, background='yellow',textvariable=v61)
    et61.place(x=10,y=350)
    y6 = ttk.Label(root, text='006', width=4, font=('Time New Roman', 12), background='cyan' )
    y6.place(x=10, y=369)
    v62 = StringVar()
    v62.set(nig['et62'])
    et62=Entry(root, width=27, background='red',textvariable=v62)
    et62.place(x=180,y=350)
    v63 = StringVar()
    v63.set(nig['et63'])
    et63=Entry(root, width=27, background='yellow',textvariable=v63)
    et63.place(x=350,y=350)
    y19 = ttk.Label(root, text='019', width=4, font=('Time New Roman', 12), background='cyan' )
    y19.place(x=350, y=369)
    v64 = StringVar()
    v64.set(nig['et64'])
    et64=Entry(root, width=27, background='red',textvariable=v64)
    et64.place(x=520,y=350)
    v65 = StringVar()
    v65.set(nig['et65'])
    et65=Entry(root, width=27, background='yellow',textvariable=v65)
    et65.place(x=690,y=350)
    y32 = ttk.Label(root, text='032', width=4, font=('Time New Roman', 12), background='cyan' )
    y32.place(x=690, y=369)
    v66 = StringVar()
    v66.set(nig['et66'])
    et66=Entry(root, width=27, background='red',textvariable=v66)
    et66.place(x=860,y=350)
    v67 = StringVar()
    v67.set(nig['et67'])
    et67=Entry(root, width=27, background='yellow',textvariable=v67)
    et67.place(x=1030,y=350)
    y45 = ttk.Label(root, text='045', width=4, font=('Time New Roman', 12), background='cyan' )
    y45.place(x=1030, y=369)
    v68 = StringVar()
    v68.set(nig['et68'])
    et68=Entry(root, width=27, background='red',textvariable=v68)
    et68.place(x=1200,y=350)

    v71 = StringVar()
    v71.set(nig['et71'])
    et71=Entry(root, width=27, background='yellow',textvariable=v71)
    et71.place(x=10,y=400)
    y7 = ttk.Label(root, text='007', width=4, font=('Time New Roman', 12), background='cyan' )
    y7.place(x=10, y=419)
    v72 = StringVar()
    v72.set(nig['et72'])
    et72=Entry(root, width=27, background='red',textvariable=v72)
    et72.place(x=180,y=400)
    v73 = StringVar()
    v73.set(nig['et73'])
    et73=Entry(root, width=27, background='yellow',textvariable=v73)
    et73.place(x=350,y=400)
    y19 = ttk.Label(root, text='020', width=4, font=('Time New Roman', 12), background='cyan' )
    y19.place(x=350, y=419)
    v74 = StringVar()
    v74.set(nig['et74'])
    et74=Entry(root, width=27, background='red',textvariable=v74)
    et74.place(x=520,y=400)
    v75 = StringVar()
    v75.set(nig['et75'])
    et75=Entry(root, width=27, background='yellow',textvariable=v75)
    et75.place(x=690,y=400)
    y33 = ttk.Label(root, text='033', width=4, font=('Time New Roman', 12), background='cyan' )
    y33.place(x=690, y=419)
    v76 = StringVar()
    v76.set(nig['et76'])
    et76=Entry(root, width=27, background='red',textvariable=v76)
    et76.place(x=860,y=400)
    v77 = StringVar()
    v77.set(nig['et77'])
    et77=Entry(root, width=27, background='yellow',textvariable=v77)
    et77.place(x=1030,y=400)
    y46 = ttk.Label(root, text='046', width=4, font=('Time New Roman', 12), background='cyan' )
    y46.place(x=1030, y=419)
    v78 = StringVar()
    v78.set(nig['et78'])
    et78=Entry(root, width=27, background='red',textvariable=v78)
    et78.place(x=1200,y=400)

    v81 = StringVar()
    v81.set(nig['et81'])
    et81=Entry(root, width=27, background='yellow',textvariable=v81)
    et81.place(x=10,y=450)
    y8 = ttk.Label(root, text='008', width=4, font=('Time New Roman', 12), background='cyan' )
    y8.place(x=10, y=469)
    v82 = StringVar()
    v82.set(nig['et82'])
    et82=Entry(root, width=27, background='red',textvariable=v82)
    et82.place(x=180,y=450)
    v83 = StringVar()
    v83.set(nig['et83'])
    et83=Entry(root, width=27, background='yellow',textvariable=v83)
    et83.place(x=350,y=450)
    y21 = ttk.Label(root, text='021', width=4, font=('Time New Roman', 12), background='cyan' )
    y21.place(x=350, y=469)
    v84 = StringVar()
    v84.set(nig['et84'])
    et84=Entry(root, width=27, background='red',textvariable=v84)
    et84.place(x=520,y=450)
    v85 = StringVar()
    v85.set(nig['et85'])
    et85=Entry(root, width=27, background='yellow',textvariable=v85)
    et85.place(x=690,y=450)
    y34 = ttk.Label(root, text='034', width=4, font=('Time New Roman', 12), background='cyan' )
    y34.place(x=690, y=469)
    v86 = StringVar()
    v86.set(nig['et86'])
    et86=Entry(root, width=27, background='red',textvariable=v86)
    et86.place(x=860,y=450)
    v87 = StringVar()
    v87.set(nig['et87'])
    et87=Entry(root, width=27, background='yellow',textvariable=v87)
    et87.place(x=1030,y=450)
    y47 = ttk.Label(root, text='047', width=4, font=('Time New Roman', 12), background='cyan' )
    y47.place(x=1030, y=469)
    v88 = StringVar()
    v88.set(nig['et88'])
    et88=Entry(root, width=27, background='red',textvariable=v88)
    et88.place(x=1200,y=450)

    v91 = StringVar()
    v91.set(nig['et91'])
    et91=Entry(root, width=27, background='yellow',textvariable=v91)
    et91.place(x=10,y=500)
    y9 = ttk.Label(root, text='009', width=4, font=('Time New Roman', 12), background='cyan' )
    y9.place(x=10, y=519)
    v92 = StringVar()
    v92.set(nig['et92'])
    et92=Entry(root, width=27, background='red',textvariable=v92)
    et92.place(x=180,y=500)
    v93 = StringVar()
    v93.set(nig['et93'])
    et93=Entry(root, width=27, background='yellow',textvariable=v93)
    et93.place(x=350,y=500)
    y22 = ttk.Label(root, text='022', width=4, font=('Time New Roman', 12), background='cyan' )
    y22.place(x=350, y=519)
    v94 = StringVar()
    v94.set(nig['et94'])
    et94=Entry(root, width=27, background='red',textvariable=v94)
    et94.place(x=520,y=500)
    v95 = StringVar()
    v95.set(nig['et95'])
    et95=Entry(root, width=27, background='yellow',textvariable=v95)
    et95.place(x=690,y=500)
    y35 = ttk.Label(root, text='035', width=4, font=('Time New Roman', 12), background='cyan' )
    y35.place(x=690, y=519)
    v96 = StringVar()
    v96.set(nig['et96'])
    et96=Entry(root, width=27, background='red',textvariable=v96)
    et96.place(x=860,y=500)
    v97 = StringVar()
    v97.set(nig['et97'])
    et97=Entry(root, width=27, background='yellow',textvariable=v97)
    et97.place(x=1030,y=500)
    y48 = ttk.Label(root, text='048', width=4, font=('Time New Roman', 12), background='cyan' )
    y48.place(x=1030, y=519)
    v98 = StringVar()
    v98.set(nig['et98'])
    et98=Entry(root, width=27, background='red',textvariable=v98)
    et98.place(x=1200,y=500)

    v101 = StringVar()
    v101.set(nig['et101'])
    et101=Entry(root, width=27, background='yellow',textvariable=v101)
    et101.place(x=10,y=550)
    y10 = ttk.Label(root, text='010', width=4, font=('Time New Roman', 12), background='cyan' )
    y10.place(x=10, y=569)
    v102 = StringVar()
    v102.set(nig['et102'])
    et102=Entry(root, width=27, background='red',textvariable=v102)
    et102.place(x=180,y=550)
    v103 = StringVar()
    v103.set(nig['et103'])
    et103=Entry(root, width=27, background='yellow',textvariable=v103)
    et103.place(x=350,y=550)
    y23 = ttk.Label(root, text='023', width=4, font=('Time New Roman', 12), background='cyan' )
    y23.place(x=350, y=569)
    v104 = StringVar()
    v104.set(nig['et104'])
    et104=Entry(root, width=27, background='red',textvariable=v104)
    et104.place(x=520,y=550)
    v105 = StringVar()
    v105.set(nig['et105'])
    et105=Entry(root, width=27, background='yellow',textvariable=v105)
    et105.place(x=690,y=550)
    y36 = ttk.Label(root, text='036', width=4, font=('Time New Roman', 12), background='cyan' )
    y36.place(x=690, y=569)
    v106 = StringVar()
    v106.set(nig['et106'])
    et106=Entry(root, width=27, background='red',textvariable=v106)
    et106.place(x=860,y=550)
    v107 = StringVar()
    v107.set(nig['et107'])
    et107=Entry(root, width=27, background='yellow',textvariable=v107)
    et107.place(x=1030,y=550)
    y49 = ttk.Label(root, text='049', width=4, font=('Time New Roman', 12), background='cyan' )
    y49.place(x=1030, y=569)
    v108 = StringVar()
    v108.set(nig['et108'])
    et108=Entry(root, width=27, background='red',textvariable=v108)
    et108.place(x=1200,y=550)

    v111 = StringVar()
    v111.set(nig['et111'])
    et111=Entry(root, width=27, background='yellow',textvariable=v111)
    et111.place(x=10,y=600)
    y11 = ttk.Label(root, text='011', width=4, font=('Time New Roman', 12), background='cyan' )
    y11.place(x=10, y=619)
    v112 = StringVar()
    v112.set(nig['et112'])
    et112=Entry(root, width=27, background='red',textvariable=v112)
    et112.place(x=180,y=600)
    v113 = StringVar()
    v113.set(nig['et113'])
    et113=Entry(root, width=27, background='yellow',textvariable=v113)
    et113.place(x=350,y=600)
    y24 = ttk.Label(root, text='024', width=4, font=('Time New Roman', 12), background='cyan' )
    y24.place(x=350, y=619)
    v114 = StringVar()
    v114.set(nig['et114'])
    et114=Entry(root, width=27, background='red',textvariable=v114)
    et114.place(x=520,y=600)
    v115 = StringVar()
    v115.set(nig['et115'])
    et115=Entry(root, width=27, background='yellow',textvariable=v115)
    et115.place(x=690,y=600)
    y37 = ttk.Label(root, text='037', width=4, font=('Time New Roman', 12), background='cyan' )
    y37.place(x=690, y=619)
    v116 = StringVar()
    v116.set(nig['et116'])
    et116=Entry(root, width=27, background='red',textvariable=v116)
    et116.place(x=860,y=600)
    v117 = StringVar()
    v117.set(nig['et117'])
    et117=Entry(root, width=27, background='yellow',textvariable=v117)
    et117.place(x=1030,y=600)
    y50 = ttk.Label(root, text='050', width=4, font=('Time New Roman', 12), background='cyan' )
    y50.place(x=1030, y=619)
    v118 = StringVar()
    v118.set(nig['et118'])
    et118=Entry(root, width=27, background='red',textvariable=v118)
    et118.place(x=1200,y=600)

    v121 = StringVar()
    v121.set(nig['et121'])
    et121=Entry(root, width=27, background='yellow',textvariable=v121)
    et121.place(x=10,y=650)
    y12 = ttk.Label(root, text='012', width=4, font=('Time New Roman', 12), background='cyan' )
    y12.place(x=10, y=669)
    v122 = StringVar()
    v122.set(nig['et122'])
    et122=Entry(root, width=27, background='red',textvariable=v122)
    et122.place(x=180,y=650)
    v123 = StringVar()
    v123.set(nig['et123'])
    et123=Entry(root, width=27, background='yellow',textvariable=v123)
    et123.place(x=350,y=650)
    y25 = ttk.Label(root, text='025', width=4, font=('Time New Roman', 12), background='cyan' )
    y25.place(x=350, y=669)
    v124 = StringVar()
    v124.set(nig['et124'])
    et124=Entry(root, width=27, background='red',textvariable=v124)
    et124.place(x=520,y=650)
    v125 = StringVar()
    v125.set(nig['et125'])
    et125=Entry(root, width=27, background='yellow',textvariable=v125)
    et125.place(x=690,y=650)
    y38 = ttk.Label(root, text='038', width=4, font=('Time New Roman', 12), background='cyan' )
    y38.place(x=690, y=669)
    v126 = StringVar()
    v126.set(nig['et126'])
    et126=Entry(root, width=27, background='red',textvariable=v126)
    et126.place(x=860,y=650)
    v127 = StringVar()
    v127.set(nig['et127'])
    et127=Entry(root, width=27, background='yellow',textvariable=v127)
    et127.place(x=1030,y=650)
    y51 = ttk.Label(root, text='051', width=4, font=('Time New Roman', 12), background='cyan' )
    y51.place(x=1030, y=669)
    v128 = StringVar()
    v128.set(nig['et128'])
    et128=Entry(root, width=27, background='red',textvariable=v128)
    et128.place(x=1200,y=650)

    v131 = StringVar()
    v131.set(nig['et131'])
    et131=Entry(root, width=27, background='yellow',textvariable=v131)
    et131.place(x=10,y=700)
    y13 = ttk.Label(root, text='013', width=4, font=('Time New Roman', 12), background='cyan' )
    y13.place(x=10, y=719)
    v132 = StringVar()
    v132.set(nig['et132'])
    et132=Entry(root, width=27, background='red',textvariable=v132)
    et132.place(x=180,y=700)
    v133 = StringVar()
    v133.set(nig['et133'])
    et133=Entry(root, width=27, background='yellow',textvariable=v133)
    et133.place(x=350,y=700)
    y26 = ttk.Label(root, text='026', width=4, font=('Time New Roman', 12), background='cyan' )
    y26.place(x=350, y=719)
    v134 = StringVar()
    v134.set(nig['et134'])
    et134=Entry(root, width=27, background='red',textvariable=v134)
    et134.place(x=520,y=700)
    v135 = StringVar()
    v135.set(nig['et135'])
    et135=Entry(root, width=27, background='yellow',textvariable=v135)
    et135.place(x=690,y=700)
    y39 = ttk.Label(root, text='039', width=4, font=('Time New Roman', 12), background='cyan' )
    y39.place(x=690, y=719)
    v136 = StringVar()
    v136.set(nig['et136'])
    et136=Entry(root, width=27, background='red',textvariable=v136)
    et136.place(x=860,y=700)
    v137 = StringVar()
    v137.set(nig['et137'])
    et137=Entry(root, width=27, background='yellow',textvariable=v137)
    et137.place(x=1030,y=700)
    y52 = ttk.Label(root, text='052', width=4, font=('Time New Roman', 12), background='cyan' )
    y52.place(x=1030, y=719)
    v138 = StringVar()
    v138.set(nig['et138'])
    et138=Entry(root, width=27, background='red',textvariable=v138)
    et138.place(x=1200,y=700)

    def schet():
        window=Tk()
        window.title('Счет')
        window.geometry('500x300')

        languages = ['001', '002', '003', '004','005','006','007','008','009','010','011','012','013','014','015','016',
                     '017','018','019','020','021','022','023','024','025','026','027','028','029','030','031','032',
                     '033','034','035','036','037','038','039','040','041','042','043','044','045','046','047','048',
                     '049','050','051','052']
        combobox = ttk.Combobox(window,values=languages)
        combobox.place(x=20,y=40)

        label=Label(window,text='Количества')
        label.place(x=250,y=20)
        v=IntVar()
        v.set(0)
        e = Entry(window, width=10, background='white', textvariable=v)
        e.place(x=250, y=40)

        s=[]
        def yesho():
            g1=combobox.get()
            g2=e.get()
            if g1=='001':
                p=(st1[9][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='014':
                p=(st1[11][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='027':
                p=(st1[13][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='040':
                p=(st1[15][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='002':
                p=(st1[17][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='015':
                p=(st1[19][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='028':
                p = (st1[21][0:-1]).replace(' ', '')
                f = int(p) * int(g2)
                s.append(f)
            elif g1=='041':
                p=(st1[23][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='003':
                p=(st1[25][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='016':
                p=(st1[27][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='029':
                p=(st1[29][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='042':
                p=(st1[31][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='004':
                p=(st1[33][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='017':
                p=(st1[35][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='030':
                p=(st1[37][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='043':
                p=(st1[39][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='005':
                p=(st1[41][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='018':
                p=(st1[43][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='031':
                p=(st1[45][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='044':
                p=(st1[47][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='006':
                p=(st1[49][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='019':
                p=(st1[51][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='032':
                p=(st1[53][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='045':
                p=(st1[55][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='007':
                p=(st1[57][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='020':
                p=(st1[59][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='033':
                p=(st1[61][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='046':
                p=(st1[63][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='008':
                p=(st1[65][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='021':
                p=(st1[67][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='034':
                p=(st1[69][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='047':
                p=(st1[71][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='009':
                p=(st1[73][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='022':
                p=(st1[75][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='035':
                p=(st1[77][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='048':
                p=(st1[79][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='010':
                p=(st1[81][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='023':
                p=(st1[83][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='036':
                p=(st1[85][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='049':
                p=(st1[87][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='011':
                p=(st1[89][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='024':
                p=(st1[91][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='037':
                p=(st1[93][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='050':
                p=(st1[95][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='012':
                p=(st1[97][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='025':
                p=(st1[99][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='038':
                p=(st1[101][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='051':
                p=(st1[103][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='013':
                p=(st1[105][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='026':
                p=(st1[107][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='039':
                p=(st1[109][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='052':
                p=(st1[111][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)


        esho = Button(window, text='Ещё', command=yesho, bg="yellow", font=("Times New Roman", 13, 'bold'), width=10,
                     height=1)
        esho.place(x=250, y=150)

        def ok():
            g1=combobox.get()
            g2=e.get()
            if g1=='001':
                p=(st1[9][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='014':
                p=(st1[11][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='027':
                p=(st1[13][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='040':
                p=(st1[15][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='002':
                p=(st1[17][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='015':
                p=(st1[19][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='028':
                p = (st1[21][0:-1]).replace(' ', '')
                f = int(p) * int(g2)
                s.append(f)
            elif g1=='041':
                p=(st1[23][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='003':
                p=(st1[25][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='016':
                p=(st1[27][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='029':
                p=(st1[29][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='042':
                p=(st1[31][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='004':
                p=(st1[33][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='017':
                p=(st1[35][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='030':
                p=(st1[37][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='043':
                p=(st1[39][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='005':
                p=(st1[41][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='018':
                p=(st1[43][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='031':
                p=(st1[45][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='044':
                p=(st1[47][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='006':
                p=(st1[49][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='019':
                p=(st1[51][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='032':
                p=(st1[53][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='045':
                p=(st1[55][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='007':
                p=(st1[57][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='020':
                p=(st1[59][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='033':
                p=(st1[61][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='046':
                p=(st1[63][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='008':
                p=(st1[65][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='021':
                p=(st1[67][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='034':
                p=(st1[69][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='047':
                p=(st1[71][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='009':
                p=(st1[73][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='022':
                p=(st1[75][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='035':
                p=(st1[77][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='048':
                p=(st1[79][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='010':
                p=(st1[81][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='023':
                p=(st1[83][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='036':
                p=(st1[85][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='049':
                p=(st1[87][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='011':
                p=(st1[89][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='024':
                p=(st1[91][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='037':
                p=(st1[93][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='050':
                p=(st1[95][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='012':
                p=(st1[97][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='025':
                p=(st1[99][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='038':
                p=(st1[101][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='051':
                p=(st1[103][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='013':
                p=(st1[105][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='026':
                p=(st1[107][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='039':
                p=(st1[109][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            elif g1=='052':
                p=(st1[111][0:-1]).replace(' ','')
                f=int(p)*int(g2)
                s.append(f)
            t=str(sum(s))
            t1=t[0:-3]+' '+t[-3:]
            label1=Label(window,text='Вы заплатите '+t1+' сум',font=("Times New Roman", 20, 'bold'))
            label1.place(x=20,y=250)

        okey = Button(window, text='Сумма', command=ok, bg="cyan", font=("Times New Roman", 13, 'bold'), width=10,
                     height=1)
        okey.place(x=20, y=150)



    bt2 = Button(root, text='Счет', command=schet, bg="yellow", font=("Times New Roman", 13, 'bold'), width=10,height=1)
    bt2.place(x=500, y=8)


    def viyti1():
        # root.destroy()
        root.destroy()
        #root1.destroy()
    bt1 = Button(root, text='Выйти', command=viyti1, bg="red", font=("Times New Roman", 13, 'bold'), width=10,height=1)
    bt1.place(x=1150, y=8)


    def dobavit():
        a11=et11.get()
        if a11 != nig['et11']:
            if a11=='':
                print(1)
                a11+='1'
                st1.pop(8)
                st1.insert(8,str(a11)+'\n')
            else:
                print(0)
                st1.pop(8)
                st1.insert(8,str(a11)+'\n')
        a12=et12.get()
        if a12 != nig['et12']:
            if a12=='':
                print(1)
                a12+='2'
                st1.pop(9)
                st1.insert(9,str(a12)+'\n')
            else:
                print(0)
                st1.pop(9)
                st1.insert(9, str(a12) + '\n')
        a13=et13.get()
        if a13 != nig['et13']:
            if a13=='':
                print(1)
                a13+='3'
                st1.pop(10)
                st1.insert(10,str(a13)+'\n')
            else:
                print(0)
                st1.pop(10)
                st1.insert(10,str(a13)+'\n')
        a14=et14.get()
        if a14 != nig['et14']:
            if a14=='':
                print(1)
                a14+='4'
                st1.pop(11)
                st1.insert(11,str(a14)+'\n')
            else:
                print(0)
                st1.pop(11)
                st1.insert(11, str(a14) + '\n')
        a15=et15.get()
        if a15 != nig['et15']:
            if a15=='':
                print(1)
                a15+='5'
                st1.pop(12)
                st1.insert(12,str(a15)+'\n')
            else:
                print(0)
                st1.pop(12)
                st1.insert(12, str(a15) + '\n')
        a16=et16.get()
        if a16 != nig['et16']:
            if a16=='':
                print(1)
                a16+='6'
                st1.pop(13)
                st1.insert(13,str(a16)+'\n')
            else:
                print(0)
                st1.pop(13)
                st1.insert(13, str(a16) + '\n')
        a17=et17.get()
        if a17 != nig['et17']:
            if a17=='':
                print(1)
                a17+='7'
                st1.pop(14)
                st1.insert(14,str(a17)+'\n')
            else:
                print(0)
                st1.pop(14)
                st1.insert(14, str(a17) + '\n')
        a18=et18.get()
        if a18 != nig['et18']:
            if a18=='':
                print(1)
                a18+='8'
                st1.pop(15)
                st1.insert(15,str(a18)+'\n')
            else:
                print(0)
                st1.pop(15)
                st1.insert(15,str(a18)+'\n')

        a21=et21.get()
        if a21 != nig['et21']:
            if a21=='':
                print(1)
                a21+='9'
                st1.pop(16)
                st1.insert(16,str(a21)+'\n')
            else:
                print(0)
                st1.pop(16)
                st1.insert(16, str(a21) + '\n')
        a22=et22.get()
        if a22 != nig['et22']:
            if a22=='':
                print(1)
                a22+='10'
                st1.pop(17)
                st1.insert(17,str(a22)+'\n')
            else:
                print(0)
                st1.pop(17)
                st1.insert(17, str(a22) + '\n')
        a23=et23.get()
        if a23 != nig['et23']:
            if a23=='':
                print(1)
                a23+='11'
                st1.pop(18)
                st1.insert(18,str(a23)+'\n')
            else:
                print(0)
                st1.pop(18)
                st1.insert(18, str(a23) + '\n')
        a24=et24.get()
        if a24 != nig['et24']:
            if a24=='':
                print(1)
                a24+='12'
                st1.pop(19)
                st1.insert(19,str(a24)+'\n')
            else:
                print(0)
                st1.pop(19)
                st1.insert(19, str(a24) + '\n')
        a25=et25.get()
        if a25 != nig['et25']:
            if a25=='':
                print(1)
                a25+='13'
                st1.pop(20)
                st1.insert(20,str(a25)+'\n')
            else:
                print(0)
                st1.pop(20)
                st1.insert(20, str(a25) + '\n')
        a26=et26.get()
        if a26 != nig['et26']:
            if a26=='':
                print(1)
                a26+='14'
                st1.pop(21)
                st1.insert(21,str(a26)+'\n')
            else:
                print(0)
                st1.pop(21)
                st1.insert(21, str(a26) + '\n')
        a27=et27.get()
        if a27 != nig['et27']:
            if a27=='':
                print(1)
                a27+='15'
                st1.pop(22)
                st1.insert(22,str(a27)+'\n')
            else:
                print(0)
                st1.pop(22)
                st1.insert(22, str(a27) + '\n')
        a28=et28.get()
        if a28 != nig['et28']:
            if a28=='':
                print(1)
                a28+='16'
                st1.pop(23)
                st1.insert(23,str(a28)+'\n')
            else:
                print(0)
                st1.pop(23)
                st1.insert(23, str(a28) + '\n')

        a31=et31.get()
        if a31 != nig['et31']:
            if a31=='':
                print(1)
                a31+='17'
                st1.pop(24)
                st1.insert(24,str(a31)+'\n')
            else:
                print(0)
                st1.pop(24)
                st1.insert(24, str(a31) + '\n')
        a32=et32.get()
        if a32 != nig['et32']:
            if a32=='':
                print(1)
                a32+='18'
                st1.pop(25)
                st1.insert(25,str(a32)+'\n')
            else:
                print(0)
                st1.pop(25)
                st1.insert(25, str(a32) + '\n')
        a33=et33.get()
        if a33 != nig['et33']:
            if a33=='':
                print(1)
                a33+='19'
                st1.pop(26)
                st1.insert(26,str(a33)+'\n')
            else:
                print(0)
                st1.pop(26)
                st1.insert(26,str(a33)+'\n')
        a34=et34.get()
        if a34 != nig['et34']:
            if a34=='':
                print(1)
                a34+='20'
                st1.pop(27)
                st1.insert(27,str(a34)+'\n')
            else:
                print(34)
                st1.pop(27)
                st1.insert(27, str(a34) + '\n')
        a35=et35.get()
        if a35 != nig['et35']:
            if a35=='':
                a35+='21'
                st1.pop(28)
                st1.insert(28,str(a35)+'\n')
            else:
                print(35)
                st1.pop(28)
                st1.insert(28, str(a35) + '\n')
        a36=et36.get()
        if a36 != nig['et36']:
            if a36=='':
                a36+='22'
                st1.pop(29)
                st1.insert(29,str(a36)+'\n')
            else:
                print(36)
                st1.pop(29)
                st1.insert(29, str(a36) + '\n')
        a37=et37.get()
        if a37 != nig['et37']:
            if a37=='':
                a37+='23'
                st1.pop(30)
                st1.insert(30,str(a37)+'\n')
            else:
                print(37)
                st1.pop(30)
                st1.insert(30, str(a37) + '\n')
        a38=et38.get()
        if a38 != nig['et38']:
            if a38=='':
                a38+='24'
                st1.pop(31)
                st1.insert(31,str(a38)+'\n')
            else:
                print(38)
                st1.pop(31)
                st1.insert(31, str(a38) + '\n')

        a41=et41.get()
        if a41 != nig['et41']:
            if a41=='':
                a41+='25'
                st1.pop(32)
                st1.insert(32,str(a41)+'\n')
            else:
                print(41)
                st1.pop(32)
                st1.insert(32, str(a41) + '\n')
        a42=et42.get()
        if a42 != nig['et42']:
            if a42=='':
                a42+='26'
                st1.pop(33)
                st1.insert(33,str(a42)+'\n')
            else:
                print(42)
                st1.pop(33)
                st1.insert(33, str(a42) + '\n')
        a43=et43.get()
        if a43 != nig['et43']:
            if a43=='':
                a43+='27'
                st1.pop(34)
                st1.insert(34,str(a43)+'\n')
            else:
                print(43)
                st1.pop(34)
                st1.insert(34, str(a43) + '\n')
        a44=et44.get()
        if a44 != nig['et44']:
            if a44=='':
                a44+='28'
                st1.pop(35)
                st1.insert(35,str(a44)+'\n')
            else:
                print(44)
                st1.pop(35)
                st1.insert(35, str(a44) + '\n')
        a45=et45.get()
        if a45 != nig['et45']:
            if a45=='':
                a45+='29'
                st1.pop(36)
                st1.insert(36,str(a45)+'\n')
            else:
                print(45)
                st1.pop(36)
                st1.insert(36, str(a45) + '\n')
        a46=et46.get()
        if a46 != nig['et46']:
            if a46=='':
                a46+='30'
                st1.pop(37)
                st1.insert(37,str(a46)+'\n')
            else:
                pritn(46)
                st1.pop(37)
                st1.insert(37, str(a46) + '\n')
        a47=et47.get()
        if a47 != nig['et47']:
            if a47=='':
                a47+='31'
                st1.pop(38)
                st1.insert(38,str(a47)+'\n')
            else:
                print(47)
                st1.pop(38)
                st1.insert(38,str(a47)+'\n')

        a48=et48.get()
        if a48 != nig['et48']:
            if a48=='':
                a48+='32'
                st1.pop(39)
                st1.insert(39,str(a48)+'\n')
            else:
                print(48)
                st1.pop(39)
                st1.insert(39, str(a48) + '\n')

        a51=et51.get()
        if a51 != nig['et51']:
            if a51=='':
                a51+='33'
                st1.pop(40)
                st1.insert(40,str(a51)+'\n')
            else:
                print(51)
                st1.pop(40)
                st1.insert(40, str(a51) + '\n')
        a52=et52.get()
        if a52 != nig['et52']:
            if a52=='':
                a52+='34'
                st1.pop(41)
                st1.insert(41,str(a52)+'\n')
            else:
                print(52)
                st1.pop(41)
                st1.insert(41, str(a52) + '\n')
        a53=et53.get()
        if a53 != nig['et53']:
            if a53=='':
                a53+='35'
                st1.pop(42)
                st1.insert(42,str(a53)+'\n')
            else:
                print(53)
                st1.pop(42)
                st1.insert(42, str(a53) + '\n')
        a54=et54.get()
        if a54 != nig['et54']:
            if a54=='':
                a54+='36'
                st1.pop(43)
                st1.insert(43,str(a54)+'\n')
            else:
                print(54)
                st1.pop(43)
                st1.insert(43, str(a54) + '\n')
        a55=et55.get()
        if a55 != nig['et55']:
            if a55=='':
                a55+='37'
                st1.pop(44)
                st1.insert(44,str(a55)+'\n')
            else:
                print(55)
                st1.pop(44)
                st1.insert(44, str(a55) + '\n')
        a56=et56.get()
        if a56 != nig['et56']:
            if a56=='':
                a56+='38'
                st1.pop(45)
                st1.insert(45,str(a56)+'\n')
            else:
                st1.pop(45)
                st1.insert(45, str(a56) + '\n')
        a57=et57.get()
        if a57 != nig['et57']:
            if a57=='':
                a57+='39'
                st1.pop(46)
                st1.insert(46,str(a57)+'\n')
            else:
                print(57)
                st1.pop(46)
                st1.insert(46, str(a57) + '\n')
        a58=et58.get()
        if a58 != nig['et58']:
            if a58=='':
                a58+='40'
                st1.pop(47)
                st1.insert(47,str(a58)+'\n')
            else:
                print(58)
                st1.pop(47)
                st1.insert(47, str(a58) + '\n')

        a61=et61.get()
        if a61 != nig['et61']:
            if a61=='':
                a61+='41'
                st1.pop(48)
                st1.insert(48,str(a61)+'\n')
            else:
                print(61)
                st1.pop(48)
                st1.insert(48, str(a61) + '\n')
        a62=et62.get()
        if a62 != nig['et62']:
            if a62=='':
                a62+='42'
                st1.pop(49)
                st1.insert(49,str(a62)+'\n')
            else:
                print(62)
                st1.pop(49)
                st1.insert(49,str(a62)+'\n')
        a63=et63.get()
        if a63 != nig['et63']:
            if a63=='':
                a63+='43'
                st1.pop(50)
                st1.insert(50,str(a63)+'\n')
            else:
                print(63)
                st1.pop(50)
                st1.insert(50, str(a63) + '\n')
        a64=et64.get()
        if a64 != nig['et64']:
            if a64=='':
                a64+='44'
                st1.pop(51)
                st1.insert(51,str(a64)+'\n')
            else:
                print(64)
                st1.pop(51)
                st1.insert(51, str(a64) + '\n')
        a65=et65.get()
        if a65 != nig['et65']:
            if a65=='':
                a65+='45'
                st1.pop(52)
                st1.insert(52,str(a65)+'\n')
            else:
                print(65)
                st1.pop(52)
                st1.insert(52, str(a65) + '\n')
        a66=et66.get()
        if a66 != nig['et66']:
            if a66=='':
                a66+='46'
                st1.pop(53)
                st1.insert(53,str(a66)+'\n')
            else:
                print(66)
                st1.pop(53)
                st1.insert(53, str(a66) + '\n')
        a67=et67.get()
        if a67 != nig['et67']:
            if a67=='':
                a67+='47'
                st1.pop(54)
                st1.insert(54,str(a67)+'\n')
            else:
                print(67)
                st1.pop(54)
                st1.insert(54, str(a67) + '\n')
        a68=et68.get()
        if a68 != nig['et68']:
            if a68=='':
                a68+='48'
                st1.pop(55)
                st1.insert(55,str(a68)+'\n')
            else:
                print(68)
                st1.pop(55)
                st1.insert(55, str(a68) + '\n')

        a71=et71.get()
        if a71 != nig['et71']:
            if a71=='':
                a71+='49'
                st1.pop(56)
                st1.insert(56,str(a71)+'\n')
            else:
                print(71)
                st1.pop(56)
                st1.insert(56, str(a71) + '\n')
        a72=et72.get()
        if a72 != nig['et72']:
            if a72=='':
                a72+='50'
                st1.pop(57)
                st1.insert(57,str(a72)+'\n')
            else:
                print(72)
                st1.pop(57)
                st1.insert(57, str(a72) + '\n')
        a73=et73.get()
        if a73 != nig['et73']:
            if a73=='':
                a73+='51'
                st1.pop(58)
                st1.insert(58,str(a73)+'\n')
            else:
                print(73)
                st1.pop(58)
                st1.insert(58, str(a73) + '\n')
        a74=et74.get()
        if a74 != nig['et74']:
            if a74=='':
                a74+='52'
                st1.pop(59)
                st1.insert(59,str(a74)+'\n')
            else:
                print(74)
                st1.pop(59)
                st1.insert(59, str(a74) + '\n')
        a75=et75.get()
        if a75 != nig['et75']:
            if a75=='':
                a75+='53'
                st1.pop(60)
                st1.insert(60,str(a75)+'\n')
            else:
                print(75)
                st1.pop(60)
                st1.insert(60, str(a75) + '\n')
        a76=et76.get()
        if a76 != nig['et76']:
            if a76=='':
                a76+='54'
                st1.pop(61)
                st1.insert(61,str(a76)+'\n')
            else:
                print(76)
                st1.pop(61)
                st1.insert(61, str(a76) + '\n')
        a77=et77.get()
        if a77 != nig['et77']:
            if a77=='':
                a77+='55'
                st1.pop(62)
                st1.insert(62,str(a77)+'\n')
            else:
                print(77)
                st1.pop(62)
                st1.insert(62, str(a77) + '\n')
        a78=et78.get()
        if a78 != nig['et78']:
            if a78=='':
                a78+='56'
                st1.pop(63)
                st1.insert(63,str(a78)+'\n')
            else:
                print(78)
                st1.pop(63)
                st1.insert(63, str(a78) + '\n')

        a81=et81.get()
        if a81 != nig['et81']:
            if a81=='':
                a81+='57'
                st1.pop(64)
                st1.insert(64,str(a81)+'\n')
            else:
                print(81)
                st1.pop(64)
                st1.insert(64, str(a81) + '\n')
        a82=et82.get()
        if a82 != nig['et82']:
            if a82=='':
                a82+='58'
                st1.pop(65)
                st1.insert(65,str(a82)+'\n')
            else:
                print(82)
                st1.pop(65)
                st1.insert(65, str(a82) + '\n')
        a83=et83.get()
        if a83 != nig['et83']:
            if a83=='':
                a83+='59'
                st1.pop(66)
                st1.insert(66,str(a83)+'\n')
            else:
                print(83)
                st1.pop(66)
                st1.insert(66, str(a83) + '\n')
        a84=et84.get()
        if a84 != nig['et84']:
            if a84=='':
                a84+='60'
                st1.pop(67)
                st1.insert(67,str(a84)+'\n')
            else:
                print(84)
                st1.pop(67)
                st1.insert(67, str(a84) + '\n')
        a85=et85.get()
        if a85 != nig['et85']:
            if a85=='':
                a85+='61'
                st1.pop(68)
                st1.insert(68,str(a85)+'\n')
            else:
                print(85)
                st1.pop(68)
                st1.insert(68, str(a85) + '\n')
        a86=et86.get()
        if a86 != nig['et86']:
            if a86=='':
                a86+='62'
                st1.pop(69)
                st1.insert(69,str(a86)+'\n')
            else:
                print(86)
                st1.pop(69)
                st1.insert(69, str(a86) + '\n')
        a87=et87.get()
        if a87 != nig['et87']:
            if a87=='':
                a87+='63'
                st1.pop(70)
                st1.insert(70,str(a87)+'\n')
            else:
                print(87)
                st1.pop(70)
                st1.insert(70, str(a87) + '\n')
        a88=et88.get()
        if a88 != nig['et88']:
            if a88=='':
                a88+='64'
                st1.pop(71)
                st1.insert(71,str(a88)+'\n')
            else:
                print(88)
                st1.pop(71)
                st1.insert(71,str(a88)+'\n')

        a91=et91.get()
        if a91 != nig['et91']:
            if a91=='':
                a91+='65'
                st1.pop(72)
                st1.insert(72,str(a91)+'\n')
            else:
                print(91)
                st1.pop(72)
                st1.insert(72, str(a91) + '\n')
        a92=et92.get()
        if a92 != nig['et92']:
            if a92=='':
                a92+='66'
                st1.pop(73)
                st1.insert(73,str(a92)+'\n')
            else:
                print(92)
                st1.pop(73)
                st1.insert(73, str(a92) + '\n')
        a93=et93.get()
        if a93 != nig['et93']:
            if a93=='':
                a93+='67'
                st1.pop(74)
                st1.insert(74,str(a93)+'\n')
            else:
                print(93,a93)
                st1.pop(74)
                st1.insert(74, str(a93) + '\n')
        a94=et94.get()
        if a94 != nig['et94']:
            if a94=='':
                a94+='68'
                st1.pop(75)
                st1.insert(75,str(a94)+'\n')
            else:
                print(94)
                st1.pop(75)
                st1.insert(75, str(a94) + '\n')
        a95=et95.get()
        if a95 != nig['et95']:
            if a95=='':
                a95+='69'
                st1.pop(76)
                st1.insert(76,str(a95)+'\n')
            else:
                print(95)
                st1.pop(76)
                st1.insert(76, str(a95) + '\n')
        a96=et96.get()
        if a96 != nig['et96']:
            if a96=='':
                a96+='70'
                st1.pop(77)
                st1.insert(77,str(a96)+'\n')
            else:
                print(96)
                st1.pop(77)
                st1.insert(77, str(a96) + '\n')
        a97=et97.get()
        if a97 != nig['et97']:
            if a97=='':
                a97+='71'
                st1.pop(78)
                st1.insert(78,str(a97)+'\n')
            else:
                print(97)
                st1.pop(78)
                st1.insert(78, str(a97) + '\n')
        a98=et98.get()
        if a98 != nig['et98']:
            if a98=='':
                a98+='72'
                st1.pop(79)
                st1.insert(79,str(a98)+'\n')
            else:
                print(98,a98)
                st1.pop(79)
                st1.insert(79,str(a98)+'\n')


        a101=et101.get()
        if a101 != nig['et101']:
            if a101=='':
                a101+='73'
                st1.pop(80)
                st1.insert(80,str(a101)+'\n')
            else:
                print(101)
                st1.pop(80)
                st1.insert(80, str(a101)+'\n')
        a102=et102.get()
        if a102 != nig['et102']:
            if a102=='':
                a102+='74'
                st1.pop(81)
                st1.insert(81,str(a102)+'\n')
            else:
                print(102)
                st1.pop(81)
                st1.insert(81, str(a102)+'\n')
        a103=et103.get()
        if a103 != nig['et103']:
            if a103=='':
                a103+='75'
                st1.pop(82)
                st1.insert(82,str(a103)+'\n')
            else:
                print(103)
                st1.pop(82)
                st1.insert(82, str(a103) + '\n')
        a104=et104.get()
        if a104 != nig['et104']:
            if a104=='':
                a104+='76'
                st1.pop(83)
                st1.insert(83,str(a104)+'\n')
            else:
                print(104)
                st1.pop(83)
                st1.insert(83, str(a104) + '\n')
        a105=et105.get()
        if a105 != nig['et105']:
            if a105=='':
                a105+='77'
                st1.pop(84)
                st1.insert(84,str(a105)+'\n')
            else:
                print(105)
                st1.pop(84)
                st1.insert(84, str(a105) + '\n')
        a106=et106.get()
        if a106 != nig['et106']:
            if a106=='':
                a106+='78'
                st1.pop(85)
                st1.insert(85,str(a106)+'\n')
            else:
                print(106)
                st1.pop(85)
                st1.insert(85, str(a106) + '\n')
        a107=et107.get()
        if a107 != nig['et107']:
            if a107=='':
                a107+='79'
                st1.pop(86)
                st1.insert(86,str(a107)+'\n')
            else:
                print(107,a107)
                st1.pop(86)
                st1.insert(86, str(a107) + '\n')
        a108=et108.get()
        if a108 != nig['et108']:
            if a108=='':
                a108+='80'
                st1.pop(87)
                st1.insert(87,str(a108)+'\n')
            else:
                print(108)
                st1.pop(87)
                st1.insert(87, str(a108) + '\n')

        a111=et111.get()
        if a111 != nig['et111']:
            if a111=='':
                a111+='81'
                st1.pop(88)
                st1.insert(88,str(a111)+'\n')
            else:
                print(111)
                st1.pop(88)
                st1.insert(88, str(a111) + '\n')
        a112=et112.get()
        if a112 != nig['et112']:
            if a112=='':
                a112+='82'
                st1.pop(89)
                st1.insert(89,str(a112)+'\n')
            else:
                print(112,a112)
                st1.pop(89)
                st1.insert(89, str(a112) + '\n')
        a113=et113.get()
        if a113 != nig['et113']:
            if a113=='':
                a113+='83'
                st1.pop(90)
                st1.insert(90,str(a113)+'\n')
            else:
                print(113)
                st1.pop(90)
                st1.insert(90, str(a113) + '\n')
        a114=et114.get()
        if a114 != nig['et114']:
            if a114=='':
                a114+='84'
                st1.pop(91)
                st1.insert(91,str(a114)+'\n')
            else:
                print(114)
                st1.pop(91)
                st1.insert(91, str(a114) + '\n')
        a115=et115.get()
        if a115 != nig['et115']:
            if a115=='':
                a115+='85'
                st1.pop(92)
                st1.insert(92,str(a115)+'\n')
            else:
                print(115)
                st1.pop(92)
                st1.insert(92, str(a115) + '\n')
        a116=et116.get()
        if a116 != nig['et116']:
            if a116=='':
                a116+='86'
                st1.pop(93)
                st1.insert(93,str(a116)+'\n')
            else:
                print(116)
                st1.pop(93)
                st1.insert(93, str(a116) + '\n')
        a117=et117.get()
        if a117 != nig['et117']:
            if a117=='':
                a117+='87'
                st1.pop(94)
                st1.insert(94,str(a117)+'\n')
            else:
                print(117)
                st1.pop(94)
                st1.insert(94, str(a117) + '\n')
        a118=et118.get()
        if a118 != nig['et118']:
            if a118=='':
                a118+='88'
                st1.pop(95)
                st1.insert(95,str(a118)+'\n')
            else:
                print(118)
                st1.pop(95)
                st1.insert(95, str(a118) + '\n')

        a121=et121.get()
        if a121 != nig['et121']:
            if a121=='':
                a121+='89'
                st1.pop(96)
                st1.insert(96,str(a121)+'\n')
            else:
                print(121)
                st1.pop(96)
                st1.insert(96, str(a121) + '\n')
        a122=et122.get()
        if a122 != nig['et122']:
            if a122=='':
                a122+='90'
                st1.pop(97)
                st1.insert(97,str(a122)+'\n')
            else:
                print(122)
                st1.pop(97)
                st1.insert(97, str(a122) + '\n')
        a123=et123.get()
        if a123 != nig['et123']:
            if a123=='':
                a123+='91'
                st1.pop(98)
                st1.insert(98,str(a123)+'\n')
            else:
                print(123)
                st1.pop(98)
                st1.insert(98, str(a123) + '\n')
        a124=et124.get()
        if a124 != nig['et124']:
            if a124=='':
                a124+='92'
                st1.pop(99)
                st1.insert(99,str(a124)+'\n')
            else:
                print(124)
                st1.pop(99)
                st1.insert(99, str(a124) + '\n')
        a125=et125.get()
        if a125 != nig['et125']:
            if a125=='':
                a125+='93'
                st1.pop(100)
                st1.insert(100,str(a125)+'\n')
            else:
                print(125)
                st1.pop(100)
                st1.insert(100, str(a125) + '\n')
        a126=et126.get()
        if a126 != nig['et126']:
            if a126=='':
                a126+='94'
                st1.pop(101)
                st1.insert(101,str(a126)+'\n')
            else:
                print(126)
                st1.pop(101)
                st1.insert(101, str(a126) + '\n')
        a127=et127.get()
        if a127 != nig['et127']:
            if a127=='':
                a127+='95'
                st1.pop(102)
                st1.insert(102,str(a127)+'\n')
            else:
                print(127,a127)
                st1.pop(102)
                st1.insert(102, str(a127) + '\n')
        a128=et128.get()
        if a128 != nig['et128']:
            if a128=='':
                a128+='96'
                st1.pop(103)
                st1.insert(103,str(a128)+'\n')
            else:
                print(128)
                st1.pop(103)
                st1.insert(103,str(a128)+'\n')


        a131=et131.get()
        if a131 != nig['et131']:
            if a131=='':
                a131+='97'
                st1.pop(104)
                st1.insert(104,str(a131)+'\n')
            else:
                print(131)
                st1.pop(104)
                st1.insert(104,str(a131)+'\n')
        a132=et132.get()
        if a132 != nig['et132']:
            if a132=='':
                a132+='98'
                st1.pop(105)
                st1.insert(105,str(a132)+'\n')
            else:
                print(132)
                st1.pop(105)
                st1.insert(105, str(a132) + '\n')
        a133=et133.get()
        if a133 != nig['et133']:
            if a133=='':
                a133+='99'
                st1.pop(106)
                st1.insert(106,str(a133)+'\n')
            else:
                print(133)
                st1.pop(106)
                st1.insert(106, str(a133) + '\n')
        a134=et134.get()
        if a134 != nig['et134']:
            if a134=='':
                a134+='100'
                st1.pop(107)
                st1.insert(107,str(a134)+'\n')
            else:
                print(134)
                st1.pop(107)
                st1.insert(107, str(a134) + '\n')
        a135=et135.get()
        if a135 != nig['et135']:
            if a135=='':
                a135+='101'
                st1.pop(108)
                st1.insert(108,str(a135)+'\n')
            else:
                print(135)
                st1.pop(108)
                st1.insert(108, str(a135) + '\n')
        a136=et136.get()
        if a136 != nig['et136']:
            if a136=='':
                a136+='102'
                st1.pop(109)
                st1.insert(109,str(a136)+'\n')
            else:
                print(136)
                st1.pop(109)
                st1.insert(109, str(a136) + '\n')
        a137=et137.get()
        if a137 != nig['et137']:
            if a137=='':
                a137+='103'
                st1.pop(110)
                st1.insert(110,str(a137)+'\n')
            else:
                print(137)
                st1.pop(110)
                st1.insert(110, str(a137) + '\n')
        a138=et138.get()
        if a138 != nig['et138']:
            if a138=='':
                a138+='104'
                st1.pop(111)
                st1.insert(111,str(a138)+'\n')
            else:
                print(138)
                st1.pop(111)
                st1.insert(111, str(a138))

        with open("menu_basa.txt", "r+") as f:
            f.seek(0)  # устанавливаем указатель в начало файла, перед имеющимися значениями
            for line in st1:
                f.write(line)
            f.truncate()  # усекаем файл до позиции, на которой стоит указатель в данный момент




    bt2 = Button(root, text='Добавить', command=dobavit, bg="red", font=("Times New Roman", 13, 'bold'), width=10,height=1)
    bt2.place(x=10, y=8)
    '''CREATE TABLE menu
    (
	Основное_блюдо NVarchar(30),
	Цена_блюдо INT,
	Салаты NVARCHAR(30),
	Цена_салатов INT,
	Десерты NVARCHAR(30),
	Цена_десертов INT,
	Напитки NVARCHAR(30),
	Цена_напитков INT
    );'''





    root.mainloop()
menu()

'''bn2 = Button(root1, text='Menu', command=menu, bg="cyan", font=("Times New Roman", 13, 'bold'), width=15, height=2)
bn2.place(x=1150,y=160)



root1.mainloop()'''
