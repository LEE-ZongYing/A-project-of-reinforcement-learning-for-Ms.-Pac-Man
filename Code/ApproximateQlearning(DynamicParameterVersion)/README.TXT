小精靈vs怪獸(approximate Q-learning vs Approximate SARSA)--
python start.py -p ApproximateQAgent -g ApproximateGhostQAgent -a extractor=SimpleExtractor  -x 50 -n 60 -l mediumGrid

內部程式大致上由CS188(Berkeley AI course)的Project3修改而來
只是在專題中有添加了一些檔案(.py)
1. start.py為啟動檔案(主要用於圖形介面的關係)
2. gametest為按下圖形介面(start、about、exit)後程式所執行的指令
3. ghostAgents則為怪物的agent
4. qlearningAgents則為小精靈的agent放置處
最主要與原Project3的程式不同之處
1. 動態參數我們是在pacman.py內部參數的地方(762行)
runGames(**args,alpha=0.6,gamma=0.4,epsilon=0.6)設定 
runGames function內做iteration次數地調整的