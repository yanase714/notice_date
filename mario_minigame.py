import random

#|■|□|□|■|
#|■|□|■|■|
#|■|■|□|■|
#|■|□|□|■|

# 編集済み



class Panel:
  def __init__(self):
    self.level = 1  #レベル1から　　　更新ごとに+1
    self.life = 3  #各レベルのライフ　更新ごとに初期化
    


  def set_num(self):
    time = random.randint(1, 11)  #ひっくり返す回数
    if time >= 5:
      self.time = 3
    elif time == 1:
      self.time = 1
    else:
      self.time = 2

    linenum = random.randint(1, 6)  #正方形のマスの数
    if linenum >= 4:
      self.linenum = 4
    elif linenum == 1:
      self.linenum = 6
    else:
      self.linenum = 5

    set_list = [[1, 4], [1, 4], [1, 4], [2, 4], [2, 4], [1, 5], [1, 5], [1, 5], [2, 5], [2, 5], [1, 6], [1, 6], [1, 6], [2, 6], [2, 6], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4]]

    if self.level < 21:
      self.time = set_list[self.level - 1][0]
      self.linenum = set_list[self.level - 1][1]

    #変更するマスを格納するリストの作成
    self.change = [[-1]*2 for _ in range(self.time)] #変更するマスを-1で初期化
    used = []

    for i in range(self.time):
      while True:
        x = random.randint(0, self.linenum - 1)
        y = random.randint(0, self.linenum - 1)

        if [x, y] not in used:
            used.append([x, y])
            self.change[i][0] = x
            self.change[i][1] = y
            break
          

    #変更するマスを格納するリストの作成完了####################



  def set_sample(self):
    self.sample = [["□"]*self.linenum for _ in range(self.linenum)]

    #見本を作成
    if self.linenum == 4:  #マスの数が4
      sample = random.randint(1, 4)

      if sample == 2:
        self.sample[1][1] = self.sample[2][2] = "■"
        for i in range(4):
          self.sample[i][0] = self.sample[i][3] = "■"

      if sample == 3:
        self.sample[1][1] = self.sample[1][2] = self.sample[2][1] = self.sample[2][2] = "■"

      if sample == 4:
        self.sample[1][1] = self.sample[1][2] = self.sample[2][1] = self.sample[2][2] = "■"
        self.sample[0][0] = self.sample[0][3] = self.sample[3][0] = self.sample[3][3] = "■"

    if self.linenum == 5:  #マスの数が5
      sample = random.randint(1, 5)

      if sample == 2:
        for i in range(5):
          self.sample[i][0] = self.sample[i][4] = "■"
          self.sample[i][i] = "■"

      if sample == 3:
        for i in range(0, 5, 2):
          self.sample[i][1] = self.sample[i][3] = "■"
          self.sample[1][i] = self.sample[3][i] = "■"

      if sample == 4:
        for i in range(1, 4, 1):
          for l in range(1, 4, 1):
            self.sample[i][l] = "■"

      if sample == 5:
        for i in range(5):
          self.sample[i][0] = self.sample[i][4] = "■"
          for l in range(0, 5, 2):
            self.sample[l][i] = "■"

    if self.linenum == 6: #マスの数が6
      sample = random.randint(1, 7)

      if sample == 2:
        for i in range(1, 5, 1):
          self.sample[i][2] = self.sample[i][3] = "■"
          self.sample[2][i] = self.sample[3][i] = "■"

      if sample == 3:
        for i in range(6):
          self.sample[i][0] = self.sample[i][5] = "■"
          self.sample[i][i] = "■"

      if sample == 4:
        for i in range(6):
          self.sample[i][2] = self.sample[i][3] = self.sample[2][i] = "■"

        self.sample[1][1] = self.sample [1][4] = "■"

      if sample == 5:
        for i in range(0, 6, 2):
          for l in range(1, 6, 2):
            self.sample[i][l] = self.sample[l][i] = "■"

      if sample == 6:
        for i in range(6):
          self.sample[2][i] = self.sample[3][i] = "■"
        for i in range(4):
          self.sample[4][i+1] = "■"
        self.sample[1][0] = self.sample[1][1] = self.sample[1][4] = self.sample[1][5] = self.sample[5][2] = self.sample[5][3] = "■"

      if sample == 7:
        for i in range(4):
          for l in range(4):
            self.sample[i+1][l+1] = "■"

    #見本の作成完了#####################################

    self.cur = [row[:] for row in self.sample]  #現在の状態を見本と同じにする


#パネル操作関数
  def panel_change(self, u, v):
    for i in range(-1, 2):  #u
      for l in range(-1, 2):  #v
        if 0 <= u+i and u+i < self.linenum and 0 <= v+l and  v+l < self.linenum :
          if self.cur[u+i][v+l] == "■":
            self.cur[u+i][v+l] = "□"
          else:
            self.cur[u+i][v+l] = "■" 



  def set_first(self):
    for i in range(self.time):
      self.panel_change(self.change[i][0], self.change[i][1])
    
    #self.first = [row[:] for row in self.cur]


#出力関数
  def sample_output(self):
    print()
    print('　 見本　　　　　 現在')
    for i in range(self.linenum):
      for l in range(self.linenum):
        print(f'|{self.sample[i][l]}', end='')
      print('|', end='      ')

       
      for l in range(self.linenum):
        print(f'|{self.cur[i][l]}', end='')
      print('|   ')
    
    print()



  def panel_check(self):
    if self.sample != self.cur:
      return 0   #見本と異なっていたら0を返す
    else:
      return 1






#初期値設定関数(パネル操作関数呼び出し)


panel = Panel()

while panel.life != 0:
  panel.set_num()         #time, linenum, changeを設定
  panel.set_sample()      #sampleを設定
  panel.set_first()       #cur(first), firstを設定
  
  while panel.life != 0:
    print("level = " f'{panel.level}' "    life = " f'{panel.life}')
    panel.sample_output()   #output

    for i in range(panel.time):
      print("残りの変えられる回数: "f'{panel.time - i}')
      print('変えるマスの位置を行列の順で入力してください(1行2列目の場合"12"と入力する)')
      change = input()
      x = int(change[0]) - 1
      y = int(change[1]) - 1

      panel.panel_change(x, y)
      panel.sample_output()

    check = panel.panel_check()
    if check == 0:
      print()
      print("--------miss...--------")
      print()
      panel.life = panel.life - 1
      panel.cur = [row[:] for row in panel.first]
    else:
      print()
      print("--------clear!!--------")
      print()
      panel.level = panel.level + 1
      panel.life = 3
      break

print("========done========")


  #panel.life = 0

