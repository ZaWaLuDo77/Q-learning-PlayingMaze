import matplotlib.pyplot as plt



class maze_line():
    
    def __init__(self,set_round, total_state_history, size):
        
        self.set_round = set_round
        self.total_state_history = total_state_history
        self.size = size
        print("this is 18x18 maze")
        ax = plt.gca()
        
        # 繪製迷宮
        plt.plot([1, 1], [14, 17], color='black', linewidth=2)
        plt.plot([2, 5], [17, 17], color='black', linewidth=2)
        plt.plot([2, 2], [17, 15], color='black', linewidth=2)
        plt.plot([2, 4], [15, 15], color='black', linewidth=2)
        plt.plot([3, 5], [16, 16], color='black', linewidth=2)
        plt.plot([5, 5], [16, 12], color='black', linewidth=2)
        plt.plot([2, 4], [14, 14], color='black', linewidth=2)
        plt.plot([0, 4], [13, 13], color='black', linewidth=2)
        plt.plot([6, 6], [13, 17], color='black', linewidth=2)
        plt.plot([7, 7], [12, 18], color='black', linewidth=2)
        plt.plot([8, 8], [13, 17], color='black', linewidth=2)
        plt.plot([7, 13], [12, 12], color='black', linewidth=2)
        plt.plot([13, 13], [12, 13], color='black', linewidth=2)
        plt.plot([9, 9], [13, 14], color='black', linewidth=2)
        plt.plot([9, 12], [13, 13], color='black', linewidth=2)
        plt.plot([9, 14], [14, 14], color='black', linewidth=2)
        plt.plot([14, 14], [14, 13], color='black', linewidth=2)
        plt.plot([9, 15], [15, 15], color='black', linewidth=2)
        plt.plot([9, 12], [16, 16], color='black', linewidth=2)
        plt.plot([9, 11], [17, 17], color='black', linewidth=2)
        plt.plot([9, 9], [17, 16], color='black', linewidth=2)
        plt.plot([12, 16], [17, 17], color='black', linewidth=2)
        plt.plot([16, 16], [15, 17], color='black', linewidth=2)
        plt.plot([15, 15], [6, 16], color='black', linewidth=2)
        plt.plot([14, 14], [16, 17], color='black', linewidth=2)
        plt.plot([13, 13], [15, 16], color='black', linewidth=2)
        plt.plot([17, 17], [17, 9], color='black', linewidth=2)
        plt.plot([16, 16], [13, 7], color='black', linewidth=2)
        plt.plot([16, 17], [7, 7], color='black', linewidth=2)
        plt.plot([18, 17], [6, 6], color='black', linewidth=2)
        plt.plot([1, 4], [12, 12], color='black', linewidth=2)
        plt.plot([1, 2], [11, 11], color='black', linewidth=2)
        plt.plot([3, 11], [11, 11], color='black', linewidth=2)
        plt.plot([12, 14], [11, 11], color='black', linewidth=2)
        plt.plot([14, 14], [10, 12], color='black', linewidth=2)
        plt.plot([1, 1], [11, 12], color='black', linewidth=2)
        plt.plot([11, 11], [11, 10], color='black', linewidth=2)
        plt.plot([8, 8], [11, 9], color='black', linewidth=2)
        plt.plot([1, 7], [10, 10], color='black', linewidth=2)
        plt.plot([9, 11], [10, 10], color='black', linewidth=2)
        plt.plot([1, 1], [10, 6], color='black', linewidth=2)
        plt.plot([2, 2], [9, 6], color='black', linewidth=2)
        plt.plot([2, 1], [6, 6], color='black', linewidth=2)
        plt.plot([2, 7], [9, 9], color='black', linewidth=2)
        plt.plot([15, 9], [9, 9], color='black', linewidth=2)
        plt.plot([6, 8], [8, 8], color='black', linewidth=2)
        plt.plot([11, 14], [8, 8], color='black', linewidth=2)
        plt.plot([9, 9], [9, 7], color='black', linewidth=2)
        plt.plot([10, 10], [9, 7], color='black', linewidth=2)
        plt.plot([3, 9], [7, 7], color='black', linewidth=2)
        plt.plot([5, 5], [8, 2], color='black', linewidth=2)
        plt.plot([3, 3], [2, 7], color='black', linewidth=2)
        plt.plot([4, 4], [1, 5], color='black', linewidth=2)
        plt.plot([4, 4], [6, 7], color='black', linewidth=2)
        plt.plot([6, 6], [0, 6], color='black', linewidth=2)
        plt.plot([2, 2], [4, 1], color='black', linewidth=2)
        plt.plot([0, 2], [3, 3], color='black', linewidth=2)
        plt.plot([1, 2], [1, 1], color='black', linewidth=2)
        plt.plot([1, 1], [1, 2], color='black', linewidth=2)
        plt.plot([1, 3], [5, 5], color='black', linewidth=2)
        plt.plot([6, 10], [6, 6], color='black', linewidth=2)
        plt.plot([6, 9], [5, 5], color='black', linewidth=2)
        plt.plot([7, 18], [4, 4], color='black', linewidth=2)
        plt.plot([6, 8], [3, 3], color='black', linewidth=2)
        plt.plot([7, 8], [1, 1], color='black', linewidth=2)
        plt.plot([8, 8], [1, 3], color='black', linewidth=2)
        plt.plot([7, 7], [1, 2], color='black', linewidth=2)
        plt.plot([9, 15], [3, 3], color='black', linewidth=2)
        plt.plot([10, 14], [2, 2], color='black', linewidth=2)
        plt.plot([9, 14], [1, 1], color='black', linewidth=2)
        plt.plot([9, 9], [1, 3], color='black', linewidth=2)
        plt.plot([15, 15], [0, 3], color='black', linewidth=2)
        plt.plot([16, 16], [1, 4], color='black', linewidth=2)
        plt.plot([17, 17], [1, 3], color='black', linewidth=2)
        plt.plot([10, 14], [5, 5], color='black', linewidth=2)
        plt.plot([15, 18], [5, 5], color='black', linewidth=2)
        plt.plot([14, 14], [5, 7], color='black', linewidth=2)
        plt.plot([12, 14], [7, 7], color='black', linewidth=2)
        plt.plot([12, 12], [7, 6], color='black', linewidth=2)
        plt.plot([13, 12], [6, 6], color='black', linewidth=2)
        
        # 繪製狀態起點與終點
        plt.text(0.5, 17.25, 'S',size=11, ha='center',color='g')
        plt.text(17.5, 0.25, 'F',size=11, ha='center',color='r')
        
        # 設定繪圖範圍與塗銷刻度
        ax.set_xlim(0, 18)
        ax.set_ylim(0, 18)
        plt.tick_params(axis='both', which='both', bottom='off', top='off',
                        labelbottom='off', right='off', left='off', labelleft='off')
        
        # 初始目前位置S0繪製綠色圓形
        self.line, = ax.plot([0.5], [17.5], marker="o", color='g', markersize=12)

    def init_set(self):
        self.line.set_data([], [])
  
        return self.line
    


    
