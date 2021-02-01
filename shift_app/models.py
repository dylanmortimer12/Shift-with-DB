from app import db


class play_by_play(db.Model):
    __tablename__ = 'PLAY_BY_PLAY'

    PLAYER_KEY = db.Column(db.Integer, primary_key=True, autoincrement=True)
    BATTER_NAME = db.Column(db.String(50))
    PITCHER_HAND = db.Column(db.String(10))
    BATTER_HAND = db.Column(db.String(10))
    STRIKES = db.Column(db.Integer)
    BALLS = db.Column(db.Integer)
    CX = db.Column(db.Integer)
    CY = db.Column(db.Integer)
    HIT_DIRECTION = db.Column(db.Float)

    def __init__(self, name, phand,bhand, s,b,cx,cy,hit_dir):
        self.BATTER_NAME = name
        self.PITCHER_HAND = phand
        self.BATTER_HAND = bhand
        self.STRIKES = s
        self.BALLS = b
        self.CX = cx
        self.CY = cy
        self.HIT_DIRECTION = hit_dir