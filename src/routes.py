from flask import render_template, request, redirect, url_for, session, make_response
from flask import current_app as app
from .models import db, Player
from .engine import get_riddle, check_answer, get_hint, RIDDLES

@app.route('/')
def index():
    if 'player_id' in session:
        return redirect(url_for('game'))
    return render_template('index.html', riddle_count=len(RIDDLES))

@app.route('/hint')
def hint():
    if 'player_id' not in session:
        return "", 401
    
    player = Player.query.get(session['player_id'])
    hint_text = get_hint(player.current_level)
    return f'<p class="hint"><em>Hint: {hint_text}</em></p>'

@app.route('/join', methods=['POST'])
def join():
    player_name = request.form.get('player_name')
    if not player_name or not player_name.isalnum() or len(player_name) > 12:
        return "Invalid name. Use up to 12 alphanumeric characters.", 400
    
    player = Player.query.filter_by(name=player_name).first()
    if not player:
        player = Player(name=player_name)
        db.session.add(player)
        db.session.commit()
    
    session['player_id'] = player.id
    
    if request.headers.get('HX-Request'):
        return render_template('game_content.html', player=player, riddle=get_riddle(player.current_level))
    return redirect(url_for('game'))

@app.route('/game')
def game():
    if 'player_id' not in session:
        return redirect(url_for('index'))
    
    player = Player.query.get(session['player_id'])
    if not player:
        session.pop('player_id', None)
        return redirect(url_for('index'))
        
    riddle = get_riddle(player.current_level)
    return render_template('game.html', player=player, riddle=riddle)

@app.route('/answer', methods=['POST'])
def answer():
    if 'player_id' not in session:
        return redirect(url_for('index'))
    
    player = Player.query.get(session['player_id'])
    user_answer = request.form.get('answer')
    
    if check_answer(player.current_level, user_answer):
        player.current_level += 1
        player.score += 1
        db.session.commit()
        
        riddle = get_riddle(player.current_level)
        if not riddle:
            return render_template('end_game.html', score=player.score)
            
        return render_template('game_content.html', player=player, riddle=riddle, correct=True)
    else:
        riddle = get_riddle(player.current_level)
        return render_template('game_content.html', player=player, riddle=riddle, correct=False)

@app.route('/skip', methods=['POST'])
def skip():
    if 'player_id' not in session:
        return redirect(url_for('index'))
    
    player = Player.query.get(session['player_id'])
    # Get the answer for the level being skipped
    skipped_riddle = get_riddle(player.current_level)
    skipped_answer = skipped_riddle['answer'] if skipped_riddle else None
    
    player.current_level += 1
    db.session.commit()
    
    riddle = get_riddle(player.current_level)
    if not riddle:
        return render_template('end_game.html', score=player.score)
        
    return render_template('game_content.html', player=player, riddle=riddle, skipped_answer=skipped_answer)

@app.route('/leaderboard')
def leaderboard():
    top_players = Player.query.order_by(Player.score.desc()).limit(10).all()
    return render_template('leaderboard.html', players=top_players)
