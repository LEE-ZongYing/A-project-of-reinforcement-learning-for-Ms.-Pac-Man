Approximate 版本測試文件

程式執行:
python start.py -p ApproximateQAgent -g ApproximateGhostQAgent -a extractor=SimpleExtractor  -x 50 -n 60 -l mediumGrid

-x = 訓練50次，測試10次版本,-n= 程式總運行次數

1. start.py為啟動檔案(主要用於圖形介面的關係)
2. gametest為按下圖形介面(start、about、exit)後程式所執行的指令
3. ghostAgents則為怪物的agent
4. qlearningAgents則為小精靈的agent放置處
最主要與原Project3的程式不同之處
1. 動態參數我們是在pacman.py內部參數的地方(762行)
runGames(**args,alpha=0.6,gamma=0.4,epsilon=0.6)設定 
runGames function內做iteration次數地調整的