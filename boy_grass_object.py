from pico2d import *

# Game object class here


class Grass:
    #객체가 생성될때 처음 호출되는 함수, 객체의 초기상태를 설정한다. 클래스안에서 함수를 쓰려면
    #self라는 파라미터를 써줘야한다. 생성된 ㄱ객체 그 자신을 가리킨다.
    def __init__(self):  #모든 클래스안에 들어가는 함수이다. __init__  -> 생성자 함수이다.
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)
    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = 0,90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame +1) %8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0 , 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global boy

    running = True
    grass = Grass()
    boy = Boy()


def update_world():
    grass.update()
    boy.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    pass


open_canvas()

# initialization code
reset_world()



# game main loop code

while running:
    handle_events()
    update_world() # game Logic
    render_world() # draw game world
    delay(0.05)


# finalization code

close_canvas()
