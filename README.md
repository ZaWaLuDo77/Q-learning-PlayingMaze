# Q-learning-PlayingMaze
透過Q-learning訓練智能體(agent)，學習在18×18大小的迷宮中探索，找到最佳路徑。

# 首要工作
安裝繪圖工具套件  `pip install matplotlib`  
安裝numpy套件 `pip install numpy`  

# 執行文件
  
  `RL_robot_Qlearning18x18_lookstep.py` : Q-learning 訓練開始，並以gif顯示最佳完成迷宮結果  
    
  (顯示最佳結果)  
  <img src="https://github.com/ZaWaLuDo77/Q-learning-PlayingMaze/blob/main/animation/Moving_round271.gif"   width = "375"/>  
    
  (記錄每一回合步數過程)  
  <img src="https://github.com/ZaWaLuDo77/Q-learning-PlayingMaze/blob/main/animation/output_step.png"   width = "375"/>
  
# 其他
 由於每次初始化皆為隨機，因此每次訓練結果都會有所不同，也可根據參數調整: 學習率(learning rate), 折扣率(discount rate), 貪婪率(greedy rate) 而有不同的收斂效果。  
 針對優化參數調整，在此附上研究結果: https://ieeexplore.ieee.org/abstract/document/9651084
