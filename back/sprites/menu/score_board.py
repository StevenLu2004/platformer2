import back.sprites.component as c
import utils.fonts as f
import utils.functions as utils


class ScoreBoard:
    def __init__(self, pos, *, buttons=tuple(['quit']), size=(300, 240), align=(0, 0)):
        # display
        self.pos = utils.top_left(pos, size, align=align)
        self.size = size
        self.win = None
        # buttons
        self.buttons = {}
        x = 140
        for name in buttons:
            self.buttons[name] = c.Button(
                (self.pos[0] + self.size[0] // 2, self.pos[1] + x), (200, 40), name,
                font=f.tnr(22), align=(1, 0), background=(230, 230, 230)
            )
            x += 60

    def in_range(self, pos):
        return self.pos[0] < pos[0] < self.pos[0] + self.size[0] and self.pos[1] < pos[1] < self.pos[1] + self.size[1]

    def process_events(self, events):
        # buttons
        pos, clicked = events['mouse-pos'], (events['mouse-left'] == 'down')
        if clicked:
            for name in self.buttons:
                if self.buttons[name].in_range(pos):
                    return self.buttons[name].text
        elif 'return' in events['key-down']:
            return 'quit'

    def show(self, ui, win, score, *, pan=(0, 0)):
        pos = self.pos[0] + pan[0], self.pos[1] + pan[1]
        # container
        ui.show_div(pos, self.size, color=(255, 204, 204) if win else (204, 204, 255))
        ui.show_div(pos, self.size, border=2)
        # round
        ui.show_text(
            (self.size[0] // 2, 40), f'YOU  {"WIN" if win else "LOSE"}!', f.cambria(28), align=(1, 0), pan=pos
        )
        ui.show_text(
            (self.size[0] // 2, 80), f'Score: {score}', f.cambria(25), align=(1, 0), pan=pos
        )
        # buttons
        for name in self.buttons:
            self.buttons[name].show(ui)
