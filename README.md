# 應用於Pacman之強化學習

## About this project (關於計畫)
本專題旨在模擬兩個Agent如何利用所處環境中的資訊，進行對抗並達成各自目標。我們運用了強化式學習中的Q-learning與SARSA演算法進行實作，作為兩個Agent的學習方式，並透過Approximate Q-learning與Approximate SARSA改善其效能，實驗結果顯示： Approximate Q-learning與Approximate SARSA成功改善Q-learning與SARSA的不足之處，實現兩個Agent互相對抗並達成各自目標之目的。
## Environment (系統環境)
* Python 3.6
* 專案內含繪製PACMAN動畫地圖，因此需另行安裝Pygame繪製2D地圖.
## Requirement(需要裝置)
* 可運行Python3.6的電腦即可
## 使用說明
請將Code內兩文件下載入電腦內，可在Windows Command Prompt執行，執行時需於command Prompt內輸入
* Q-Learning 演算法
  1. cd 至本地QlearningAgent檔案存放地址
  2. 輸入python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
* Approximate Q-learning vs Approximate SARSA
  1. cd 至本地ApproximateQlearning(DynamicParameterVersion)檔案存放地址
  2. 輸入python start.py -p ApproximateQAgent -g ApproximateGhostQAgent -a extractor=SimpleExtractor  -x 50 -n 60 -l mediumGrid
## 參考資料
* Mesut Yang, & Carl Qi. (2021). CS188|Summer 2021. Retrieved from https://inst.eecs.berkeley.edu/~cs188/su21/. (November 8,2021)
* Jo, T. (2021). Machine Learning Foundations: Supervised, Unsupervised, and Advanced Learning. Springer Nature.
* Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press.
* Stuart, R., & Norvig, P. (2010). Artificial intelligence: A modern approach 3rd Edition. Upper Saddle River, New Jeysey.
* Xu, Z. X., Cao, L., Chen, X. L., Li, C. X., Zhang, Y. L., & Lai, J. (2018). Deep reinforcement learning with sarsa and q-learning: A hybrid approach. IEICE TRANSACTIONS on Information and Systems, 101(9), 2315-2322.
* Alfakih, T., Hassan, M. M., Gumaei, A., Savaglio, C., & Fortino, G. (2020). Task offloading and resource allocation for mobile edge computing by deep reinforcement learning based on SARSA. IEEE Access, 8, 54074-54084.




