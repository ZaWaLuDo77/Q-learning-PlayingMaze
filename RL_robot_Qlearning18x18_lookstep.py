import numpy as np
import matplotlib.pyplot as plt
from Maze_Env import maze_18x18 as env
from Maze_Line import maze_line 
import matplotlib.animation as animation

''' 參數設置 '''
###########################################
# 迭帶上限
episode_MAX_setting = 999

# 一次迭代步數上限
step_setting = 300

# learning rate 可調參數
eta = 0.8   

# discount rate 可調參數 
gamma = 0.9   

# greedy rate 可調參數
epsilon = 0.2 
###########################################

''' Q-learning function '''
# 透過環境狀態theta設置機率pi
def simple_convert_into_pi_from_theta(theta):
    [m, n] = theta.shape  
    pi = np.zeros((m, n))
    for i in range(0, m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :])  
    pi = np.nan_to_num(pi)  

    return pi

# 設定動作
def get_action(s, Q, epsilon, pi_0): 
    direction = ["up", "right", "down", "left"]

    if np.random.rand() < epsilon:
        next_direction = np.random.choice(direction, p=pi_0[s, :])
    else:
        next_direction = direction[np.nanargmax(Q[s, :])]

    if next_direction == "up":
        action = 0
    elif next_direction == "right":
        action = 1
    elif next_direction == "down":
        action = 2
    elif next_direction == "left":
        action = 3

    return action

# 設定下一步動作選擇
def get_s_next(s, a, Q, epsilon, pi_0):
    direction = ["up", "right", "down", "left"]
    next_direction = direction[a]  

    if next_direction == "up":
        s_next = s - size  
    elif next_direction == "right":
        s_next = s + 1  
    elif next_direction == "down":
        s_next = s + size  
    elif next_direction == "left":
        s_next = s - 1  

    return s_next

def Q_learning(s, a, r, s_next, Q, eta, gamma):

    if s_next == size*size-1:  
        Q[s, a] = Q[s, a] + eta * (r - Q[s, a])

    else:
        Q[s, a] = Q[s, a] + eta * (r + gamma * np.nanmax(Q[s_next,: ]) - Q[s, a])

    return Q

def goal_maze_ret_s_a_Q(Q, epsilon, eta, gamma, pi):
    s = 0  
    a = a_next = get_action(s, Q, epsilon, pi) 
    s_a_history = [[0, np.nan]] 

    # 每一回合執行步數
    for i in range(step_setting):
        a = a_next  
        s_a_history[-1][1] = a
        s_next = get_s_next(s, a, Q, epsilon, pi)
        s_a_history.append([s_next, np.nan])

        if s_next == size*size-1:
            r = 1  
            a_next = np.nan
        else:
            r = 0
            a_next = get_action(s_next, Q, epsilon, pi)

        Q = Q_learning(s, a, r, s_next, Q, eta, gamma)

        if s_next == size*size-1 or len(s_a_history) >1000:  
            break
        else:
            s = s_next

    return [s_a_history, Q]




''' 每一個的繪圖內容 '''
def animate(i):
    
    state = total_state_history[set_round][i]  # 繪製目前的位置
    x = (state % size) + 0.5  # 狀態的x座標以3除之，再於得到的餘數+0.5
    y = 17.5 - int(state / size)  # y座標以3除之，再以2.5減去商數
    draw.line.set_data(x, y)
    return draw.line


''' 執行訓練 '''
if __name__ == "__main__":    
    
    #導入迷宮
    size, theta_0 = env.maze_array()

    # 迷宮初始化
    pi_0 = simple_convert_into_pi_from_theta(theta_0)
    [a, b] = theta_0.shape
    Q = np.random.rand(a, b) * theta_0 
    
    episode = 0
    repeat = 0
    flag = 9999
    output_step = []
    total_state_history = [] 
    
    # 訓練迭代
    while True:
    
        [s_a_history, Q] = goal_maze_ret_s_a_Q(Q, epsilon, eta, gamma, pi_0) #訓練一回合
        # print(len(s_a_history) - 1)  # 可顯示當前使用步數
        
        output_step.append(len(s_a_history) - 1)
        epsilon = epsilon / 1.05 
        if flag > len(s_a_history) - 1:
            flag = len(s_a_history) - 1
        episode = episode + 1
        
        if episode >= episode_MAX_setting :
            break
    
        if len(s_a_history) - 1 <= 62:
            repeat = repeat + 1
        else :
            repeat = 0
            
        state_history = [] 
        
        for i in range(len(s_a_history)):
            state_history.append(s_a_history[i][0]) 
        
        total_state_history.append(state_history)
            
        if repeat >= 10:     
            break
            
    
    plt.plot(output_step,color='g')
    plt.savefig("./animation/output_step.png")
        


    # 繪製動畫
    set_round = episode-1 #觀看第N回合數 (預設最後一回合)
    fig = plt.figure(figsize=(7, 7))
    draw = maze_line(set_round, total_state_history, size)   
    anim = animation.FuncAnimation(fig, animate, init_func=draw.init_set, frames=len(
        total_state_history[set_round]), interval=50, repeat=False)
    # plt.show()
    anim.save('./animation/Moving_round{}.gif'.format(set_round), fps=1/0.05)

    # 觀察每回合更新次數
    for i in range(len(total_state_history)-1):
        print("{}round: ".format(i+1) + str(len(total_state_history[i])-1))
        
    print("Total rounds:"+str(set_round))





            
            
  
           