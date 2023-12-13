import os


class Ball:
    def __init__(self, texture=None, texture_rect=None, passed=None):
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
        self.passes = []

    def to_dict(self):
        return {"passes": [a_pass.to_dict() for a_pass in self.passes]}

    def set_texture(self, size=80):
        self.texture = os.path.join(
            f"assets/images/img-{size}px/metal_ball.png")

    # clears the balls potential passes
    def clear_passes(self):
        self.passes = []

    # adds a to the pass list of potential passes
    def add_pass(self, a_pass):
        self.passes.append(a_pass)
