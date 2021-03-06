import math # math모듈 import

# arguments: pos, delta, target
# - pos = (x, y) tuple
# - delta = (dx, dy) tuple
# - target = (x, y) tuple
# returns: (pos, done)
# - pos = (x, y) tuple
# - done = True if arrived
def move_toward(pos, delta, target):   # pos - 캐릭터 좌표, delta - 마우스 클릭 좌표와 캐릭터 간의 거리, target - 마우스 클릭 좌표
    done = False                       # 도달했는지 안했는지 체크하는 BOOL값
    x,y = pos[0] + delta[0], pos[1] + delta[1] # pos[0] - 캐릭터 x 좌표 , delta[0] - 캐릭터 x좌표와 target x좌표 간의 거리 pos[1] - 캐릭터 y좌표 , delta[1] - 캐릭터 y좌표와 target y좌표 간의 거리

    if delta[0] > 0 and x >= target[0] or delta[0] < 0 and x <= target[0]: # 캐릭터 x좌표에 거리를 더했을때 target의 x좌표에 도달했는지 체크
        done = True                                                        # 도달했다면 done을 True로 바꿔준다.
    if delta[1] > 0 and y >= target[1] or delta[1] < 0 and y <= target[1]: # 캐릭터 y좌표에 거리를 더했을때 target의 y좌표에 도달했는지 체크
        done = True                                                        # 도달했다면 done을 True로 바꿔준다.

    pos = target if done else (x,y)                                        # done이 True(즉, target에 도착했다면)라면 pos = target이고 아니라면 pos = (x,y)

    return (pos, done)                                                     # 좌표값과 BOOL값을 반환

#원하는 위치(마우스로 클릭한 좌표)까지 캐릭터의 위치를 움직여주는 함수

# arguments: pos, target, speed
# - pos = (x, y) tuple
# - target = (x, y) tuple
# - speed = pixels per frame
# returns: (dx, dy)
# - x/y pixels per frame
def delta(pos, target, speed):         # pos - 캐릭터 좌표, target - 마우스 클릭 좌표 , speed - 캐릭터의 속도값 int형 변수
    dx, dy = target[0] - pos[0], target[1] - pos[1]  #dx - 타겟 x좌표에서 캐릭터 x좌표를 뺀 값 ,  dy - 타겟 y좌표에서 캐릭터 y좌표를 뺀값
    distance = math.sqrt(dx**2 + dy**2)  # 점과 점 사이의 거리를 구하는 공식 : 거리이기 때문에 음수가 아니어야함.
    if distance == 0: return 0, 0        #distance가 0이라면 tuple(0,0)을 반환
    return dx * speed / distance, dy * speed / distance #분기가 되지 않는다면(if문 조건에 걸리지 않을 시) dx*speed/distance값을 반환

#캐릭터 위치,목표 위치,속도 3가지 인자로 점과 점사이의 거리를 점점 가까워지게 거리를 계산해주는 함수


# object version

def move_toward_obj(obj):               # 클래스 객체를 인자로 받는다.
    if obj.target == None: return       # target이 존재하지 않는다면 move_toward에 인자로 받은 obj의 멤버변수인 pos,delta,target을 인자로 호출하여 pos,done값을 반환한다.
    pos, done = move_toward(obj.pos, obj.delta, obj.target)
    if done:                            # done이 True라면 (객체가 도착한 target의 위치에 있을 때)
        obj.target = None               # obj.target(목표 위치) 은 값이 없다.
        obj.delta = 0,0                 # obj.delta(거리)도 값이 0,0

    obj.pos = pos                       # move_toward로 pos에 받은 값을 obj.pos에 넣어준다.

def set_target(obj, target):            # 객체와 목표로 할 위치를 인자로 받는다.
    obj.target = target                 # 객체의 멤버변수 obj.target에 인자로 받은 target의 위치값을 넣는다.
    obj.delta = 0,0 if target is None else delta(obj.pos, target, obj.speed) # obj.delta(객체가 움직이는 거리)에 target이 없을 시에 0,0을 넣고 그게 아니라면 delta()를 호출하여 값을 받아 obj.delta에 값을 넣어준다.